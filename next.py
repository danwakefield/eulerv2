#!/usr/bin/env python3
# encoding: utf-8
from __future__ import print_function

import argparse
from glob import glob
from string import Template
import textwrap
import os

import requests
from bs4 import BeautifulSoup as beautifulsoup

TEMPLATE = (
'''#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=$number

$text
"""
from __future__ import print_function
from utils import timer


ANSWER = None


def test_answer():
    if ANSWER is None:
        assert 0, 'Not Completed'
    else:
        assert ANSWER == main()

$resource

@timer
def main():
    pass


if __name__ == '__main__':
    print(main())
''')

def main():
    parser = argparse.ArgumentParser(description='Downloads the next problem '
                                     'from project euler and creates the file '
                                     'for it')

    parser.add_argument('-o', '--overwrite', action='store_true',
                        default=False, help='Overwrite the file')
    parser.add_argument('number', metavar='NUMBER', nargs='?', type=int,
                        help='Number of the problem to download')

    args = parser.parse_args()

    if args.number:
        get(args.number, args.overwrite)
    else:
        problem_files = sorted(glob('[0-9]*_*.py'))
        last_problem_file = problem_files[-1]
        last_problem_number = int(last_problem_file.split('_', 1)[0])
        get(last_problem_number + 1, args.overwrite)


def get(num, overwrite):
    euler_url = 'http://projecteuler.net/'
    url = '{0}problem={1}'.format(euler_url, num)
    r = requests.get(url)
    soup = beautifulsoup(r.content)
    c = soup.find_all(id='content')[0]
    problem_text = []
    resource_file = None
    for x in c.find_all('sup'):
        x.string = '^' + ''.join(list(x.stripped_strings))

    for x in c.find_all('sub'):
        x.string = '_' + ''.join(list(x.stripped_strings))

    for x in c.find_all('div', class_='problem_content'):
        if x.find_all('a'):
            resource_file = '{0}{1}'.format(
                euler_url, x.find_all('a', href=True)[0]['href'])
        problem_text.append(' '.join(list(x.stripped_strings)))

    problem_text = '\n'.join(textwrap.wrap('\n'.join(problem_text)))
    problem_text = problem_text.replace(' ^', '^')
    problem_text = problem_text.replace(' _', '_')
    problem_name = (c.find_all('h2')[0].string
                    .lower()
                    .replace(' ', '_')
                    .replace('-', '_'))

    print(num)
    print(problem_name, end='\n\n')
    print(problem_text)

    if resource_file:
        resource_file_name = './data/{0:03d}_{1}.txt'.format(num, problem_name)
        make_file(resource_file_name,
                  requests.get(resource_file).content,
                  executable=False)

        resource = ("\nwith open('{0}', 'r') as f:\n    DATA = f.readlines()\n\n"
                    ''.format(resource_file_name))

    else:
        resource = ''

    t = Template(TEMPLATE)
    s = t.safe_substitute(number=num, text=problem_text, resource=resource)
    file_name = './{0:03d}_{1}.py'.format(num, problem_name)
    if not os.path.isfile(file_name):
        make_file(file_name, s)
    else:
        if overwrite:
            make_file(file_name, s)
        else:
            print('\n{0} already exists'.format(file_name))


def make_file(fn, cont, executable=True):
    if isinstance(cont, type(b'')):
        open_mode = 'wb+'
    else:
        open_mode = 'w+'

    with open(fn, open_mode) as f:
        f.write(cont)

    if executable:
        os.chmod(fn, 0o775)


if __name__ == '__main__':
    main()

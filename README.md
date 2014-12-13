
These are my solutions to the brilliant problems at
[https://projecteuler.net](Project Euler).  

This site was one of the first things that got me truly interested in
programming, 'programming' being a loose term back then.  
Many of my old solutions are just plain bad,
Brute force and plagiarism are rampant as is
complete ignorance of PEP8 and even a consistent personal style.
(Blame it on reading K&R C and trying to apply that to python)


Over the years I have learned and been taught new techniques and just generally
improved in many areas of my programming skill.
The exception to this is maths, While I have a good knowledge of basic algebra, 
linear equations and other useful things I lack the understanding of more advanced theories.

To attempt to remedy this I thought back to the challenges herein. Many Project
Euler problems require an understanding of some aspects of higher math and as
such I have made it my goal to learn concepts one at a time as I complete the
challenges.

### How Its laid out.

`next.py` pulls the problem text from Project Euler displaying it in the console
and creating a template file for the problem. It also downloads and data files
associated with the problem to the data folder and adds a section to the
template the reads the file into the DATA global variable.

    $ ./next.py 1   # Get Problem one.
    $ ./next.py N   # Get problem N
    $ ./next.py     # Get Problem N where N = X+1 where X is highest problem
                    # number in the sorted directory listing


`next.py` uses BeatifulSoup4 to parse the pages. To install it run

    $ pip3 install beautifulsoup4
    # or
    $ apt-get install python-beatifulsoup4

The utils directory is used to house functions that have been useful over
multiple problems. They are separated in the best way I can think of at the
moment and imported into the flat .utils namespace.

#### Warning
The problem files are named in such a way that prevents the being easily
imported. This wasnt really the plan but has made it so that any time a problem
has roots in another its forces me to generalize the problem and export it to
utils.


If you have found this repo while attempting to solve the problems for yourself
I recommend not just copying to code or the answer. You should understand what
you are doing otherwise it doesnt help at all. That being said using the
answers to troubleshoot out by 1 errors is helpful.


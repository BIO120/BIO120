# `course_sphinx_template:` A Template Course Website Using Sphinx

In data science and computational biology, Jupyter notebooks reign supreme. While
I have gripes (and joy) about this, it breaks my heart to see plain-text websites 
for courses with links to aesthetically gross and poorly documented raw Jupyter Notebooks.
This template serves as a way to easily spin up course websites where Jupyter 
Notebooks are the core of the content (including lessons, problem sets, and
recitations). I've documented it so you can spin one up easily, with the boring 
bits boilerplated. This template is inspired by the course websites for [BE/Bi 103: Principles of Biological Data Analysis](https://bebi103.caltech.edu)
taught by [Dr. Justin Bois](https://bois.caltech.edu) at Caltech (one of the most 
influential courses in my own scientific career).

## Usage

To use this repository for your course website, click on the big-ass "Use Template"
button at the top-right of this page, enter your course details, and create your 
repository. Congratulations, you've just set up your own course website!


To finish the deployment, navigate to your new repository's settings, click on the "Pages" 
pane, and set the deploy branch to `gh-pages`.

## Configuration
You need to configure a few things to get your website off the ground. 

1. **Edit `setup.py`**: Add your email, course information, and site URL, along with the 
version of the course website. 

2. **Edit `conf.py`**: Add your email and course description to the relevant settings (and only those settings). 


## Populating with Content

The best way (right now) to figure out the repository structure is to dig around 
in the guts and figure out what does what. The major components to look at are 
the folders `lessons` and  `problem_sets`, which house the Jupyter notebooks 
that make up this website. Also edit `index.rst`, `syllabus.rst`, and `policies.rst`
to finish initiating the website. New pages can be added by creating a new RST file 
(such as `people.rst`) and then adding it to the `toctree` setting data block in `index.rst`.

## License
All creative work (e.g. prose, artwork) is licensed under a [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) license.
The software herein is licensed under a standard MIT license, which reads as
follows:

```
MIT License

Copyright (c) 2023 Griffin Chure 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

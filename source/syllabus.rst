
.. note::
    This page is generated using Restructured Text, and not a Jupyter Notebook.

Syllabus
--------
You will almost certainly have a table-based syllabus that lists the days,
topics, related readings, exams, or due problem sets. You can set this up 
easily using a table. Sphinx, by default, supports `ReStructured-Text <https://github.com/ralsina/rst-cheatsheet/blob/master/rst-cheatsheet.rst>`_ 
for markup, an alternative to markdown, which supports tables like the following:

.. list-table:: Syllabus
    :widths: 5, 10, 50, 20, 20
    :header-rows: 1

    * - Week
      - Date
      - Topic 
      - Readings 
      - Due

    * - 1
      - 1/8/2024
      - Intro. to Evolution
      - `Darwin 1859 <https://en.wikipedia.org/wiki/On_the_Origin_of_Species>`_
      - --

    * - 1
      - 1/10/2024
      - Intro. to Genetics 
      -  :download:`Mendel 1865 <papers/gm-65.pdf>`
      - `Problem Set 1 <problem_sets/problem_set_1.html>`_

    * - 2
      - 1/15/24
      - You get the idea 
      - More readings
      - More homeworks!


This table is produced from this RST code.

.. code-block::
    
    .. list-table:: Syllabus
        :widths: 5, 10, 50, 20, 20
        :header-rows: 1

        * - Week
          - Date
          - Topic 
          - Readings 
          - Due

        * - 1
          - 1/8/2024
          - Intro. to Evolution
          - `Darwin 1859 <https://en.wikipedia.org/wiki/On_the_Origin_of_Species>`_
          - --

        * - 1
          - 1/10/2024
          - Intro. to Genetics 
          -  :download:`Mendel 1865 <papers/gm-65.pdf>`
          - `Problem Set 1 <problem_sets/problem_set_1.html>`_

        * - 2
          - 1/15/24
          - You get the idea 
          - More readings
          - More homeworks!


Note that you can link to external websites, internal files, or other pages 
within the same site.
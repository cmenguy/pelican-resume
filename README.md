Introduction
============
[![Build Status](https://travis-ci.org/cmenguy/pelican-resume.svg?branch=master)](https://travis-ci.org/cmenguy/pelican-resume)

This is **pelican_resume**, a Pelican plugin enabling automatic PDF resume generation for one of your Pelican pages.
The main benefit is that you only need to maintain a single Markdown version of your resume - the corresponding
HTML and generated PDF are completely automated so you can showoff your awesome resume both online and physically.

It allows you write your own resume style, or use one of the styles provided by this plugin.

Installation
============

Installing is easy, simply run:

    pip install pelican-resume

Alternatively, you can also clone this repository and install it manually:

    git clone git@github.com:cmenguy/pelican-resume.git
    python setup.py install

In **pelicanconf.py** you need to update your plugins to inclue **pelican_resume**:

    PLUGINS = [
        # ...
        "pelican_resume",
        # ...
    ]

Settings
========

You can customize the behavior of the plugin by adding the variables below to your **pelicanconf.py**.
For simple usage, the default values should work but will look for a specific input file and produce a specific PDF name.

Setting name | Default value | Usage
--- | --- | ---
`RESUME_SRC` | pages/resume.md | Path to your Markdown resume page (relative to your `PATH` variable).
`RESUME_PDF` | pdfs/resume.pdf | Path to the generated PDF output (relative to your `OUTPUT_PATH` variable).
`RESUME_CSS_DIR` | *<module-install-path>/static/css* | Path to the directory containing your resume CSS files.
`RESUME_TYPE` | moderncv | Type of resume to use. Has to match one of the CSS filenames under `RESUME_CSS_DIR`.
`RESUME_PANDOC` | pandoc | Path to your `pandoc` command. If `pandoc` is in your `PATH`, then it can be left as default.
`RESUME_WKHTMLTOPDF` | wkhtmltopdf | Path to your `wkhtmltopdf` command. If `wkhtmltopdf` is in your `PATH`, then it can be left as default.

Usage
=====

Once you have the plugin properly configured, it will generate a PDF version of your resume automatically under the
`RESUME_PDF` location everytime you run `pelican content`.

It can then easily be embedded into your Pelican website by referencing that location - thus ensuring your visitors
can download the latest version of your resume which is consistent with your Markdown file.

Contributing
============

[Contributing Guidelines](CONTRIBUTING.md)

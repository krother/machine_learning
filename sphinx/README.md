![](https://github.com/spicedacademy/datascience_source/workflows/build%20and%20deploy%20the%20site/badge.svg)


# Compiling the documentation

## Installation with pip

### 1. Create a virtual environment

    conda create -n doc python=3.7

### 2. Install packages

    pip install --user -r requirements.txt

Also install *LaTeX* (for formulas). On Ubuntu, do:

    sudo apt install mathtex
    sudo apt install texlive-latex-extra

### 3. Add main directory of repository to PYTHONPATH

Required to import `quiz_extension`.

    export PYTHONPATH=$PYTHONPATH:$(pwd)

### 4. Build the docs

*Compiles the HTML locally, so that you can check that everything looks
the way you want it, before publishing / deploying*.

    make teach

### 5. Publish

Done automatically via GitHub actions, see `.github/workflows/build_deploy.yml`

All you need to do is:

    git push origin master

----

## Guide for authors

Somewhat idealized description that we are working towards:

* there is one main table of contents that lists all encounters
* every project has a main page listing goals, a TOC and a few teasers
* ideally, every chapter has: images, a warmup, 1+ challenges, a recap, 1-5 link
s
* use `literalinclude::` for bigger scripts, `code::` for a few lines
* prefer written content over downloadable PDFs
* prefer banner headings for challenges and links

### Special Headings

Try:

    .. container:: banner warmup

    .. container:: banner recap

    .. container:: banner linux

    .. container:: banner db

    .. container:: banner docker

    .. container:: banner git

These refer to custom CSS code that is defined in the ``spiced.css`` file (found in
``themes/``).


## Docker

To prevent installation issues, you can build the documentation locally with Docker:

    make dockerbuild

If `make` does not run on your OS (Windows):

**Build / run container:**

    docker build -t ds_source .
    docker run -v /home/me/stuff/datascience_source/:/usr/src/app -itd --name ds_source ds_source

**Build:**

    docker exec -it ds_source make teach

Enter container through bash terminal:

*(Probably not needed, but good to know anyways)*

    docker exec -it ds_source bash

Stop / remove container:

    docker stop ds_source && docker rm ds_source


----

## License

Most of the content in this repository belongs to SPICED Academy.
Some other is based on earlier work by Kristian Rother published under the CC-BY-SA 4.0 License.
Other material is taken from third parties, in particular Chris Albon, O'Reilly and scipy-lectures (and some others).

I wish to say that it is cleanly documented everywhere what exactly the license is, but I'd be careful with that. If we want to publish our course material e.g. as a book, we need to check this thoroughly.

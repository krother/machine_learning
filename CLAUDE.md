# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **Sphinx-based educational course** on Machine Learning. The content is written in reStructuredText (`.rst`) and Markdown (`.md`), with Jupyter notebooks (`.ipynb`) and Python scripts as code examples.

The built site is published at: www.academis.eu/machine_learning

## Building the Documentation

```bash
# Install dependencies
pip install -r requirements.txt

# Build HTML output
make html

# Build and view (output goes to build/html/)
make html && open build/html/index.html
```

The `Makefile` delegates all targets to Sphinx via `sphinx-build`.

## Repository Structure

- **`index.rst`** — top-level table of contents, defines the course outline
- **`conf.py`** — Sphinx configuration (theme: furo, extensions: myst-parser, sphinx-design, sphinx-copybutton)
- **`fundamentals/`**, **`supervised/`**, **`unsupervised/`**, **`clustering/`**, **`deep_learning/`** — topic chapters, each as a subdirectory with `README.rst` and supporting files
- **`notebooks/`** — Jupyter notebooks organized by topic (fundamentals, regression, classification, deep_learning, etc.)
- **`solutions/`** — complete worked solutions (notebooks and scripts)
- **`challenges/`** — exercises and quizzes for students
- **`classroom_exercises/`** — in-class activity materials

## Content Conventions

- Chapter pages are `README.rst` files inside topic subdirectories
- Recap questions appear in `.. highlights::` blocks inside `.. container:: banner recap`

## Content Organization Pattern

Each ML topic follows this structure:
1. Conceptual explanation with math
2. Terminology table
3. Code example (inline or `.. literalinclude::`)
4. Recap questions at the end

New chapters should follow this pattern and be registered in `index.rst`.

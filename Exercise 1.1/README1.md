# Exercise 1.1 — Getting Started with Python

**Course:** CareerFoundry — Python for Web Developers (Full-Stack)  
**Author:** Ivan Cortes  
**Date:** October 2025

---

## Overview

This document provides a complete walkthrough of Exercise 1.1, including the required deliverables and practical solutions for common setup challenges. The exercise focuses on establishing a Python development environment with proper dependency management and reproducible workflows.

---

## Table of Contents

- [Learning Objectives](#learning-objectives)
- [Environment Specifications](#environment-specifications)
- [Project Structure](#project-structure)
- [Installation Guide](#installation-guide)
- [Technical Notes](#technical-notes)
- [Deliverables](#deliverables)
- [AI Assistance Declaration](#ai-assistance-declaration)
- [Resources](#resources)

---

## Learning Objectives

- Install and verify Python 3.8.x or 3.9.x
- Create isolated virtual environments for project-specific dependencies
- Implement basic Python scripting
- Utilize IPython for interactive development
- Generate requirements files for environment reproducibility
- Establish version control workflows with Git and GitHub

---

## Environment Specifications

**Operating System:** Windows 10/11  
**Shell:** Git Bash (MINGW64)  
**Python Version:** 3.9.x  
**Text Editor:** Visual Studio Code  
**Version Control:** Git + GitHub

### Note on Course Materials

The course materials reference **Python 3.8.7** and **virtualenvwrapper-win**. While these tools remain functional, this guide uses the built-in `venv` module, which provides equivalent functionality with broader compatibility across platforms and shells. Both approaches satisfy the exercise requirements.

---

## Project Structure

```
Exercise-1.1/
│
├── README.md                    # Documentation
├── add.py                       # Addition script
├── requirements.txt             # Package dependencies
├── LEARNING_JOURNAL.md          # Learning reflections
│
└── screenshots/
    ├── 01-python-version.png
    ├── 02-folder-setup.png
    ├── 03-env-created.png
    ├── 04-script-running.png
    ├── 05-ipython-installed.png
    ├── 06-env-copied.png
    └── 07-github-upload.png
```

---

## Installation Guide

### Step 1: Verify Python Installation

```bash
# Check available Python versions
py -0p

# Verify specific version
py -3.9 --version
```

**Expected output:** `Python 3.9.x`

**Screenshot:** 01-python-version.png

---

### Step 2: Set Up Project Directory

```bash
# Navigate to project folder
cd ~/Documents/careerfoundry/PYTHON_COURSE/Exercise\ 1.1

# Verify location
pwd
ls -la
```

**Screenshot:** 02-folder-setup.png

---

### Step 3: Create Virtual Environment

```bash
# Create environment using venv module
py -3.9 -m venv cf-python-base

# Activate environment
source cf-python-base/Scripts/activate

# Verify Python version within environment
python --version
```

The terminal prompt should display `(cf-python-base)` prefix.

**Screenshot:** 03-env-created.png

---

### Step 4: Install IPython

```bash
# Update pip
python -m pip install --upgrade pip

# Install IPython
pip install ipython

# Verify installation
ipython --version
```

---

### Step 5: Create add.py Script

Create file `add.py` with the following content:

```python
# add.py - Simple addition script for Exercise 1.1

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = a + b

print(f"The sum of {a} and {b} is: {c}")
```

Execute the script:

```bash
python add.py
```

**Screenshot:** 04-script-running.png

---

### Step 6: Generate Requirements File

```bash
# Export package list
pip freeze > requirements.txt

# View contents
cat requirements.txt
```

**Note:** The `>` operator is shell redirection syntax (not part of the pip command). It directs output to the specified file.

**Screenshot:** 05-ipython-installed.png

---

### Step 7: Test Environment Reproducibility

```bash
# Deactivate current environment
deactivate

# Create second environment
py -3.9 -m venv cf-python-copy

# Activate new environment
source cf-python-copy/Scripts/activate

# Install dependencies from requirements file
python -m pip install --upgrade pip
pip install -r requirements.txt

# Verify IPython installation
ipython --version
```

**Screenshot:** 06-env-copied.png

---

### Step 8: Version Control

```bash
git add .
git commit -m "Exercise 1.1: Python environment setup and deliverables"
git push
```

**Screenshot:** 07-github-upload.png (GitHub repository page)

---

## Technical Notes

### Command Variations

Different systems and shells may require different Python commands:

- **Windows with Python Launcher:** `py -3.9`
- **macOS/Linux:** `python3` or `python3.9`
- **Within virtual environment:** `python` (references environment interpreter)

**Recommendation:** Test your system's command early and use consistently.

---

### Virtual Environment Tools

**venv (built-in module):**

- Create: `python -m venv <name>`
- Activate (Git Bash): `source <name>/Scripts/activate`
- Activate (Command Prompt): `<name>\Scripts\activate.bat`
- Deactivate: `deactivate`

**virtualenvwrapper-win (alternative):**

- Install: `pip install virtualenvwrapper-win`
- Create: `mkvirtualenv <name>`
- Activate: `workon <name>`
- Deactivate: `deactivate`

**Note:** virtualenvwrapper-win requires Windows Command Prompt (not compatible with PowerShell or Git Bash).

---

### File Path Handling

In Git Bash, escape spaces in directory paths:

```bash
# Option 1: Backslash escaping
cd ~/Documents/My\ Project/Python\ Course

# Option 2: Quotes
cd "~/Documents/My Project/Python Course"
```

---

### pip Command Clarification

The requirements file generation command:

```bash
pip freeze > requirements.txt
```

The course materials occasionally format this as `> pip freeze > requirements.txt`, which includes an extra `>` symbol. The correct syntax uses a single `>` operator for output redirection.

---

## Deliverables

- ✅ Python 3.8.x or 3.9.x verified installation
- ✅ Virtual environment `cf-python-base` created and activated
- ✅ `add.py` script functional
- ✅ IPython installed and operational
- ✅ `requirements.txt` generated
- ✅ Second environment `cf-python-copy` created with dependencies installed
- ✅ GitHub repository with organized folder structure
- ✅ Comprehensive documentation (this README)
- ✅ Process screenshots
- ✅ Learning journal

---

## AI Assistance Declaration

This exercise was completed through independent, self-directed learning. AI assistance was utilized to resolve technical challenges related to:

### Technical Problem-Solving
- **Version compatibility:** Adapting Python 3.8.7-specific course instructions for Python 3.9.x environments
- **Tool alternatives:** Understanding current best practices when course materials referenced deprecated tools (virtualenvwrapper vs venv)
- **Shell-specific syntax:** Translating Command Prompt commands to Git Bash equivalents for Windows development
- **Command clarification:** Resolving syntax ambiguities in course materials (e.g., pip freeze redirection)
- **Environment configuration:** Troubleshooting PATH and activation issues specific to different shell environments

### Learning Context
This exercise was completed independently while working asynchronously through the course. AI tools served as a technical reference for modernizing course instructions to current Python standards, similar to consulting documentation or developer forums when encountering version-specific issues.

### Implementation Approach
All commands were executed manually and errors were debugged hands-on. AI assistance provided guidance on current best practices when course materials referenced older tools or syntax, but all solutions were implemented and validated directly. This approach ensured hands-on learning while maintaining compatibility with current Python ecosystem standards.

---

## Resources

### Documentation

- [Python 3.9 Official Documentation](https://docs.python.org/3.9/)
- [venv Module Reference](https://docs.python.org/3/library/venv.html)
- [pip User Guide](https://pip.pypa.io/en/stable/user_guide/)
- [IPython Documentation](https://ipython.readthedocs.io/)

### Development Tools

- [Visual Studio Code](https://code.visualstudio.com/)
- [Git for Windows](https://gitforwindows.org/)
- [Python Package Index (PyPI)](https://pypi.org/)

---

## Summary

This exercise established foundational Python development practices: environment isolation, dependency management, and reproducible workflows. The technical skills developed here—troubleshooting version conflicts, adapting instructions to different systems, and documenting solutions—are essential for professional software development.

---

**Repository:** [GitHub Link]  
**Contact:** Ivan Cortes  
**Next:** Exercise 1.2

---

*Documentation prepared to assist future learners working through similar environment setup challenges.*
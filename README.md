[![CodeQL](https://github.com/tarekmulla/HaX/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/tarekmulla/HaX/actions/workflows/github-code-scanning/codeql) [![Snyk Security](https://github.com/tarekmulla/HaX/actions/workflows/snyk-security.yml/badge.svg)](https://github.com/tarekmulla/HaX/actions/workflows/snyk-security.yml)

# HaX Tool

HaX is an AI-powered Cybersecurity tool designed to detect website vulnerabilities. Its cloud connection enhances capabilities for advanced analytics and modeling.

<p align="center">
  <img src="/docs/images/HaX.png" alt="design" width="40%"/>
</p>


## About the project

This tool is expertly designed for ethical hacking, using intelligent cyber attack simulations to identify successful outcomes. It uploads results to the cloud for advanced data analytics, refining models for future attacks.

The implemented attacks are:

- CrossSite Scripting (XSS)
- SQL injection (SQLi)


## 🧰 Tech stack

The application uses the following technology and tools.
| Technology / Tool | Purpose |
| ----------- | ----------- |
| [Python](https://www.python.org/) |  Build the atcual application |
| [TKinter](https://docs.python.org/3/library/tkinter.html) | Python package (“Tk interface”) to build the GUI interface |
| [Github actions](https://github.com/features/actions) | Automation pipelines |
| [Snyk](https://snyk.io/) | Security check ([SAST](https://snyk.io/learn/application-security/static-application-security-testing/) analysis, and [SCA](https://snyk.io/series/open-source-security/software-composition-analysis-sca/) analysis) |
| [CodeQL](https://codeql.github.com/) | Discover vulnerabilities across the codebase |
| [Dependabot](https://github.com/dependabot) | Send alert when the repository is using a dependency with a known vulnerability |
| [flake8](https://flake8.pycqa.org/) | Python linting tool |
| [mypy](https://mypy-lang.org/) | Python static type checker |
| [isort](https://pycqa.github.io/isort/) | modules import organizer |
| [pylint](https://pylint.readthedocs.io/en/latest/) | Python static code analyser |

## How do I get set up?

Feel free to clone the repository and create your own version of the application. However, kindly note that the source code is licensed under the `GPL-3.0 license`. To learn more about the license and its terms, please refer to the complete license documentation available [here](./LICENSE).


### Deployment prerequisites

Before running the application, make sure to meet the following requirements:
_**Note**: Those steps are working for both macOS, and Linux_

- Download and install python latest version, [check here](https://www.python.org/downloads/).
- Install pip, [check here](https://pip.pypa.io/en/stable/installation/).
- Install TKinter `brew install python-tk` or `make install-tk`. _**Note**: You need to have brew installed_.
- Set up a Python Virtual Environment (venv) by executing `make create-env` and then switch to the newly created venv using the command: `source ./.venv/bin/activate`. It's worth noting that the `make` command automatically installs the necessary libraries listed in [requirements.txt](./requirements.txt). If you prefer using your local environment instead of venv, you can achieve the same by running `python -m pip install -r requirements.txt` to install the required libraries.
- The entry point is [./hax/main.py](./hax/main.py), You can start the application by running `make run` or `python3 ./hax/main.py`.


## Who do I talk to?

You can contact Tarek Mulla directly using one of the following:
* 👔 Linkedin: [Tarek Mulla](https://www.linkedin.com/in/tarekmulla/)
* ✉️ Personal Email [tarek@mulla.au](mailto:tarek@mulla.au)
* 📇 Contact form [mulla.au](https://mulla.au)

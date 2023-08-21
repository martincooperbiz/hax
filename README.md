[![CodeQL](https://github.com/tarekmulla/HaX/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/tarekmulla/HaX/actions/workflows/github-code-scanning/codeql) [![Snyk Security](https://github.com/tarekmulla/HaX/actions/workflows/snyk-security.yml/badge.svg)](https://github.com/tarekmulla/HaX/actions/workflows/snyk-security.yml)

# HaX Tool
Tool to perform different cyber attacks

## About the project
This tool is designed for practicing ethical hacking by simulating various cyber attacks.

The implemented attacks are:

- CrossSite Scripting (XSS)


## 🧰 Tech stack ##
The application uses the following technology and tools.
| Technology / Tool | Purpose |
| ----------- | ----------- |
| [Python](https://www.python.org/) |  Build the atcual application |
| [TKinter](https://docs.python.org/3/library/tkinter.html) | Python package (“Tk interface”) to build the GUI interface |
| [Github actions](https://github.com/features/actions) | Automation pipelines |
| [Snyk](https://snyk.io/) | Security check ([SAST](https://snyk.io/learn/application-security/static-application-security-testing/) analysis, and [SCA](https://snyk.io/series/open-source-security/software-composition-analysis-sca/) analysis) |
| [CodeQL](https://codeql.github.com/) | Discover vulnerabilities across the codebase |
| [Dependabot](https://github.com/dependabot) | Send alert when the repository is using a dependency with a known vulnerability |


## How do I get set up? ##
Feel free to clone the repository and create your own version of the application. However, kindly note that the source code is licensed under the `GPL-3.0 license`. To learn more about the license and its terms, please refer to the complete license documentation available [here](./LICENSE).


### Deployment prerequisites ###

Before running the application, make sure to meet the following requirements:

- Download and install python latest version, [check here.](https://www.python.org/downloads/)
- Install pip, [check here.](https://pip.pypa.io/en/stable/installation/)
- Install the required libraries listed in [requirements.txt](./requirements.txt) `python -m pip install -r requirements.txt`
- Install TKinter `brew install python-tk`
- The entry point is [main.py](./app/main.py), You can run the file using Makefile `make run`


## Who do I talk to? ##

You can contact Tarek Mulla directly using one of the following:
* 👔 Linkedin: [Tarek Mulla](https://www.linkedin.com/in/tarekmulla/)
* ✉️ Personal Email [tarek@mulla.au](mailto:tarek@mulla.au)
* 📇 Contact form [mulla.au](https://mulla.au)

![GitHub](https://img.shields.io/github/license/diantonioandrea/CLIbrary)

![PyPI](https://img.shields.io/pypi/v/CLIbrary?label=CLIbrary%20on%20pypi)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/CLIbrary)
![PyPI - Downloads](https://img.shields.io/pypi/dm/CLIbrary)

![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/diantonioandrea/CLIbrary)
![GitHub last commit](https://img.shields.io/github/last-commit/diantonioandrea/CLIbrary)
![GitHub Release Date](https://img.shields.io/github/release-date/diantonioandrea/CLIbrary)

![GitHub commits since latest release (by date)](https://img.shields.io/github/commits-since/diantonioandrea/CLIbrary/latest)

# CLIbrary

A comprehensive Python library of standard CLI utilities for convenient command, I/O, and file handling.  

**CLIbrary** is a comprehensive Python library that makes command line usage, input/output, and file handling easier and more efficient. *It provides a wide range of tools for interacting with a shell*, including essential utilities for *command line parsing and I/O, file manipulations, tab completion, and command hinting*. With these tools, **CLIbrary** makes it easy to integrate powerful command-line functionality into any Python project.  
Additionally, it now also provides a *history feature for tracking and re-executing previous commands*.  

Make sure to take a look at the [documentation](https://github.com/diantonioandrea/CLIbrary/blob/main/docs/docs.md), at the [contributing guidelines](https://github.com/diantonioandrea/.github/blob/main/CONTRIBUTING.md) and at the [examples](#examples).

## Installation

### Installing CLIbrary

**CLIbrary** can be installed from [PyPI](https://pypi.org) by:

	python3 -m pip install --upgrade CLIbrary

### Verify installation

The installation of **CLIbrary** can be verified by:

	python3 -m CLIbrary

which would return something similar to[^1]:

	 ●  CLIbrary v1.7.2 
	A comprehensive Python library of standard CLI utilities for convenient command, I/O, and file handling.
	Developed by Andrea Di Antonio, more on https://github.com/diantonioandrea/CLIbrary
	Documentation on https://github.com/diantonioandrea/CLIbrary/blob/main/docs.md
	Bug tracker on https://github.com/diantonioandrea/CLIbrary/issues

[^1]: Example referring to version 1.7.2

### Importing CLIbrary

**CLIbrary** can be imported by:

	import CLIbrary

## Examples

These are some examples from existing projects[^2].

### Command line interface

An example from [**openTree**](https://github.com/diantonioandrea/openTree)

``` python
import CLIbrary

...

cmdHandler = {"request": "[" + user.name + "@" + name + "]"}
cmdHandler["style"] = Fore.MAGENTA

cmdHandler["helpPath"] = helpPath

...

cmdHandler["allowedCommands"] = ["set", "password", "delete", "new"]

...

command = CLIbrary.cmdIn(cmdHandler)

cmd = command["command"]
sdOpts = command["sdOpts"]
ddOpts = command["ddOpts"]
```

[^2]: "..." indicates missing code.

### Asking for input

Some examples from [**openBriefcase**](https://github.com/diantonioandrea/openBriefcase)

```python
import CLIbrary

...

class account:
	def __init__(self, otherNames: list):
		self.name = CLIbrary.strIn({"request": "Account name", "space": False, "blockedAnswers": otherNames})
		self.start = CLIbrary.numIn({"request": "Starting balance"})

...

class movement:
	def __init__(self, otherCodes: list):
		...

		self.reason = CLIbrary.strIn({"request": "Movement reason", "allowedChars": ["-", "'", ".", ",", ":"]})
		self.amount = CLIbrary.numIn({"request": "Movement amount"})
		self.date = CLIbrary.dateIn({"request": "Movement date"})

		...

		self.confirmation = CLIbrary.boolIn({"request": "Verify \"" + str(self) + "\""})
```

### Loading and dumping a file

An example from [**openTree**](https://github.com/diantonioandrea/openTree)

``` python
import CLIbrary

...

user = openTree.user()

fileHandler = {"path": dataPath + user.name, "ignoreMissing": True}
userData = CLIbrary.aLoad(fileHandler)

...

fileHandler["data"] = user
CLIbrary.aDump(fileHandler)
```

### Set values for global settings

An example from [**openTree**](https://github.com/diantonioandrea/openTree)

``` python
import CLIbrary

...

CLIbrary.data.setting_fileExtension = ".ot"

...

if userData.darkTheme:
	CLIbrary.style.setting_darkMode = True
```

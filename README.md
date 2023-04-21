# CLIbrary

A comprehensive Python library of standard CLI utilities for convenient command, I/O, and file handling.  
Make sure to take a look at the [documentation](https://github.com/diantonioandrea/CLIbrary/blob/main/docs/docs.md) and at the [contributing guidelines](https://github.com/diantonioandrea/CLIbrary/blob/main/.github/CONTRIBUTING.md).

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

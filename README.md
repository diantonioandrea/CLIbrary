# CLIbrary

A standardized collection of CLI utilities written in Python to handle commands, I/O and files.  
Make sure to take a look at the [documentation](https://github.com/diantonioandrea/CLIbrary/blob/main/docs.md)

## Installation

### Installing CLIbrary

**CLIbrary** can be installed from [PyPI](https://pypi.org) by:

	python3 -m pip install --upgrade CLIbrary

### Verify installation

The installation of **CLIbrary** can be verified by:

	python3 -m CLIbrary

which would return something similar to:

	 ●  CLIbrary v1.7.0 
	A standardized collection of CLI utilities written in Python to handle commands, I/O and files.
	Developed by Andrea Di Antonio, more on https://github.com/diantonioandrea/CLIbrary

### Importing CLIbrary

**CLIbrary** can be imported by:

	import CLIbrary

## Examples

These are some examples from existing projects[^1].

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

[^1]: "..." indicates missing code.

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

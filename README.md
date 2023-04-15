# CLIbrary

A standardized collection of CLI utilities written in Python to handle commands, I/O and files.  
Make sure to take a look at the [documentation](https://github.com/diantonioandrea/CLIbrary/blob/main/docs.md)

## Usage

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

### Command line interface

An example from [**openTree**](https://github.com/diantonioandrea/openTree)

	# Prompt.
	cmdHandler = {"request": "[" + user.name + "@" + name + "]"}
	cmdHandler["style"] = Fore.MAGENTA

	# The help that gets printed and the commands depend on the environment.
	cmdHandler["helpPath"] = helpPath

	...

	cmdHandler["allowedCommands"] = ["set", "password", "delete", "new"]

	if len(tree):
		cmdHandler["allowedCommands"] += ["list", "details", "edit", "remove"]

	if len(tree) > 1:
		cmdHandler["allowedCommands"] += ["connect", "disconnect"]

	command = CLIbrary.cmdIn(cmdHandler)

	cmd = command["command"]
	sdOpts = command["sdOpts"]
	ddOpts = command["ddOpts"]

### Loading and dumping a file

An example from [**openTree**](https://github.com/diantonioandrea/openTree)

	user = openTree.user()

	fileHandler = {"path": dataPath + user.name, "ignoreMissing": True}
	userData = CLIbrary.aLoad(fileHandler)

	...

	fileHandler["data"] = user
	CLIbrary.aDump(fileHandler)

### Set values for global settings

An example from [**openTree**](https://github.com/diantonioandrea/openTree)

	CLIbrary.data.setting_fileExtension = ".ot"
	CLIbrary.style.setting_darkMode = True
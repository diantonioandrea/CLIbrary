# CLIbrary

A standardized collection of CLI utilities written in Python to handle commands, I/O and files.  
Make sure to take a look at the [documentation](https://github.com/diantonioandrea/CLIbrary/blob/main/docs.md)

## Usage

### Installing CLIbrary

**CLIbrary** can be installed from [PyPI](https://pypi.org) by:

	python3 -m pip install --upgrade CLIbrary

### Importing CLIbrary

**CLIbrary** can be imported by:

	import CLIbrary

## Examples

### Entering commands with options

Code:

	import CLIbrary

	commandHandler = {"request": "Command", "allowedCommands": ["sample"]}
	command = CLIbrary.cmdIn(commandHandler)
	print(command)

Output:

	Command: sample -option1 value --option2
	{'command': 'sample', 'sdOpts': {'option1': 'value'}, 'ddOpts': ['option2']}
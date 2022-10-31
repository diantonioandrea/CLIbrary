# CLIbrary

A standardized collection of CLI utilities written in Python to handle commands, I/O and files.

## Usage

### Adding CLIbrary to a project

CLIbrary can added as a git submodule by:

	git submodule add https://github.com/diantonioandrea/CLIbrary

and updated by:

	git submodule update

or by directly cloning it:

	git clone https://github.com/diantonioandrea/CLIbrary

### Using CLIbrary

CLIbrary can be normally imported by:

	import CLIbrary

and its functions can be used as, for example:

	stringHandler = {}
	stringHandler["request"] = "Input a string"
	stringHandler["allowedChars"] = [",", "!"]
	stringHandler = CLIbrary.strIn(stringHandler)
	print(stringHandler["answer"])

which would result in:

	Input a string: hello, world!
	hello, world!

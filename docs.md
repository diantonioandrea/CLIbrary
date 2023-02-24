# CLIbrary's documentation

## Introduction

### CLIbrary

CLIbrary is *a standardized collection of CLI utilities written in Python to handle commands, I/O and files*. This means it is a set of functions that simplifies writing programs based on it by providing a coherent environment.

CLIbrary provides functions to:
1. Manage a CLI interface through command-and-options handling.
2. Easily access to the program's *help*.
3. Seamlessly load and dump informations to files.
4. Handle various type of inputs without having to worry about consistency and errors.
5. Output different type of informations such as errors and warnings.

CLIbrary is written in Python and developed by [Andrea Di Antonio](https://github.com/diantonioandrea).

### Handlers

Handlers play an important role inside CLIbrary.  
Every function accepts only a handler which is a dictionary structured as {"option": value}.

## Interface

### CLI

	def cmdIn(commandHandler={}) -> dict

*cmdIn* stands for *Command Input* as this function allows the user to input command as in a CLI interface.

The handler for this function makes use of the following parameters:
* request, str: The prompt to the user.
* addedChars, str: A set of characters to be automatically added to the prompt. Default is ": ".
* style, str[^1]: A particular colour style to be applied to the prompt.
* verbose, bool.
* allowedCommands, list: A list of all the allowed commands for the CLI interface.
* helpPath, str: The path to the help JSON. This enables the *help* command.

This function returns a dictionary with the following keys:
* command, str: The command.
* sdOpts, dict: A dictionary containing single-dash options as {"opts1": "value1", "opts2": "value2", ...}[^2].
* ddOpts, list: A list containing double-dash options as [opts1, opts2, ...].

Commands are always structured as:

	command -sdOpt value --ddOpt

with no more than a single word for the command itself.

[^1]: Colorama styling works best for this.

[^2]: The options get returned without the dash.

### Help

	def helpPrint(handler={}) -> None

*helpPrint* is a function that reads and print the help JSON whose path gets passed to *cmdIn*.

A help entry must be formatted this way:

	"command": {
			"description": "Command description.",
			"options": {"-sdOpt#": "VALUE", "-sdOpt": "VALUE", "--ddOpt": ""}
		}

where mandatory options get identified by a "#" and double-dash options don't require a value description.  
There is no need to call this function manually as its operation is embedded inside *cmdIn*.

## Files

CLIbrary provides two functions to handle files loading and dumping: *aLoad* and *aDump*. These functions make a great use of the Python module Pickle.

### Loading

	def aLoad(fileHandler: dict)

*aLoad* stands for *Automatic Loading* as this function loads informations from files without user confirmation.

The handler for this function makes use of the following parameters:
* path, str: The path to the file.
* ignoreMissing, bool: Whether to display an error on missing files.

### Dumping

	def aDump(fileHandler: dict) -> None

*aDump* stands for *Automatic Dumping* as this function dumps informations to files without user confirmation.

The handler for this function makes use of the following parameters:
* path, str: The path to the file.
* data: The data to be dumped.

## Inputs

### Strings

	def strIn(stringHandler={}) -> str

*strIn* stands for *String Input* as this function's purpose is used to receive string inputs.

The handler for this function makes use of the following parameters:
* request, str: The prompt to the user.
* addedChars, str: A set of characters to be automatically added to the prompt.
* allowedChars, list: The set of allowed characters which aren't letters.
* allowedAnswers, list: The list of the only allowed answers, if not empty.
* allowedStyle, str: The style of the *allowedAnswers* hint.
* blockedAnswers, list: The list of the blocked answers.
* noSpace, bool: Whether to allow or not the use of spaces.
* fixedLength, int: The length of the accepted answer, if different from zero.
* verification, bool: Whether to ask for an answer verification. Useful for passwords.
* verbose, bool.

### Numbers

### Booleans

### Dates

### List handling

## Outputs
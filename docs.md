# CLIbrary's documentation

## Table of Contents

1. [Introduction](#introduction)
	1. [CLIbrary](#clibrary)
	2. [Handlers](#handlers)
	3. [Settings](#settings)
	4. [Import CLIbrary](#import-clibrary)
2. [Interface](#interface)
	1. [CLI](#cli)
	2. [Help](#help)
	3. [Help entries](#help-entries)
3. [Files](#files)
	1. [Loading](#loading)
	2. [Dumping](#dumping)
4. [Inputs](#inputs)
	1. [Strings](#strings)
	2. [Numbers](#numbers)
	3. [Booleans](#booleans)
	4. [Dates](#dates)
	5. [List handling](#list-handling)
5. [Outputs](#outputs)
	1. [Output function](#output-function)

## Introduction

### CLIbrary

**CLIbrary** is *a standardized collection of CLI utilities written in Python to handle commands, I/O and files*. This means it is a set of functions that simplifies writing programs based on it by providing a coherent environment.

**CLIbrary** provides functions to:
* Manage a CLI interface through command-and-options handling.
* Easily access to the program's *help*.
* Seamlessly load and dump informations to files.
* Handle various type of inputs without having to worry about consistency and errors.
* Output different type of informations such as errors and warnings.

**CLIbrary** is written in Python and developed by [Andrea Di Antonio](https://github.com/diantonioandrea).

### Handlers

Handlers play an important role inside **CLIbrary**.
Every function accepts only a handler which is a dictionary structured as {"option": value}.

Note that, although every function has a default handler, it is recommended to provide at least some options to achieve a better user experience.

### Settings

As of version 1.2.1, CLIbrary has some "global options" to allow even more personalization.  
Available options are:

1. CLIbrary.style.setting_darkMode, bool: Enables dark mode.

### Import CLIbrary

**CLIbrary** can be imported by:

	import CLIbrary

and all the functions can be accessed by:

	CLIbrary.FUNCTION()

## Interface

[Go back to ToC](#table-of-contents)

### CLI

	CLIbrary.cmdIn(commandHandler={}) -> dict

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

[^1]: Colorama styling works best for styling inside **CLIbrary**.

[^2]: The options get returned without the dash.

### Help

	CLIbrary.helpPrint(handler={}) -> None

*helpPrint* is a function that reads and print the help JSON whose path gets passed to *cmdIn*.
This function cannot be called manually as its calls are embedded inside *cmdIn*.

### Help entries

A help entry must be formatted this way:

	"command": {
		"description": "Command description.",
		"options": {"-sdOpt#": "VALUE", "-sdOpt": "VALUE", "--ddOpt": ""}
	}

where mandatory options get identified by a "#" and double-dash options don't require a value description.

## Files

[Go back to ToC](#table-of-contents)

**CLIbrary** provides two functions to handle files loading and dumping: *aLoad* and *aDump*. These functions make a great use of the Python module Pickle.

### Loading

	CLIbrary.aLoad(fileHandler: dict)

*aLoad* stands for *Automatic Loading* as this function loads informations from files without user confirmation.

The handler for this function makes use of the following parameters:
* path, str: The path to the file.
* ignoreMissing, bool: Whether to display an error on missing files.

### Dumping

	CLIbrary.aDump(fileHandler: dict) -> None

*aDump* stands for *Automatic Dumping* as this function dumps informations to files without user confirmation.

The handler for this function makes use of the following parameters:
* path, str: The path to the file.
* data: The data to be dumped.

## Inputs

[Go back to ToC](#table-of-contents)

### Strings

	CLIbrary.strIn(stringHandler={}) -> str

*strIn* stands for *String Input* as this function's purpose is receiving string inputs.

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

The returned value isn't case sensitive.

### Numbers

	CLIbrary.numIn(numberHandler={}) -> "int, float"

*numIn* stands for *Number Input* as this function's purpose is receiving numeric inputs.

The handler for this function makes use of the following parameters:
* request, str: The prompt to the user.
* addedChars, str: A set of characters to be automatically added to the prompt.
* allowedRange, list: The range in which the function accepts an answer, if not empty.
* allowedTypes, list: Whether to accept just integer or integer and floats.
* round, int: The number of decimal to round to, if different from -1.
* noSpace, bool: Whether to allow or not the use of spaces.
* verbose, bool.

### Booleans

	CLIbrary.boolIn(boolHandler={}) -> bool

*boolIn* stands for *Boolean Input* as this function's purpose is receiving boolean inputs.

The handler for this function makes use of the following parameters:
* request, str: The prompt to the user.
* addedChars, str: A set of characters to be automatically added to the prompt.
* verbose, bool.

### Dates

	CLIbrary.dateIn(dateHandler={}) -> str

*dateIn* stands for *Date Input* as this function's purpose is receiving date inputs.

The handler for this function makes use of the following parameters:
* request, str: The prompt to the user.
* addedChars, str: A set of characters to be automatically added to the prompt.
* verbose, bool.

### List handling

	CLIbrary.listCh(listHandler={})

*listCh* stands for *List Choice* as this function returns the choosen element from a list.

The handler for this function makes use of the following parameters:
* list, list: The list from which the element gets choosen.
* request, str: The prompt to the user.

## Outputs

### Output function

[Go back to ToC](#table-of-contents)

	CLIbrary.output(outputHandler: dict) -> None

The handler for this function makes use of the following parameters:
* string, str: The output string.
* type, str: The output type, to be choosen from:
	* "error",
	* "warning",
	* "verbose",
	* "custom": Lets you define a custom output style.
* customStyle, str.
* before, str: A string that gets printed before the output and is unaffected by the output styling.
* after, str: A string that gets printed after the output and is unaffected by the output styling.
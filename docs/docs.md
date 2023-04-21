# CLIbrary's documentation

## Projects built with CLIbrary

These projects have been built with **CLIbrary** and they should serve as examples for future **CLIbrary** projects.

* [**openBriefcase**](https://github.com/diantonioandrea/openBriefcase), by [Andrea Di Antonio](https://github.com/diantonioandrea).
* [**openTree**](https://github.com/diantonioandrea/openTree), by [Andrea Di Antonio](https://github.com/diantonioandrea).
* [**NBody**](https://github.com/diantonioandrea/NBody), by [Andrea Di Antonio](https://github.com/diantonioandrea).

<a href="mailto:mail@diantonioandrea.com?subject=CLIbrary's project">Let me know<a> should you want your project listed here.

## Table of Contents

0. [Projects built with CLIbrary](#projects-built-with-clibrary)
1. [Introduction](#introduction)
	1. [CLIbrary](#clibrary)
	2. [Handlers](#handlers)
	3. [Settings](#settings)
	4. [Import CLIbrary](#import-clibrary)
2. [Interface](#interface)
	1. [CLI](#cli)
	2. [Option parser](#option-parser)
	3. [Help](#help)
	4. [Help entries](#help-entries)
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

**CLIbrary** is *a comprehensive Python library of standard CLI utilities for convenient command, I/O, and file handling*. This means it is a set of functions that simplifies writing programs based on it by providing a coherent environment.

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

1. `CLIbrary.style.setting_darkMode`, bool: Enables global dark mode. Dafault: `False`.
2. `CLIbrary.style.setting_plainMode`, bool: Disables styling. Default: `False`.
3. `CLIbrary.input.setting_caseSensitive`, bool: Enables case-sensitiveness. Default: `False`.
4. `CLIbrary.data.setting_fileExtension`, str: Defines a file extension for *CLIbrary.aDump* and *CLIbrary.aLoad*. Default: `".pickle"`

### Import CLIbrary

**CLIbrary** can be installed by:

	python3 -m pip install --upgrade CLIbrary

verified by:

	python3 -m CLIbrary
	
imported by:

``` python
import CLIbrary
```

and all the functions can be accessed by:

``` python
CLIbrary.FUNCTION_NAME()
```

## Interface

[Go back to ToC](#table-of-contents)

### CLI

``` python
CLIbrary.cmdIn(commandHandler={}) -> dict
```

*cmdIn* stands for *Command Input* as this function allows the user to input command as in a CLI interface.

The handler for this function makes use of the following parameters:
* request, str: The prompt to the user.
* added, str: A set of characters to be automatically added to the prompt. Default is ": ".
* style, str[^1]: A particular colour style to be applied to the prompt.
* verbose, bool.
* allowedCommands, list: A list of all the allowed commands for the CLI interface.
* helpPath, str: The path to the help JSON. This enables the *help* command.

This function returns a dictionary with the following keys:
* command, str: The command.
* sdOpts, dict: A dictionary containing single-dash options as {"opts1": "value1", "opts2": "value2", ...}[^2].
* ddOpts, list: A list containing double-dash options as [opts1, opts2, ...][^2].

Commands are always structured as:

	command -sdOpt value --ddOpt

with no more than a single word for the command itself.

[^1]: Colorama styling works best for styling inside **CLIbrary**.

[^2]: The options get returned without the dashes.

### Option parser

``` python
CLIbrary.optionParser(instructions: list) -> None
```

*optionParser* is a function that receives a list of strings and returns the single dash options sdOpts, a dictionary, and the double dash options, a list.

### Help

``` python
CLIbrary.helpPrint(handler={}) -> None
```

*helpPrint* is a function that reads and print the help JSON whose path gets passed to *cmdIn*.
There's no need to call this function manually as its calls are embedded inside *cmdIn*.

### Help entries

A help entry must be formatted this way:

``` json
"command": {
	"description": "Command description.",
	"options": {"-sdOpt#": "VALUE_DESCRIPTION", "-sdOpt": "VALUE_DESCRIPTION", "--ddOpt": ""}
}
```

where mandatory options get identified by a "#" and double-dash options don't require a value description.

This is an example from **openBriefcase**'s accounts help JSON[^3]:

``` json
{
	"exit": {
		"description": "Exits the account environment."
	},
	"new": {
		"description": "Creates a new movement."
	},
	"edit": {
		"description": "Edits a movement's features specifying at least an attribute.",
		"options": {"-q#": "MOVEMENT_QUERY", "--reason": "", "--amount": "", "--date": "", "--category": ""}
	},
	"remove": {
		"description": "Removes a movement.",
		"options": {"-c#": "MOVEMENT_QUERY"}
	},
	"summary": {
		"description": "Prints a summary of the account's movements."
	},
	"load": {
		"description": "Loads a set of movements from a file."
	},
	"dump": {
		"description": "Dumps a set of movements to a file.",
		"options": {"-s": "STARTING_TIME", "-e": "ENDING_TIME"}
	}
}

```

[^3]: This example refers to the version 1.5.0 of openBriefcase. The updated file can be found on [GitHub](https://github.com/diantonioandrea/openBriefcase/blob/main/resources/openBriefcaseAccountHelp.json).

## Files

[Go back to ToC](#table-of-contents)

**CLIbrary** provides two functions to handle files loading and dumping: *aLoad* and *aDump*. These functions make a great use of the Python module Pickle.

### Loading

``` python
CLIbrary.aLoad(fileHandler: dict)
``` 

*aLoad* stands for *Automatic Loading* as this function loads informations from files without user confirmation.

The handler for this function makes use of the following parameters:
* path, str: The path to the file.
* ignoreMissing, bool: Whether to display an error on missing files.

### Dumping

``` python
CLIbrary.aDump(fileHandler: dict) -> None
```

*aDump* stands for *Automatic Dumping* as this function dumps informations to files without user confirmation.

The handler for this function makes use of the following parameters:
* path, str: The path to the file.
* data: The data to be dumped.

## Inputs

[Go back to ToC](#table-of-contents)

### Strings

``` python
CLIbrary.strIn(stringHandler={}) -> str
```

*strIn* stands for *String Input* as this function's purpose is receiving string inputs.

The handler for this function makes use of the following parameters:
* Strings.
	* request: The prompt to the user.
	* added: A set of characters to be automatically added to the prompt.
* Lists.
	* allowedChars: The set of allowed characters which aren't letters.
	* allowedAnswers: The list of the only allowed answers, if not empty.
	* blockedAnswers: The list of the blocked answers.
* Bools.
	* empty: Whether to allow or not empty strings.
	* space: Whether to allow or not the use of spaces.
	* verification: Whether to ask for an answer verification. Useful for passwords.
	* verbose.
* Integers.
	* fixedLength: The length of the accepted answer, if different from zero.

The returned value isn't case sensitive.

### Numbers

``` python
CLIbrary.numIn(numberHandler={}) -> "int, float"
```

*numIn* stands for *Number Input* as this function's purpose is receiving numeric inputs.

The handler for this function makes use of the following parameters:
* Strings.
	* request: The prompt to the user.
	* added: A set of characters to be automatically added to the prompt.
* Strings.
	* allowedRange: The range in which the function accepts an answer, if not empty.
	* allowedTypes: Whether to accept just integer or integer and floats.
* Bools.
	* verbose.
* Integers.
	* round: The number of decimal to round to, if different from -1.

### Booleans

``` python
CLIbrary.boolIn(boolHandler={}) -> bool
```

*boolIn* stands for *Boolean Input* as this function's purpose is receiving boolean inputs.

The handler for this function makes use of the following parameters:
* Strings.
	* request: The prompt to the user.
	* added: A set of characters to be automatically added to the prompt.
* Bools.
	* verbose.

### Dates

``` python
CLIbrary.dateIn(dateHandler={}) -> str
```

*dateIn* stands for *Date Input* as this function's purpose is receiving date[^4] inputs.

The handler for this function makes use of the following parameters:
* Strings.
	* request: The prompt to the user.
	* added: A set of characters to be automatically added to the prompt.
* Bools.
	* placeholders: Enables the use of "x"s as placeholders for not fully known dates.
	* verbose.

[^4]: Dates have to be passed in respect to the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) standard. 

### List handling

``` python
CLIbrary.listCh(listHandler={})
```

*listCh* stands for *List Choice* as this function returns the choosen element from a list.

The handler for this function makes use of the following parameters:
* Strings.
	* request: The prompt to the user.
	* added: A set of characters to be automatically added to the prompt.
* Lists.
	* list: The list from which the element gets choosen.

## Outputs

[Go back to ToC](#table-of-contents)

### Output function

``` python
CLIbrary.output(outputHandler: dict) -> None
```

The handler for this function makes use of the following parameters:
* Strings.
	* string: The output string.
	* type: The output type, to be choosen from:
		* `"error"`,
		* `"warning"`,
		* `"verbose"`,
		* `""`: A plain style, similar to that of `CLIbrary.style.setting_plainMode`.
	* before: A string that gets printed before the output and is unaffected by the output styling.
	* after: A string that gets printed after the output and is unaffected by the output styling.

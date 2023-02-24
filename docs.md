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

## Interface

### CLI

### Help

## Files

CLIbrary provides two functions to handle files loading and dumping: *aLoad* and *aDump*. These functions make a great use of the Python module Pickle.

### Loading

	def aLoad(fileHandler: dict):

*aLoad* stands for *Automatic Loading* as this function loads informations from files without user confirmation.

The handler for this function makes use of the following parameters:
* path: The path to the file.
* ignoreMissing: Whether to display an error on missing files.

### Dumping

	def aDump(fileHandler: dict) -> None:

*aDump* stands for *Automatic Dumping* as this function dumps informations to files without user confirmation.

The handler for this function makes use of the following parameters:
* path: The path to the file.
* data: The data to be dumped. It can be of any type with "pickle" files.

## Inputs

### Strings

### Numbers

### Booleans

### Dates

### List handling

## Outputs
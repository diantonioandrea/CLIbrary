# CLIbrary

import pkg_resources

from .outputs import *

output({"type": "verbose", "string": "CLIbrary v" + pkg_resources.get_distribution("CLIbrary").version})
print("A comprehensive Python library of standard CLI utilities for convenient command, I/O, and file handling.")
print("Developed by " + Style.BRIGHT + Fore.CYAN + "Andrea Di Antonio" + Style.RESET_ALL + ", more on " + Style.BRIGHT + "https://github.com/diantonioandrea/CLIbrary" + Style.RESET_ALL)
print("Documentation on " + Style.BRIGHT + "https://github.com/diantonioandrea/CLIbrary/blob/main/docs/docs.md" + Style.RESET_ALL)
print("Bug tracker on " + Style.BRIGHT + "https://github.com/diantonioandrea/CLIbrary/issues" + Style.RESET_ALL)
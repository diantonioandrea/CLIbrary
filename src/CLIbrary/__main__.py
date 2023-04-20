# CLIbrary

import pkg_resources

from .outputs import *

output({"type": "verbose", "string": "CLIbrary v" + pkg_resources.get_distribution("CLIbrary").version})
print("A standardized collection of CLI utilities written in Python to handle commands, I/O and files.")
print("Developed by " + Style.BRIGHT + Fore.CYAN + "Andrea Di Antonio" + Style.RESET_ALL + ", more on " + Style.BRIGHT + "https://github.com/diantonioandrea/CLIbrary" + Style.RESET_ALL)
print("Documentation on " + Style.BRIGHT + "https://github.com/diantonioandrea/CLIbrary/blob/main/docs.md" + Style.RESET_ALL)
print("Bug tracker on " + Style.BRIGHT + "https://github.com/diantonioandrea/CLIbrary/issues" + Style.RESET_ALL)
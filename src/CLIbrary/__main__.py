from .outputs import *
import pkg_resources

output({"type": "verbose", "string": "CLIbrary v" + pkg_resources.get_distribution("CLIbrary").version})
print("A standardized collection of CLI utilities written in Python to handle commands, I/O and files.")
print("Developed by " + Style.BRIGHT + Fore.MAGENTA + "Andrea Di Antonio" + Style.RESET_ALL + ", more on " + Style.BRIGHT + "https://github.com/diantonioandrea/CLIbrary" + Style.RESET_ALL)
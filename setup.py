from setuptools import setup

setup(
	name="CLIbrary",
	version="0.1",
	author="Andrea Di Antonio",
	url="https://github.com/diantonioandrea/CLIbrary",
	packages=["CLIbrary"],
	description="A standardized collection of CLI utilities written in Python to handle commands, I/O and files.",
	install_requires=["pickle", "colorama"]
)
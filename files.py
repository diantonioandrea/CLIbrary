from pickle import load, dump

# FILES HANDLING

def autoload(filename: str):
	try:
		dataFile = open(filename, "rb")
		data = load(dataFile)
		dataFile.close()
		
		return data
		
	except:
		return None
	
def autodump(filename: str, data) -> None:
	dataFile = open(filename, "wb")
	dump(data, dataFile)
	dataFile.close()
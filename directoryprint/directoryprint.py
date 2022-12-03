import subprocess

class DirectoryPrint:
	def printDirectory(self):
		process = subprocess.Popen(["ls"])
		process.wait()
		print("-----------------------------")
		print("Directory Print Out Complete!")

def main():
	printer = DirectoryPrint()
	printer.printDirectory()

if __name__ == "__main__":
	main()

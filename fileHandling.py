# file handline
# G Allcock
# 02/10/25
# AS Computer Science

# creating a file
def createFile(filePath):
    try:
        file1 = open(filePath, "x")
        print('File created.')
        file1.close
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)

# read information from a file
def readFile(filePath):
    try:
        with open(filePath, "r") as file:
            content = file.read()
        file.close()
        return content
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("Error occurred:", e )

# Execute the main program
def main():
    filePath = "country.txt"
    print(readFile(filePath))
    createFile("town.txt")

if (__name__ == "__main__"):
    main()

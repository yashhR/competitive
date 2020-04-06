fileName = input("File to split: ")                        # Which file to split?
extension = fileName.split('.')[-1]
specificLines = int(input("Specify lines to split by: "))  # How many lines to split by?
count = 0                                                  # Count to keep track of lines written to a file
fileNumber = 1                                             # To name multiple new files
with open(fileName, 'r') as rf:                            # Reading the input file
    for line in rf:                                        # Reading each line
        wf = open(f'file{fileNumber}.{extension}', 'a+')   # Create and write if doesn't exist/ Append if exists
        wf.write(line)                                     # Writing the line
        count += 1                                         # Incrementing the no. of lines written to file
        if count % specificLines == 0:                     # If count is a multiple of specified line,
            fileNumber += 1                                # create a fresh file for rest of the lines

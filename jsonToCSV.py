import json
import sys
import csv

jsonFile = sys.argv[1]

#set up the input file for reading
jsonFileHandle = open(jsonFile, 'r')
rawText = jsonFileHandle.read()
heartParsed = json.loads(rawText)

#set up the output file for writing csv
csvFileName = jsonFile[:-4]
csvFileHandle = open(csvFileName + 'csv', 'w+')
csvWriter = csv.writer(csvFileHandle)

#write the csv header line
csvWriter.writerow(['Date', 'Resting Heart Rate',  'Error'])
for dataPoint in heartParsed:
    # For days without data, Fitbit archive file uses null for date, 0.0 for value and error
    # So, we check for null
    if dataPoint['value']['date'] != None:
        print(dataPoint['value']['date'], dataPoint['value']['value'], dataPoint['value']['error'])
        #write each line to the csv file
        csvWriter.writerow([dataPoint['value']['date'], dataPoint['value']['value'], dataPoint['value']['error']])

#close the files
jsonFileHandle.close();
csvFileHandle.close();
"""
Batch Process - third transformation

Reads from a file, transform, write to a new file.

In this case, covert degree K to degree F.

"""

import csv

input_file_name = "batchfile_2_kelvin.csv" #file created in part b
output_file_name = "batchfile_3_farenheit.csv" #new file name

input_file = open(input_file_name, "r") #reading file from part b
output_file = open(output_file_name, "w", newline='') #writing to new file

reader = csv.reader(input_file, delimiter=",") 
writer = csv.writer(output_file, delimiter=",")

header = next(reader)
header_list = ["Year","Month","Day","Time","TempF"]
writer.writerow(header_list)

for row in reader:
    Year, Month, Day, Time, TempK = row
    TempF = round((float(TempK) - 273.15) * 1.8 + 32) #Googled formula for temperature conversion
    writer.writerow([Year, Month, Day, Time, TempF])

output_file.close()
input_file.close()

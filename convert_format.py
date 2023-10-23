import sys
import json
import csv
import xml.etree.ElementTree as ET

# Ensure proper command line arguments
if len(sys.argv) != 3:
    print("Usage: python convert_format.py <filename> <-c|-j|-x>")
    sys.exit(1) 

input_filename = sys.argv[1]
output_format = sys.argv[2]

# Read data from the input file
with open(input_filename, 'r') as file:
    data = file.read()

# Define a function to convert and save data based on the format
def save_data(data, format):
    if format == "-c":
        with open('output.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Data"])
            writer.writerow([data])
    elif format == "-j":
        with open('output.json', 'w') as jsonfile:
            json.dump({"Data": data}, jsonfile, indent=4)
    elif format == "-x":
        root = ET.Element("data")
        ET.SubElement(root, "value").text = data
        tree = ET.ElementTree(root)
        tree.write("output.xml")

save_data(data, output_format)

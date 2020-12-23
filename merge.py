import fileinput
import glob
import json

# -------------------------------------------------------------------------------------------------------------------------
# Combines all JSON files in a given directory into one file.
# Author: Tyler Skow 
# -------------------------------------------------------------------------------------------------------------------------


file_list = glob.glob("*.json")


with open('all_data3.txt', 'w') as file:

    for link in file_list:

        file_temp = open(link)
        for line in file_temp:
            try:
                json_line = json.loads(line)
                json.dump(json_line, file)
                file.write('\n')
            except Exception as e:
                print(e)

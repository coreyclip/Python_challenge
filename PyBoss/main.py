"""
In this challenge, you get to be the boss. 
You oversee hundreds of employees across the country developing Tuna 2.0, 
a world-changing snack food based on canned tuna fish. 
Alas, being the boss isn't all fun, games, and self-adulation. 
The company recently decided to purchase a new HR system, and unfortunately for you, 
the new system requires employee records be stored completely differently.
Your task is to help bridge the gap by creating a Python script able to 
convert your employee records to the required format. Your script will need to do the following:

	* Import the employee_data1.csv and employee_data2.csv files,
    which currently holds employee records like the below:

Emp ID,Name,DOB,SSN,State
214,Sarah Simpson,1985-12-04,282-01-8166,Florida
15,Samantha Lara,1993-09-08,848-80-7526,Colorado
411,Stacy Charles,1957-12-20,658-75-8526,Pennsylvania

	* Then convert and export the data to use the following format instead:

Emp ID,First Name,Last Name,DOB,SSN,State
214,Sarah,Simpson,12/04/1985,***-**-8166,FL
15,Samantha,Lara,09/08/1993,***-**-7526,CO
411,Stacy,Charles,12/20/1957,***-**-8526,PA

	* In summary, the required conversions are as follows:
		* [ ]The Name column should be split into separate First Name and Last Name columns.
		* [ ]The DOB data should be re-written into DD/MM/YYYY format.
		* [ ]The SSN data should be re-written such that the first five numbers are hidden from view.
		* [ ]The State data should be re-written as simple two-letter abbreviations.


"""

import os
import csv
from datetime import datetime


path1 = os.path.join('employee_data1.csv')
path2 = os.path.join('employee_data2.csv')

pathlist = [path1, path2]

new_records = { }

for path in pathlist:
    with open(path) as file:
        reader = csv.DictReader(file)
        indexer = 0
        for row in reader:
            #split first and last name
            first_name = row['Name'].split(' ')[0]
            last_name = row['Name'].split(' ')[1]
            #reformat date
             datetime('1988-11-08').strftime('We are the %d, %b %Y')
            
            new_records[indexer] = {
                                    'Emp ID': row['Emp ID'],
                                    'First Name': first_name,
                                    'Last Name': last_name,
                                    
                                       }
            
            
            
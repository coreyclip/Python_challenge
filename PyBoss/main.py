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
		* [x]The Name column should be split into separate First Name and Last Name columns.
		* [x]The DOB data should be re-written into DD/MM/YYYY format.
		* [x]The SSN data should be re-written such that the first five numbers are hidden from view.
		* [x]The State data should be re-written as simple two-letter abbreviations.


"""

import os
import csv
from datetime import datetime
from dateutil.parser import parse
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

path1 = os.path.join('employee_data1.csv')
path2 = os.path.join('employee_data2.csv')

pathlist = [path1, path2]

new_records = []

for path in pathlist:
    with open(path) as file:
        reader = csv.DictReader(file)
        indexer = 0
        for row in reader:
            #split first and last name
            first_name = row['Name'].split(' ')[0]
            last_name = row['Name'].split(' ')[1]
            #reformat date
            Bday = datetime.strptime(row['DOB'],'%Y-%m-%d').strftime('%d/%m/%Y')
            #hide first five number of SSN
            Last4Digits = row["SSN"].split('-')[2]
            hiddenSSN = f"***-**-{Last4Digits}"
            #look up state in us_state_abbrev for abbreviation
            abbrev = us_state_abbrev[row['State']]
            new_records.append({
                                    'Emp ID': row['Emp ID'],
                                    'First Name': first_name,
                                    'Last Name': last_name,
                                    'DOB':Bday,
                                    'SSN':hiddenSSN,
                                    'State': abbrev

                                       })


with open("new_records.csv", 'w') as f:
    # Assuming that all dictionaries in the list have the same keys.
    headers = sorted([k for k, v in new_records[0].items()])
    print("headers: ")
    print(headers)
    csv_data = [headers]

    for record in new_records:
        csv_data.append([record[h] for h in headers])
        #print(csv_data)
    writer = csv.writer(f)
    writer.writerows(csv_data)
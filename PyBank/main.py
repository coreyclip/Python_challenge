"""

Challenge goals:
    Read csv files: budget_data1 and budget_data2 
    and output a report that gives the following 

	* [ ] The total number of months included in the dataset
	* [ ] The total amount of revenue gained over the entire period
	* [ ] The average change in revenue between months over the entire period
	* [ ] The greatest increase in revenue (date and amount) over the 
    entire period
	* [ ] The greatest decrease in revenue (date and amount) over the 
    entire period


"""
import os
import csv

base_path = "C:\\Users\\corey\\Dropbox\\uci\\Homework\\Python_challenge\\PyBank"
path1 = os.path.join(base_path, 'budget_data1.csv')
path2 = os.path.join(base_path, 'budget_data2.csv')



def finstat_gatherer(filepath):
    """[loops through the designated csv file and gathers information
    on the total months and revenue in a csv file while also keeping track of the
    changes in revenue]
    
    Arguments:
        filepath {[string]} -- [the complete file path to the target csv file]
    """
    #create variables for report, to be totaled later
    total_months = 0
    total_revenue = 0
    change_revenue_list = []
    length_counter = 0
    change_revenue_listOfDicts = []
    record_dict = {}
    with open(filepath) as f:
        sheet = csv.DictReader(f)
        for row in sheet:
            print(row['Date'], row['Revenue'])
    #each row is a month so we just incriment the months by one each time we loop through a row
            total_months += 1 
    #since are using an ordered dict we can use the Revenue row value to increment total_revenue
            total_revenue += float(row['Revenue'])
    #dump the rows into a dict
            record_dict[length_counter] = {"Date": row['Date'],
                                           "Revenue":row['Revenue']}
            length_counter += 1

    #gather into a dict all of the monthly changes in revenue
    for index, value in enumerate(record_dict):
        print(value, record_dict[index])
        change = record_dict[index]['Revenue'] - record_dict[index + 1]['Revenue']
      
    print(f"total revenue is now: {total_revenue}")
    print(f"There are {total_months} months in this dataset")
    return total_months, total_revenue, change_revenue_listOfDicts         

finstat_gatherer(path1)
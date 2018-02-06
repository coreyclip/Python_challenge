"""

Challenge goals:
    Read csv files: budget_data1 and budget_data2 
    and output a report that gives the following 

	* [x] The total number of months included in the dataset
	* [x] The total amount of revenue gained over the entire period
	* [ ] The average change in revenue between months over the entire period
	* [ ] The greatest increase in revenue (date and amount) over the 
    entire period
	* [ ] The greatest decrease in revenue (date and amount) over the 
    entire period


"""
import os
import csv


path1 = os.path.join('datafiles', 'budget_data1.csv')
path2 = os.path.join('datafiles', 'budget_data2.csv')



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
                                           "Revenue": int(row['Revenue'])}
            length_counter += 1

    #gather into a dict all of the monthly changes in revenue
    for index, value in enumerate(record_dict):
        print(value, record_dict[index])
        if index + 1 < 86:
            month_revenue = record_dict[index]['Revenue']
            print("month's revenue: " + str(month_revenue))
            next_month_revenue = record_dict[index + 1]['Revenue']
            print("next month's revenue: " + str(next_month_revenue ))
            change = next_month_revenue - month_revenue
            print("change: " + str(change))
            change_revenue_listOfDicts.append({"Date":record_dict[index + 1]['Date'],
                                                "Change in Revenue": change})
        else:
            pass 
    print(f"total revenue for this dataset: {total_revenue}")
    print(f"There are {total_months} months in this dataset")
    return total_months, total_revenue, change_revenue_listOfDicts         

t1, r1, total_changes_list = finstat_gatherer(path1) #make the changes list of the first dataset be the 
# main one, and just append the records of the second one

t2, r2, c2 = finstat_gatherer(path2)

# add the records in c2 to the total_changes_list
for record in c2:
    total_changes_list.append(record)

#calcualte the average change in revenue and find the greatest increase in revenue and decrease
increase = 0
decrease = 0
moving_total = 0
for record in total_changes_list:
    moving_total += record['Change in Revenue']
    if record['Change in Revenue'] > increase:
        greatest_increase_date = {'Date of greatest increase': record['Date'], 
                                    "Change": record["Change in Revenue"]}
    elif record['Change in Revenue'] < decrease: 
        greatest_decrease_date = {'Date of greatest decrease': record['Date'], 
                                    "Change": record["Change in Revenue"]}
    else:
        pass 

average_change = moving_total / len(total_changes_list)

print(f"Over the analyzed time period of {t1 + t2} months \n total revenue is {r1 + r2} \n")
print(f"{greatest_increase_date['Date of greatest increase']} saw the greatest increase in revenue \n")
print(f"with {greatest_increase_date['Change']} increase in revenue")
print(f"{greatest_decrease_date['Date of greatest decrease']} saw the greatest decrease in revenue \n")
print(f"with {greatest_decrease_date['Change']} decrease in revenue")
print(f"the average change in revenue is: {average_change}")

# Data Analysis with Vanilla Python
This repo contains sample scripts and csv files to demonstrate data minining techniques using only 
the libaries included in any basic python install. 

## PyBank
shows a Python script for analyzing financial records. The folder contains two sets of revenue data 
(budget_data_1.csv and budget_data_2.csv). Each dataset is composed of two columns: Date and Revenue. 
The Python script that analyzes the records to calculate each of the following:

	*  The total number of months included in the dataset
	*  The total amount of revenue gained over the entire period
	*  The average change in revenue between months over the entire period
	* The greatest increase in revenue (date and amount) over the entire period
	* The greatest decrease in revenue (date and amount) over the entire period

## PyPoll
This folder contains a script for processing simulated voter rolls for an election in order to output the following

	* The total number of votes cast
	*  A complete list of candidates who received votes
	*  The percentage of votes each candidate won
	*  The total number of votes each candidate won
	*  The winner of the election based on popular vote.

## PyBoss
This folder contains a script for processing employee records for HR purposes. This is much more about processing 
text data than numerical data. 

	* Import the employee_data1.csv and employee_data2.csv files, which currently holds employee records like the below:

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

		* The Name column should be split into separate First Name and Last Name columns.
		* The DOB data should be re-written into DD/MM/YYYY format.
		* The SSN data should be re-written such that the first five numbers are hidden from view.
		* The State data should be re-written as simple two-letter abbreviations.
	* Special Hint: You may find this link to be helpful—Python Dictionary for State Abbreviations.

## PyParagraph
More textual analysis. While seemingly innocuous there are plenty of situations where being able to gather statistics
about a body of text is handy, especially in the field of Natural Language Processing (NLP) 

	* Import a text file filled with a paragraph of your choosing.
	* Assess the passage for each of the following:

		* Approximate word count
		* Approximate sentence count
		* Approximate letter count (per word)
		* Average sentence length (in words)
	* As an example, this passage:

“Adam Wayne, the conqueror, with his face flung back and his mane like a lion's, stood with his great sword point upwards, the red raiment of his office flapping around him like the red wings of an archangel. And the King saw, he knew not how, something new and overwhelming. The great green trees and the great red robes swung together in the wind. The preposterous masquerade, born of his own mockery, towered over him and embraced the world. This was the normal, this was sanity, this was nature, and he himself, with his rationality, and his detachment and his black frock-coat, he was the exception and the accident - a blot of black upon a world of crimson and gold.”
...would yield these results:
Paragraph Analysis
-----------------
Approximate Word Count: 122
Approximate Sentence Count: 5
Average Letter Count: 4.56557377049
Average Sentence Length: 24.4

	
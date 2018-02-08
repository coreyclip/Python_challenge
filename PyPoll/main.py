"""
In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)
You will be given two sets of poll data (election_data_1.csv and election_data_2.csv). Each dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:

    * [x]The total number of votes cast
    * [ ]A complete list of candidates who received votes
    * [ ]The percentage of votes each candidate won
    * [ ]The total number of votes each candidate won
    * [ ]The winner of the election based on popular vote.

As an example, your analysis should look similar to the one below:
Election Results
-------------------------
Total Votes: 620100
-------------------------
Rogers: 36.0% (223236)
Gomez: 54.0% (334854)
Brentwood: 4.0% (24804)
Higgins: 6.0% (37206)
-------------------------
Winner: Gomez
-------------------------
"""
import os
import csv


path1 = os.path.join('datafiles', 'election_data_1.csv')
path2 = os.path.join('datafiles', 'election_data_2.csv')

vote_dict = {}

def polltally(filepath):
    """[summary]
    
    Arguments:
        filepath {[string]} -- [filepath of csv file that contains the poll data]
    """
    indexer = 0
    vote_count = 0
    candidate_list = set()
    with open(filepath) as file:
        reader = csv.DictReader(file)
        for row in reader:
                print(row)
            vote_dict[indexer] = {"id":row[0], "county":row[1], "vote": row[2]}
                indexer += 1
                vote_count += 1
                candidate_list.add(row[2])
        
    return vote_count, candidate_list
            

c1, candlist = polltally(path1)
c2, candlist2 = polltally(path2)

# update candidate list with the candidates from the other dataset
candlist.update(candlist2)

total_votes = c1 + c2
print("total votes: " + str(total_votes))
print()
print("candidates who received votes: ")
for i in candlist:
    print(i)


        


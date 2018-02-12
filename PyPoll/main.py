"""
In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)
You will be given two sets of poll data (election_data_1.csv and election_data_2.csv).
Each dataset is composed of three columns: Voter ID, County, and Candidate. 
Your task is to create a Python script that analyzes the votes and calculates each of the following:

    * [x]The total number of votes cast
    * [x]A complete list of candidates who received votes
    * [x]The percentage of votes each candidate won
    * [x]The total number of votes each candidate won
    * [x]The winner of the election based on popular vote.

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
path_list = [path1, path2]

def polltally(filepath, index_start=0):
    """[loops through a csv file of poll data and places the records
    into a python dict while also tabulating the number of records and a 
    list of candidates who received votes]
    
    Arguments:
        filepath {[string]} -- [filepath of csv file that contains the poll data]
        index_start {[integer]} -- [integer to start index for vote dict]
    """
    vote_dict = {}
    indexer = index_start
    vote_count = 0
    candidate_list = set()
    with open(filepath) as file:
        reader = csv.DictReader(file)
        head = 0
        for row in reader:
            vote_dict[indexer] = {
                                "id":row['Voter ID'],
                                "county":row['County'],
                                "vote": row['Candidate'],
                                        }
            indexer += 1
            vote_count += 1
            candidate_list.add(row['Candidate'])
            while head <= 3:
                print("The first 3 records")
                print("--" * 20)
                print(row)
                head += 1
            else:
                pass
        
    return vote_count, candidate_list, vote_dict


def votetally(candidate_list, vote_dict):
    """[Calculates the total votes for each candidate and prints it out]
    
    Arguments:
            cadidate_list {[list-like]} -- [list of candidates who's votes are being tabulated]
            vote_dict {[dictionary of voting records]}
    Returns:
        tally_dict {[Dictionary]} -- [dict containing {'candidate': votes, ..}]
    """
    tally_dict = {}
    for i in candidate_list:
        vote_count = 0
        for j in vote_dict:
            if vote_dict[j]['vote'] == i:
                vote_count += 1
            else:
                pass
        tally_dict[i] = vote_count
    return tally_dict
   

     
vote_count = 0
candidate_list = set()
final_tally = {}
num_datasets = 0 #counts up how many datasets we have looped through, required for final tally        
for path in path_list:
    count, candlist, voterecord = polltally(path)
    vote_count += count #incriment the total number of votes in all the datasets
    candidate_list.update(candlist)
    tally = votetally(candidate_list, voterecord)
    for key, value in tally.items():
        print(key, value)
        if num_datasets < 1: #for the first dataset simply assign
            final_tally[key] = value
        else:
            final_tally[key] += value
    num_datasets += 1 #incriment the number of datasets
        
        
        #loop through candidate list and call votetally to sum up how many votes
        # each candidate got in each dataset and sum the two totals. 

print("The Final tally from all datasets")
print("*" * 50)
print(final_tally)       
                          

#tabulate the total votes from both datasets
vote_count

#find the winner of the election
top_vote = 0
winner = "none"
for key, value in final_tally.items():
    #print(key, value)
    if value > top_vote:
        winner = key
        top_vote = value
        #print(winner)
    else:
        pass
        

print("=" * 10 + " Election Results " + "=" * 10)
print("total votes: " + str(vote_count))
print("--" *20)
for i in final_tally:
    print(f"{i}: {round(((final_tally[i] / vote_count) * 100), 4)}% ({final_tally[i]})")
print("--" *20)
print(f"The Winner is {winner}")




        


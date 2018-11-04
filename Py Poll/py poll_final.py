import os
import csv
import pandas as pd

data = pd.read_csv("election_data (1).csv")

#Calculate Total Votes
total_votes = data['Voter ID'].count()

Candidates = data['Candidate'].unique()


#Calculate Votes per Candidate
count = data['Candidate'].value_counts()


#Calculate Percentage of Votes per Candidate
per_votes = (count)/(total_votes)*100
per_votes = per_votes.astype(float).map("{:,.2f}%".format)


#Creating Results Dataframe
new_data = pd.DataFrame({"Total Votes" : count, "Percentage Votes" : per_votes})
#Find Winner

winner = data['Candidate'].mode()


#Final Results
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")
print(new_data)
print("-------------------------")
print("Winner: " +str(winner))

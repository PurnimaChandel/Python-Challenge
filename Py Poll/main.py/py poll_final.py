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


new_data = list(zip(Candidates, per_votes, count))

#Find Winner
winner = data['Candidate'].mode()


#Final Results
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")
print(new_data)
print("-------------------------")
print(str(winner))

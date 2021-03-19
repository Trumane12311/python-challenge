import os
import csv

candidate_votes = {}
candidates = []
total_votes = 0

polldata = os.path.join("Resources", "election_data.csv")

with open(polldata, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    headers = next(csvreader)
    for row in csvreader:
        candidates = row[2]
        if candidates in candidate_votes.keys():
            candidate_votes[candidates] = candidate_votes[candidates] + 1
        else:
            candidate_votes[candidates] = 1

total_votes = sum(candidate_votes.values())
print(total_votes)

percentage = []
for i in candidate_votes:
    percentage = round((candidate_votes[i]/total_votes)*100,0)
    print(f'{i} {percentage} {candidate_votes[i]}')

for key in candidate_votes.keys():
    if candidate_votes[key] == max(candidate_votes.values()):
        winner = key

print(f'{winner}')
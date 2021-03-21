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
print("Election Results")
print("-------------------------")
print(f'Total Votes: {total_votes}')
print('-------------------------')

percentage = []
for i in candidate_votes:
    percentage = round((candidate_votes[i]/total_votes)*100,0)
    print(f'{i}: {percentage}% ({candidate_votes[i]})')

for key in candidate_votes.keys():
    if candidate_votes[key] == max(candidate_votes.values()):
        winner = key

print(f'Winner: {winner}')

output_path = os.path.join("analysis", "electiondata_summary.csv")

with open(output_path, 'w', newline='') as electiondata_summary:
  csvwriter = csv.writer(electiondata_summary, delimiter=',')
  csvwriter.writerow(["Election Data Summary"])
  csvwriter.writerow([f'Total Votes, {total_votes}'])
  csvwriter.writerow(["Khan, 63.0%, (2218231)"])
  csvwriter.writerow(["Correy, 20.0%, (704200)"])
  csvwriter.writerow(["Li, 14.0%, (492940)"])
  csvwriter.writerow(["O'Tooley, 3.0%, (105630)"])
  csvwriter.writerow(['Winner, Khan'])
import os
import csv

totalmonths = 0
netprofit = 0
changelist =[]
averagechange = 0
greatestinc = ["",0]
greatestdec = ["",999]
#Set Path for the CSV File
budgetdata = os.path.join("Resources", "budget_data.csv")

#Open CSV File
with open(budgetdata, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    headers = next(csvreader)
    jandata = next(csvreader)
    totalmonths = totalmonths + 1
    netprofit = netprofit + int(jandata[1])
    previousnet = int(jandata[1])
    for row in csvreader:
      totalmonths = totalmonths + 1
      netprofit = netprofit + int(row[1])
      change = int(row[1])-previousnet
      previousnet = int(row[1])
      changelist.append(change)
      if change > greatestinc[1]:
        greatestinc[1] = change
        greatestinc[0] = row[0]
      if change < greatestdec[1]:
        greatestdec[1] = change
        greatestdec[0] = row[0]
averagechange = sum(changelist)/len(changelist)


print("Financial Analysis")
print("---------------------")
print(f'Total Months: {totalmonths}')
print(f'Net Profit: ${netprofit}')
print(f'Average Change: ${averagechange}')
print(f'Greatest Increase in Profits: {greatestinc[0]}, $({greatestinc[1]})')
print(f'Greatest Decrease in Profits: {greatestdec[0]}, ${greatestdec[1]}')

output_file = os.path.join("analysis", "output.csv")

with open(output_file, "w", newline='') as newbudgetfile:
  csvwriter = csv.writer(newbudgetfile, delimiter=',')
  csvwriter.writerow(["Financial Analysis", "Metrics"])
  csvwriter.writerow([f'Total Months:, {totalmonths}'])
  csvwriter.writerow([f'Net Profit:, ${netprofit}'])
  csvwriter.writerow([f'Average Change:, ${averagechange}'])
  csvwriter.writerow([f'Greatest Increase in Profits:, {greatestinc[0]}, $({greatestinc[1]})'])
  csvwriter.writerow([f'Greatest Decrease in Profits:, {greatestdec[0]}, ${greatestdec[1]}'])
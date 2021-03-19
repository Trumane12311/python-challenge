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
print('Total Months: ' + f'{totalmonths}')
print('Net Profit: ' +  f'{netprofit}')
print('Average Change: ' + f'{averagechange}')


print(greatestinc[0],greatestinc[1])
print(greatestdec[0],greatestdec[1])
 
# * The total number of months included in the dataset
# print("Financial Analysis")
# print("---------------------------")

# def sum(numbers):
#     length = len(numbers)
#     monthcount = 0.0
#     for number in numbers:
#         monthcount += number

# #print('Total Months: ') + print(sum(range(1)))

# #The net total amount of "Profit/Losses" over the entire period
# def sumgainloss(numbers):
#     length = len(numbers)
#     net_total = 0.0
#     for number in numbers:
#         net_total += number
# print(f'Net Total: ' + print(sumgainloss(range(2)))

# def average(numbers):
#     length = len(numbers)
#     mean_change = 0.0
#     for number in numbers:
#         mean_change += number
#     return mean_change / length
#   #Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
# print(f'Average Change: ' + '{mean_change}')



# def print_percentages(budgetdata):
#     monthspercent = str(budgetdata[0])
#     lossgain = str(budgetdata[1])

#   #The greatest increase in profits (date and amount) over the entire period
# print(f'Greatest Increase in Profits: ' + '{greatest_inc}')
#   # The greatest decrease in losses (date and amount) over the entire period
# print(f"Greatest Decrease in Losses: " + '{greatest_dec}')

#Save the output file path
# output_file = os.path.join("..","analysis", "output.csv")

# with open(output_file, "w", newline='') as newbudgetfile:
#     csvwriter = csv.writer(newbudgetfile)
#     csvwriter.writerow("Financial Analysis")
#     csvwriter.writerow("-------------------")
#     csvwriter.writerow(f"Total Months:" + "{total_months}")
#     csvwriter.writerow(f"Net Total:" + "{net_total}")
#     csvwriter.writerow(f"Average Change:" + "{mean_change}")
#     csvwriter.writerow(f"Greatest Increase in Profits:" + "{greatest_inc}")
#     csvwriter.writerow(f"Greatest Decrease in Profits:" + "{greatest_dec}")
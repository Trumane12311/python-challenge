import os
import csv
from astropy.table import row

#Set Path for the CSV File
budgetdata = os.path.join('.., Resources, budget_data.csv')

#Open CSV File
with open(budgetdata, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    headers = next(csvreader)
 
# * The total number of months included in the dataset
print("Financial Analysis")
print("---------------------------")

def sum(numbers):
    length = len(numbers)
    monthcount = 0.0
    for number in numbers:
        monthcount += number

print('Total Months: ') + print(sum(range(1)))

#The net total amount of "Profit/Losses" over the entire period
def sum(numbers):
    length = len(numbers)
    net_total = 0.0
    for number in numbers:
        net_total += number
print(f'Net Total: ' + print(sum(range(2)))

def average(numbers):
    length = len(numbers)
    mean_change = 0.0
    for number in numbers:
        mean_change += number
    return mean_change / length
  #Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
print(f'Average Change: ' + '{mean_change}')



def print_percentages(budgetdata):
    monthspercent = str(budgetdata[0])
    lossgain = str(budgetdata[1])

  #The greatest increase in profits (date and amount) over the entire period
print(f'Greatest Increase in Profits: ' + '{greatest_inc}')
  # The greatest decrease in losses (date and amount) over the entire period
print(f"Greatest Decrease in Losses: " + '{greatest_dec}')

#Save the output file path
output_file = os.path.join("..","analysis", "output.csv")

with open(output_file, "w", newline='') as newbudgetfile:
    csvwriter = csv.writer(newbudgetfile)
    csvwriter.writerow("Financial Analysis")
    csvwriter.writerow("-------------------")
    csvwriter.writerow(f"Total Months:" + "{total_months}")
    csvwriter.writerow(f"Net Total:" + "{net_total}")
    csvwriter.writerow(f"Average Change:" + "{mean_change}")
    csvwriter.writerow(f"Greatest Increase in Profits:" + "{greatest_inc}")
    csvwriter.writerow(f"Greatest Decrease in Profits:" + "{greatest_dec}")
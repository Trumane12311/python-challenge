import os
import csv

#Set Path for the CSV File
budgetdata = os.path.join("..","Resources","budget_data.csv")

#Open CSV File
with open(budgetdata) as csvfile:
    csvreader = csv.reader(budgetdata, delimiter=",")

def print_percentages(budgetdata):
    months = str(budgetdata[0])
    lossgain = str(budgetdata[1])

# * The total number of months included in the dataset
print("Financial Analysis")
print("---------------------------")
print("Total Months: ")
  #The net total amount of "Profit/Losses" over the entire period
print("Net Total: ")
  #Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
print("Average Change: ")
  #The greatest increase in profits (date and amount) over the entire period
print("Greatest Increase in Profits: ")
  # The greatest decrease in losses (date and amount) over the entire period
print("Greatest Decrease in Losses: ")
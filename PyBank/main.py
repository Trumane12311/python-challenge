import os
import csv

#Set Path for the CSV File
budgetdata = os.path.join('.., Resources, budget_data.csv')

#Open CSV File
with open(budgetdata, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    headers = next(csvreader)
    months = str(row[1])
    gainloss = int(row[2])
    net_total = gainloss.sum()


def print_percentages(budgetdata):
    monthspercent = str(budgetdata[0])
    lossgain = str(budgetdata[1])

monthcount = ["Jan","Feb","Mar","April","May","Jun","Jul",
            "Aug","Sep","October","November","December"]
for months in monthcount:
    print(month.count(monthcount))


# * The total number of months included in the dataset
print("Financial Analysis")
print("---------------------------")
print(f"Total Months: " + str{monthcount})
  #The net total amount of "Profit/Losses" over the entire period
print("Net Total: " + str{net_total})
  #Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
print("Average Change: " + str{mean_change})
  #The greatest increase in profits (date and amount) over the entire period
print("Greatest Increase in Profits: " + str{greatest_inc})
  # The greatest decrease in losses (date and amount) over the entire period
print("Greatest Decrease in Losses: " + str{greatest_dec})

#Save the output file path
output_file = os.path.join("..","analysis", "output.csv")

with open(output_file, "w", newline='') as newbudgetfile:
    csvwriter = csv.writer(newbudgetfile)
    csvwriter.writerow("Financial Analysis")
    csvwriter.writerow("-------------------")
    csvwriter.writerow(f"Total Months:" + {total_months})
    csvwriter.writerow(f"Net Total:" + str{net_total})
    csvwriter.writerow(f"Average Change:" + str{mean_change})
    csvwriter.writerow(f"Greatest Increase in Profits:" + str{greatest_inc})
    csvwriter.writerow(f"Greatest Decrease in Profits:" + str{greatest_dec})
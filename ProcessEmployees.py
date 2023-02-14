"""
The Customer Service Represetatives (CSRs) in the marketing department with a security clearance of 'TS' were able
to thwart an attack on the server and for that management has decided to reward them with a 10% increase in their salary. 
To evaluate the impact on the budget, you have been asked to run a report on the employee file and display the results 
of BEFORE AND AFTER the salary increase. Also calculate the total difference between the old salary and the new
salary (as shown in the image).

You will create a dictionary that has the full employee name as the key and only their NEW salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as shown in the image)
"""

import csv

# open the file
infile = open("employee_data.csv", "r")
next(infile)

# create an empty dictionary
employees_ts = {}
current_total = 0
new_total = 0

# use a loop to iterate through the csv file
for line in infile:
    line = line.rstrip("\n")
    line_list = line.split(",")
    # check if the employee fits the search criteria
    if line_list[3] == "Marketing" and line_list[4] == "CSR" and line_list[-1] == "TS":
        full_name = line_list[1] + " " + line_list[2]
        current_salary = float(line_list[5])
        print(f"Employee Name: {full_name} Current Salary: ${current_salary:,.2f}")
        new_salary = current_salary * 1.1
        employees_ts[full_name] = new_salary
        current_total += current_salary
print()
print("=========================================")
print()

# iternate through the dictionary and print out the key and value as per image

for key, value in employees_ts.items():
    print(f"Employee Name: {key} New Salary: ${value:,.2f}")
    new_total += value
print()
print("=========================================")
print()
# print out the total difference between the old salary and the new salary as per image.
total_increase = new_total - current_total
print(f"Total increase in salary: ${total_increase:,.2f}")
infile.close()

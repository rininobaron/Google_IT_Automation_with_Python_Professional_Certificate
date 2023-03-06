#!/usr/bin/env python3

import csv
csv.register_dialect('empDialect', skipinitialspace=True, strict=True)

username="ricardo"
csv_file_location="/home/"+username+"/Google_IT_Automation_with_Python_Professional_Certificate/COURSE_2_Using_Python_to_Interact_with_the_Operating_System/Week2/LAB/data/employees.csv"

# Convert employee data to dictionary

def read_employees(csv_file_location):
	with open(csv_file_location, "r") as file:
		employee_file = csv.DictReader(file, dialect = 'empDialect')
		employee_list = []
		for data in employee_file:
			employee_list.append(data)
	return employee_list

employee_list = read_employees(csv_file_location)
#print(employee_list)

# Process employee data

def process_data(employee_list):
	department_list = []
	for employee_data in employee_list:
		department_list.append(employee_data['Department'])
	department_data = {}
	for department_name in set(department_list):
		department_data[department_name] = department_list.count(department_name)
	return department_data

dictionary = process_data(employee_list)
#print(dictionary)

# Generate a report

report_file = "/home/"+username+"/Google_IT_Automation_with_Python_Professional_Certificate/COURSE_2_Using_Python_to_Interact_with_the_Operating_System/Week2/LAB/data/report.txt"

def write_report(dictionary, report_file):
	with open(report_file, "w+") as f:
		for k in sorted(dictionary):
			f.write(str(k)+':'+str(dictionary[k])+'\n')
		f.close()

write_report(dictionary, report_file)
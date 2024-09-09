"""
File: project1/input_compute_output.py
Initial developers: Professors Gitlitz and Sabin
Student developers: Christina Bevill
Date: 05-SEP-2024
"""

print("Initial Question: get minutes from years")
print("========================================")
years_str = input("Enter the number of years: ")
years = int(years_str)
days = years * 365
hours = days * 24
minutes = hours * 60
print(f"There are {minutes} minutes in {years} year(s)")
print("   ")
print("   ")
print("Question 1: get seconds from years")
print("========================================")
years_str = input("Enter the number of years: ")
years = int(years_str)
days = years * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
print(f"There are {seconds} seconds in {years} year(s)")
print("   ")
print("   ")
print("Q2: Change the problem above to go the other direction, given a number of seconds, how many years?")
print("========================================")
seconds = input("Enter a number of seconds and I'll tell you how many years, months, days, and minutes that is ")
seconds = int(seconds)
minutes = seconds / 60
hours = minutes / 60
days = hours / 24
years = days /365
print(f"There are {years} years in {seconds} seconds.")
print("   ")
print("   ")
print("Q3: Enhance solution to Q1 above so that you print the number of years, months, days and minutes.")
print("========================================")
seconds = input("Enter a number of seconds and I'll tell you how many years, months, days, and minutes that is ")
seconds = int(seconds)
minutes = seconds / 60
hours = minutes / 60
days = hours / 24
months = days / 30.42
years = days /365 
print(f"There are {years} years in {seconds} seconds")
print(f"There are {months} months in {seconds} seconds")
print(f"There are {days} days in {seconds} seconds.")
print(f"There are {minutes} minutes in {seconds} seconds.")

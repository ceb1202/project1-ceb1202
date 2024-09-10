## Initial Problem
- **Input**: Get the number of years from the user.
- **Output**: Print out the number of minutes corresponding to the given 
  number of years. 

### Algorithmic Steps
- Get number of years from user (it's a string) in variable `years_str`
- Convert `years_str` to an integer, `years`
- Find the number of days in `years` and store it in `days`
  -  Multiply `years` by 365 
- Find the number of hours in those days and store it in `hours`
  - Multiply `days` by 24
- Find the number of minutes in `hours` and store in `minutes`
  - Multiply `hours` by 60
- Print out `minutes` corresponding to `years`

## Question 1
- **Input**: Get the number of years from the user.
- **Output**: Print out the number of seconds corresponding to the number of 
  years. 

### Algorithmic Steps
- Get number of years from user (it's a string) in variable `years_str`
- Convert `years_str` to an integer, `years`
- Find the number of days in `years` and store it in `days`
  -  Multiply `years` by 365 
- Find the number of hours in those days and store it in `hours`
  - Multiply `days` by 24
- Find the number of minutes in `hours` and store in `minutes`
  - Multiply `hours` by 60
- Find the number of seconds in `minutes` and store in `seconds`
  - Multiply `minutes ` by 60
- Print out `seconds` corresponding to `years`

## Question 2
- **Input**: Get the number of seconds from the user.
- **Output**: Print out the years corresponding to the number of seconds. 
- **Assumptions**: We assume that the year has 365 days (we ignore leap years)

### Algorithmic Steps
- Get number of seconds from user (it's a string) in variable `seconds_str`
- Find the number of minutes in `seconds` and store in `minutes`
| - Divide `seconds` by 60
- Find the number of hours in `hours` in `minutes` and store in `hours`
| - Divide `minutes` by 60
- Find the number of days in `days` in `hours` and store in `days`
| - Divide `hours` by 24
- Find the number of years in `years` in `days` and store in `years`
| - Divide `days` by 365
- Print out the years corresponding to the number of seconds.

## Question 3
- **Input**: Get the number of seconds from the user.
- **Output**: Print out the umber of years, number of months, number of days, 
  and nunber of minutes corresponding to the given number of seconds. 
- **Assumptions**: 
  - Ignore leap years. 
  - Consider that all months have 30 days.
- **Hint**: Use integer division and modulo operator to avoid decimal 
    numbers. For example, dviding 65 seconds by 60 should give you 1 minutes 
    and 6 seconds, not 1.08333333. 

### Algorithmic Steps

seconds = input("Enter a number of seconds and I'll tell you how many years that is ")
seconds = int(seconds)
minutes = seconds / 60
hours = minutes / 60
days = hours / 24
months = days / 30.42
years = days /365 

print(seconds, "seconds is ", years, "years")
print(seconds, "seconds is ", months, "months")
print(seconds, "seconds is ", days, "days")
print(seconds, "seconds is ", minutes, "minutes")



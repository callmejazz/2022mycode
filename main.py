#!/usr/bin/python3
"""Alta3 Research | RZFeeser
   Review of Lists and Dictionaries"""

# define a short data set (in real world, we want to read this from a file or API)
munsters = {'endDate': 1966, 'startDate': 1964,\
        'names':['Lily', 'Herman', 'Grandpa', 'Eddie', 'Marilyn']}   # {} creates dict

# Your solution goes below this line
# ----------------------------------
print("The names of the munsters are: ", munsters.get("names"))

print("The end date for munsters is: ", munsters.get("endDate"))

print("The start date for munsters is: ", munsters.get("startDate"))

munsters["episodes"] = 99

print("episodes", munsters.get("episodes"))
#####
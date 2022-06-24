#create data
from tabulate import tabulate

data = [["Mavs", 99], 
        ["Suns", 91], 
        ["Spurs", 94], 
        ["Nets", 88]]
  
#define header names
col_names = ["Team", "Points"]
  
#display table
print(tabulate(data, headers=col_names))


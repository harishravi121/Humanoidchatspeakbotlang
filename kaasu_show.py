#Cashier Problem
'''

Few outputs
169 
[500, 100, 50, 10, 5, 2, 1]
[0.0, 1.0, 1.0, 1.0, 1.0, 2.0, 0.0]

530
[500, 100, 50, 10, 5, 2, 1]
[1.0, 0.0, 0.0, 3.0, 0.0, 0.0, 0.0]

823
[500, 100, 50, 10, 5, 2, 1]
[1.0, 3.0, 0.0, 2.0, 0.0, 1.0, 1.0]
'''
import random

bill=random.randint(5,1000)  # Generating a random bill upto 1000 Rs
print(bill)
bill2=bill
cash=[500,100,50,10,5,2,1] # Array of denominations of cash from 500 Rs to 1 Re or $
print(cash)

Breakup=[0]*len(cash) # Creating an array of length cash
#denominations where each no is a value

for i in range(len(Breakup)): 
    Breakup[i]=(bill-bill%cash[i])/cash[i] # Calculating decreasing cash nos 
    bill=bill-Breakup[i]*cash[i] # Subtracting the previous cash denomination

print(Breakup)


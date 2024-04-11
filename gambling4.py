#Dr. Harish humanoid gambling
import random
import time
while 1:
  a=input()
  time.sleep(2+2*random.random()) #Building the cresendo
  a=random.randint(1,100) #Change upper limit if needed
  print(a,a%2) #Change percent value to gamble with differenent odds. Bet a large sum in mind on reminder and see reminder
  time.sleep(2)

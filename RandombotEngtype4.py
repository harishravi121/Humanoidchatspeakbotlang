
import random


responses1=['Physics is great and fun','Ground state of Hydrogen is -13.6eV','BEC is Bose Einstein Condensate at nano kelvin','h=6e-34 Js and c=3e8 m/s']
responses2=['FInd the divergence of r^2cos(\\ theta) er','E=mc^2 and \gamma=1/\sqrt(v^2-c^2)','EMF of a line is Blv','Power radiated by a hot black body is AesigmaT^4']
responses3=['We have to go to conferences and publish in journals like nature, science and EJPD']
responses4=['Life is prokaryotes and Eukaryotes','Heart has 4 chambers and couples to body and respiratory system','Brain has a billion neurons','Eat 1900 calories a day and atleast 60 g of protein']
responses5=['Love all serve all','Help ever hurt never','Patience is a virtue','There should be deva chintana',' Observe a path of devotion']
responses6=['Compound interest is (1+r/100)^n','As prices increase demand decreases','Stocks, mutual funds and real estate are good investment vehicles']
jobs=['Apply for a post doc','Apply for a electronics job','Apply for a physics teaching job','Apply for a labour job']
history=['India got its independence in 1947','Bronze age was in 3000 BC']
law=['Fundamental duties are called bill of rights in USA','Patents act 1970 protects for 20 years']
geography=['India is situated north of the equator between 8°4\' north (the mainland) to 37°6\' north latitude and 68°7\' east to 97°25\' east longitude.']
psychology=['Psychology is the study of mind and behavior in humans and non-humans.','Psychology includes the study of conscious and unconscious phenomena, including feelings and thoughts.']
responses=responses1+responses2+responses3+responses4+responses5+responses6+jobs+history+law+geography+psychology
while 1:
    a=input()
    responsejj=['I spent '+str(random.randint(10,500))+' $ on shopping','I spent '+str(random.randint(10,500))+' $ on shopping']
    
    z2=random.choice(responses+responsejj)
    print('Dr. Harish 2 the physicist : ' ,z2,'.')
 



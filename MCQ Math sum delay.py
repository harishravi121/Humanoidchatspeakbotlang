import random
import time



while 1:
    n1=random.randint(2,100)
    n2=random.randint(2,100)
    print(n1,n2,'what is sum')
    ans=[n1+n2,n1+n2+random.randint(2,10),n1+n2+random.randint(2,10),n1+n2+random.randint(2,10)]
    random.shuffle(ans)
    print(ans)
    chs=input()
    if(ans[int(chs)-1]==n1+n2):
        print('Correct, congrats')
    else:
        print('wrong')
    time.sleep(2+random.random()*2)

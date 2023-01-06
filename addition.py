#Generate two random single digit integers n1 and n2
import random
n1=random.randint(1,9)
n2=random.randrange(1,10)
#####n3 = n1+n2????

#Ask the user what is n1 + n2? 
#print('what is',n1,'+',n2,'?')
#have user input their response 
#answer = int(input('enter your answer: '))
###if correct: print correct
##if answer==n1+n2:
##    print('That is correct:',n1,'+',n2,'=',answer)
###else: print incorrect 
##else:
##    print("That is incorrect, try again!")
##while answer!=n1+n2:
##    print("That is incorrect, try again!")
##    print('what is',n1,'+',n2,'?')
##    answer = int(input('enter your answer: '))
##else:
##    print('That is correct:',n1,'+',n2,'=',answer,'!')
for i  in range(1,4):
    print('what is',n1,'+',n2,'?')
    answer = int(input('enter your answer: '))
    if answer == n1+n2:
        print('you are correct:',n1,'+',n2,'=',answer)
        break
    else:
        print('your answer is incorrect')
#end of loop /outside the loop 
if answer!=n1+n2:
    print('please review your note')

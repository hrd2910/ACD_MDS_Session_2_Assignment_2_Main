# Create the below pattern using nested for loop in Python.

#  *
#  * *
#  * * *
#  * * * *
#  * * * * *
#  * * * *
#  * * *
#  * *
#  *
#End of comment


n=5;
         # outer loop to handle number of rows
         # n in this case is number of rows
for i in range(n):
         # inner loop to handle number of columns        
    for j in range(i):
        print ('* ', end="")
    print('')
        # running the loop in reverse order     
for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')


# a  = int(input('enter any number'))
a=int(input('ENTER NUMBER:  '))
a=abs(a)

for p in range(0,a,1):
    print(' '*(a-p),(' ')*(p+1))
    
print('',' '*(a+1))

for p in range(a,0,-1):
    p=p-1
    print(' '*(a-p),(' ')*(p+1))
    

    
    
    
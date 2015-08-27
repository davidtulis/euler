x=20
hits=0
test = range(x/2+1, x+1)
while (True):
    for num in test:
        if x%num==0:
            hits+=1
        else:
            x+=20
            break
    if hits==len(test):
        break

print x        

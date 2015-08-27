##print max(x*y for x in range(1000, 100, -1) for y in range(1000, x-1, -1)
##          if str(x*y)==str(x*y)[::-1])

def isPalindrome(s):
    s=str(s)
    if len(s)<=1:
        return True
    else:
        if s[0]==s[-1]:
            return isPalindrome(s[1:-1])
        else:
            return False
for x in reversed(range(1000, 100)):
    for y in reversed(range(1000, x-1)):
        if isPalindrome(x*y):
            print x*y    

x=91
y=99
print str(x*y)
print str(x*y)[::-1]
s="abcdef"
print s[::-1]

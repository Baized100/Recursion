#The term Recursion can be defined as the process of defining something in terms of itself. In simple words, it is a process in which a function calls itself directly or indirectly. 
def fact(n):
    if n==1:
        return 1
    else:
       return n*fact(n-1)
print(fact(5))

def fact(n):
    ans = 1 
    while n > 1:
        ans *= n
        n-=1 
    return ans

a = fact(10)
print(a)
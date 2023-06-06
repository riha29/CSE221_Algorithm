# Determining the factorial of any number. Factorial is multiplying the number with every 1unit less than the number until
# it's 0. for example, 5!= 5*4*3*2*1

# Hence, n!= n*(n-1)*(n-2)*...........2*1

def factorial(n):
    if n==1:
        return n
    return n* factorial(n-1)

print(factorial(5))
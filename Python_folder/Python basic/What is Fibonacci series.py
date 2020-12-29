# What is Fibonacci Series?
# Fibonacci series is a series of numbers formed by the addition of the preceeding two numbers in the series.

# Example of Fibonacci Series: 0,1,1,2,3,5

# In the above example, 0 and 1 are the first two terms of the series. These two terms are printed directly. The third term is calculated by adding the first two terms. In this case 0 and 1. So, we get 0+1=1. Hence 1 is printed as the third term. The next term is generated by using the second and third term and not using the first term. It is done until the number of terms you want or requested by the user. In the above example, we have used five terms.

def fiboIter(n):
    pass

def fiboRecur(n):
    if n==0:
        return 0
    elif(n==1):
            return 1
    else:
        return fiboRecur(n-1) + fiboRecur(n-2)

if __name__ == '__main__':
    num =int(input("Enter a number"))
    print(f"Using recursion value of fib({num}) is {fiboRecur(num)}")



























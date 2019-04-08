#https://www.programiz.com/python-programming/examples/fibonacci-sequence 08.04.19

'''Program to display the Fibonacci sequence up to n-th term where n is provided by the user'''

# change this value for a different result
nterms = 10

# uncomment to take input from the user
nterms = int(input("How many terms? "))

# first two terms
n1 = 0
n2 = 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence upto",nterms,":")
   while count < nterms:
       print(n1,end=' , ')
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1

#def fib(n):
#  '''Calculate the nth Fibinacci number'''
#	if n == 0 or n == 1:
#		return 1
#
#	return fib(n-1) + fib(n-2)

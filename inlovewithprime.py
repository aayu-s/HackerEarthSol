

#new changes
#Every even number can be represented as prime number
t = int(input())
while t>0:
    t -= 1
    a = int(input())
    if a != 2:
        print("Deepa")
    else:
        print("Arjit")

# METHOD 2 : for all the numbers
# import math

# t = int(input())
# inp = []
# out = []
# while t>0:
#     n = int(input())
#     inp.append(n)
#     t-=1
    

# def isPrime(n): 
#     if n <= 1: 
#         return False
#     for i in range(2, (int)(math.sqrt(n))): 
#         if n % i == 0: 
#             return False
#     return True
  
# def isPossible(n):
#     for i in range(2, n-1):
#         print(n-i,i)
#         if isPrime(n-i) and isPrime(i):
#             return True
        
# for elem in inp:
#     if elem == 1:
#         out.append("Arjit")
#     elif isPossible(elem) == True: 
#         out.append("Deepa") 
#     else: 
#         out.append("Arjit")
        
# print(*out, sep="\n")

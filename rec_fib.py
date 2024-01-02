# f0 = 0
# f1 = 1

# def fibo(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return  fibo(n-2) + fibo(n-1)

# for i in range(10):
#     print(fibo(i))


# s1 = {5,9,11,6}
# s2 = {9,6}
# print(s2.issubset(s1)) #True
# print(s1.difference(s2))  # {11, 5}
# print(s1.issuperset(s2)) #True
# print(s1.isdisjoint(s2)) #False


# s1 = {5,9,11,6}
# s2 = {9,6,8,3}
# print(s1.symmetric_difference(s2)) # {3, 5, 8, 11}


# class quitError(Exception):
#      pass
    
    
# inp = input("enter an input  quit")


# try:
#     if inp == "quit":
#         print("quiting ")
#     else:
#         raise quitError
# except quitError:
#     print("its not written quit")


#-------------------- parantheses generation -------------------

# def generate_parentheses(n):
#     def backtrack(s, left, right):
#         if len(s) == 2 * n:
#             combinations.append(s)
#             return
#         if left < n:
#             print(f"left { left} < {n} n")
#             print(f" backtrack(s + '(', left + 1, right)   backtrack(s + '(', {left + 1} left + 1, {right}right) ")
#             backtrack(s + '(', left + 1, right)
            
#         if right < left:
#             print(f"right {right} < {left} left")
#             print(f"backtrack(s + ')', left, right + 1)  backtrack(s + ')', left{left}, {right+1}right + 1)")
#             backtrack(s + ')', left, right + 1)

#     combinations = []
#     backtrack('', 0, 0)
#     return combinations

# # Example usage:
# n = 3
# result = generate_parentheses(n)
# print(result)
#-----------------------------------------------------------

#-------------------------stair case problem----------------
# def stairWayCount(n):
#     if n<0:
#         return 0
#     if n == 0:
#         return 1
    
#     ans = stairWayCount(n-1) + stairWayCount(n-2)
    
#     return ans

# print(stairWayCount(4))  # 5
    


#-----------------------------------------------------------

# -------------------------- number printing problem------------

# def counter(n,d):
    
    
#     if n == 0:
#         return
#     dig = int(n % 10)
#     n = n // 10
    
#     counter(n,d)
#     print(d[dig])
    

# d = ["Zero","One","Two","Three","Four","Five","Six","Seven", "Eight","Nine"]
# n= 596
# counter(n,d)

#---------------------------------------------------------------

# #------------ sorted or not----------#
# def isSorted(arr,size):
#     if size == 0 or size == 1:
#         return True
#     if arr[0]>arr[1]:
#         return False
#     else:
#         return isSorted(arr[1:],size-1)
    
# arr = [5,8,33,86]
# size = len(arr)
# print(isSorted(arr,size))
# #--------------------------------------

# def sum(arr,size):
#     if size == 0:
#         return 0
#     if size == 1:
#         return arr[0]
    
#     rem = sum(arr[1:],size -1)
#     s = arr[0] + rem
#     return s
    
# arr = [4,9,5,8,3,6]
# print(f" trial.. {arr[0:3]}")
# size = len(arr)
# print(sum(arr,size))



# def pri(n,limit):
#     if n <= limit:
#         pri(n+1,limit)
#         print(n)
# pri(1,15)

# import re
# s = "X-OXXXO-O"
# pattern = re.compile(r"\b\w{3}XXX{3}.*")
# match = pattern.search(s)
# if match:
#     print("X won")
# else:
#     print("mari gayo")
    
import re

 



def checkIt(i,j,k,text):
    s = f"{text[i]}{text[j]}{text[k]}"
    print(s)
    if (s == "XXX") or (s == "OOO"):
        print("in def")
        return 1
    else :
        return 0
text = "OXO-XXXO-" 
checker = 0
for i in range(0,7,3):
    checker = checkIt(i,i+1,i+2,text)
    if checker == 1:
        print("horizontal")
        break


print(f"checker val {checker}")   
if checker == 0:
    for i in range(0,3):
        checker = checkIt(i,i+3,i+6,text)
        if checker == 1:
            print("vertical")
            break
print(f"checker val {checker}")  

if checker == 0:
    checker = checkIt(0,4,8,text)
    print("diagonal1")

print(f"checker val {checker}") 
if checker == 0:
    checker = checkIt(2,4,6,text)
    print("diagonal 2")
   
print(f"checker val {checker}")   

if checker == 0:
    print("no one won")

    



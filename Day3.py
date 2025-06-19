# while loop, for loop, function

"""count = 1
while (count <= 5):
    print("Hello")
    count+=1
"""

"""a = 1
while a <= 100:
    print(a)
    a = a+1"""

"""a = 100
while a >= 1:
    print(a)
    a = a-1"""

"""n = int(input("Enter a number = "))
i = 1
while i<= 10:
    print(n*i)
    i += 1 """

"""nums = [1,2,4,11,13,20,25,30,40,50]
i = 0
while i < len(nums):
    print(nums[i])
i += 1 """

"""i = 100
while i >= 1:
    print(i)
    i -= 1"""

"""i = 1
n = int(input("Enter a number = "))
while i <= 10:
    print(n*i)
    i += 1"""

"""num = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
idx = 0
while idx < len(num):
    print(num[idx])
    idx += 1"""

"""x = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
x = 12
i = 0
while i < len(num):
    if (num[i] == x):
        print("Found index at  ", i)
        i +=1

for num in x:
    print(num)"""


"""x = ("Manav", "Jay", "Smit", "Sahal", "Preet", "Pratham")
for val in x:
    print(val)"""

"""x = [12, 34, 56, 78, 90, 98, 76, 54, 32, 10]
a = 10
i = 0
for el in x:
    if(el == x):
        print("Element found at index : ", i)
    i += 1"""

"""x = [12, 34, 56, 78, 90, 98, 76, 54, 32, 10]
a = 98
i = 0
for el in x:
    if (el == a):
        print("Element found at index:", i)
    i += 1"""


"""for i in range(0,10):
    print(i)"""
"""
for i in range(10,0,-1):
    print(i)"""

"""n = int(input("Enter a number : "))
for i in range(1,11):
    print(n*i)"""
"""
n = int(input("Enter a number = "))
i = 1
while i<=10:
    print(n*i)
    i += 1"""

"""def calu_sum(a, b):
    sum = a + b
    print(sum)
    return(sum)

calu_sum(5, 4)"""
"""
cites = ["Gujarat", "Mumbai", "Rajestan", "Punjab", "Hydrabad", "Chennai", "Kashmir", "Delhi"]
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def print_lenth(list):
    print(len(list))


print_lenth(cites)
print_lenth(num)"""

"""
def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD = ", inr_val, "INR = ")


converter(300)"""
"""
def calculate_sum(a , b):
    sum0 = a + b
    sum1 = a - b
    sum2 = a * b
    sum3 = a / b
    print(sum0, sum1, sum2, sum3)
    return sum0, sum1, sum2, sum3


calculate_sum(20 , 30)"""



"""def calc_avg(a, b, c):
    sum = a + b + c
    avg = sum / 2
    print(avg)
    return avg


calc_avg(4, 2, 9)
"""


"""num = [2,3,4,6,4,2,7,8,9,4,1,2,4,5,6,7]
cities = ["Ahmedabad", "Amritshar", "Chennai", "Anand", "Nadiad", "Kheda","Surat"]
heros = ["Ironman", "Spiderman", "Superman", "Batman", "Homelander", "Caption America", "Thor", "Hulk", "Vision", "Black Panter","Flesh","Aquaman", "Wolverin"]
"""
"""
def lenth_list(list):
    print(len(list))
    return list


lenth_list(num)
lenth_list(cities)
lenth_list(heros)"""


"""
def print_list(list):
    for item in list:
        print(item, end=" ")
        
    

print_list(heros)
"""


#def cal_fact(n):
#    fact = 1
#    for i in range(1, n+1):
#        fact *= i 
#        print(fact)


#cal_fact(6)

"""
def exch_cur(usd_val):
    inr_val = usd_val * 86.07
    print(usd_val , "USD = ", inr_val, "INR = ")


exch_cur(1000)"""


def even_odd(num):
    if num % 2 == 0:
        print("Even")

    else:
        print("Odd")

even_odd(10)

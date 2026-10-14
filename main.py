# def func(a,b):
#     return a+b

# def func2(a,b):
#     print(a+b)
#     return 5

# m = func2(1,20)

# print(m)


# def func(a):
#     n = []
#     for i in a:
#         if i==a:
#             i.append(n)
#             func([1,2,3,4,5,5])



# def factorial(n):
#     if n==1:
#         return 1
#     return n*factorial(n-1)
# print(factorial(9))

# def factorial(n):
#     if n==1:
#         return 1
#     return n+factorial(n-1)
# print(factorial(4))

# def factorial(a):
#     if a== 1:
#         return 1
#     return a**2+factorial(a-1)
# print(factorial(6))


# def factorial(a):
#     if a==0:
#         return 
#     print(a)
#     return factorial(a-1)

# factorial(6)

# def factorial(n):
#     if n==1:
#         return 1
#     return n**2+factorial(n-1)
# print(factorial(3))


#2
# def factorial(n):
#     if n==1:
#         return 1
#     return n**3+factorial(n-1)
# print(factorial(2))


#3
# def func(a):
#     if a==1:
#         return 1
#     return a**1+func(a-1)



# ///////////// HOME WORK ///////////////////////////////


#1
# def Dictionary(name, age, city):
#     student = {
#         "Name": name,
#         "Age": age,
#         "City": city
#     }
    
#     for i, a in student.items():
#         print(f"{i}: {a}")

# Dictionary("Ali", 18, "Khujand")



#2
# def Dictionary():
#     name = input("Enter your name: ")
#     age = input("Enter your age: ")
#     city = input("Enter your city: ")
#     student = {
#         "Name": name,
#         "Age": age,
#         "City": city
#     }
#     print("")
#     for i, a in student.items():
#         print(f"{i}: {a}")
# Dictionary()


#3
# def Dictionary(student):
#     total_sum = sum(student.values())
#     return total_sum
# items = {
#     "apple": 10,
#     "banana": 15,
#     "orange": 20
# }
# result = Dictionary(items)
# print(result)


#4
# def Dictionary(text):
#     words = text.split()
#     items = {}
#     for word in words:
#         items[word] = items.get(word, 0) + 1
#     return items
# text = "apple banana apple orange banana apple"
# result = Dictionary(text)
# print(result)


#5
# def Dictionary(box, boxx):
#     if boxx in box:
#         return box[boxx]
#     else:
#         return "Not found"
# students = {
#     "Ali": 90,
#     "Sara": 85,
#     "Omar": 70
# }
# text = "Sara"
# result = Dictionary(students, text)
# print(result)

#6
# def Dictionary(box, box1, price):
#     box[box1] = price
#     return box
# products = {
#     "apple": 10,
#     "banana": 15
# }
# box2 = Dictionary(products, "orange", 20)
# print(box2)



#7
# def Dictionary(d):
#     name = max(d, key=d.get)
#     print(name, d[name])
# products = {'phone': 500, 'laptop': 1200, 'tablet': 700}
# Dictionary(products)

#8
# def Dictionary(box, name):
#     box.pop(name, None)
#     return box
# students = {'Ali': 90, 'Sara': 85, 'Omar': 70}
# result = Dictionary(students, "Sara")
# print(result)


#9
# def Dictionary(dict1, dict2):
#     box = dict1.copy()
#     box.update(dict2)
#     return box

#10
# def Dictionary(box):
#     for name, score in box.items():
#         if score >= 80:
#             print(name, end=" ")
# students = {'Ali': 90, 'Sara': 75, 'Omar': 85, 'Zara': 60}
# Dictionary(students)

#11
# def Dictionary(box, name):
#     box.pop(name, None)
#     return box
# students = {1:'Ali', 2:'Sara', 3:'Omar'} 
# result = Dictionary(students, "")
# print(result)


#13
# s = "hello world"
# result = len(s.replace(" ", ""))
# print(result)  

#14
# s = "PYTHON"
# String  = s.upper()
# box = s.lower()
# print(String , box)

#15
# s = "hello python"
# result = s.strip()
# print(result)  

#16
# s = "This is a bad day"
# result = s.replace("bad", "good")
# print(result) 

#17
# s = "programming"
# box = "pro"
# box1 = "ing"
# starts = s.startswith(box)
# ends = s.endswith(box1)
# print(starts, ends)  


#18
# s = "apple,banana,orange"
# result = s.split(",")
# print(result)  

#19
# words = ['Python', 'is', 'easy']
# result = "-".join(words)
# print(result)
 

# 20  
# s = "banana"
# result = s.count("an")
# print(result)

#21
# s= "12345"
# result = s.isdigit()
# print(result)


#22
# s = "aLi ahmEd"
# result = s.title()
# print(result)  

#23
# def greet(name):
#     print("Салом,")


#24
# def greet(name):
#     print(f"Hello, {name}!")

# greet("Ali")

#25
# def add(a, b):
#     return a + b
# result = add(5, 7)
# print(result) 

#26
# def box(n):
#     if n % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
# result = box(8)
# print(result)  

#27
# def square(n):
#     return n ** 2
# result = square(6)
# print(result)  

#28
# def maximum(a, b):
#     if a > b:
#         return a
#     else:
#         return b
# result = maximum(12, 7)
# print(result) 

#29
# def i(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
# print(i(5))  


#30
# def sum_numbers(n):
#     return sum(range(1, n + 1))
# print(sum_numbers(10))
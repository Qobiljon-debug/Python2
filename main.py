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


# ///////////////////////////////////////// 3 RYZ KLASS TASK ///////////////////////////////

# def box (n):

#     if n==1:
#         return 1
#     if(n % 2 == 0 or n % 3 == 0) and (n % 6 != 0):
#         return n+box(n-1)
#     return box (n-1)

# print(box(10))

# task 8

# n1=int(input())
# q1=int(input())
# def multiple(n):
#     def my_inner(q):
#         return n1*q1
#     return my_inner
# hosili_zarb=multiple(n1)
# print(hosili_zarb(q1))

# task 9

# sum=0
# def accumulator():
#    def my_inner(n):
#       global sum
#       sum+=n
#       return sum
#    return my_inner
# summa=accumulator()
# print(summa(5))
# print(summa(10))
# print(summa(20))

#task 10

# count=0
# def attempt(limit):
#    def my_inner():
#       global count
#       count+=1
#       if count<=limit:
#          return f"Attempt {count}"
#       else:
#          return "Mytasifona Limiti shumo ba anjom rasid!"
#    return my_inner
# cnt=attempt(10)
# print(cnt()) 
# print(cnt())
# print(cnt())
# print(cnt())
# print(cnt())
# print(cnt())
# print(cnt())
# print(cnt())
# print(cnt())
# print(cnt())
# print(cnt())

#task 11

# def bank_account(balance):
#     def deposit(amount):
#          nonlocal balance
#          balance+=amount
#          return balance
#     def withdraw(amount):
#          nonlocal balance
#          if balance < amount:
#             return "Not enough money!"
#          balance-=amount
#          return balance
#     return deposit,withdraw
# deposit,withdraw=bank_account(1000)
# print(deposit(500))
# print(withdraw(300))
# print(withdraw(1500))

#task 12

# def time_greeting(period):
#     def my_inner(name):
#         if period=="morning":
#             return f"Goog morning {name}"
#         elif period=="afternoon":
#             return f"Good afternoon {name}"
#         else:
#             return f"Good night {name}"
#     return my_inner
# men=time_greeting("night")
# print(men("Abdulvahhob"))

# task 13

# def logger():
#     history = []  
#     def log(message):
#         nonlocal history
#         history.append(message)  
#         return history           
#     return log
# my_log = logger()
# print(my_log("start"))    
# print(my_log("process"))  
# print(my_log("end"))

#1
# def n(b,a=1):
#     if a==b:
#         return b
#     print (a)
#     return n(b, a+1)

# print(n(10))

#2
# def s(a,b):
#     if b==a:
#         return b
#     print(a)
#     return s(b, a+1)
    
# print(s(10))


#3
# def s(a,b):
#     if a==b:
#         return a
#     print(a)
#     return s(a+1,b)
    
# print(s(3,7))

#1
# def box(name):
#     print(name)
#     def box2(hello):
#         print(hello)

#         box("Ali")


#2
# def time_greeting(name, morning):
#     def greet():
#         return f"Good {morning.lower()}, {name}!"
#     return greet
# f = time_greeting("Aziz", "morning")
# print(f())

#3
# def logger():
#     history = []
#     def log(message):
#         history.append(message)
#         return history
#     return log
# log = logger()
# print(log("start"))     
# print(log("process"))   
# print(log("end"))       

#4
# def temperature_converter(scale):
#     if scale == "c":
#         return lambda t: (t * 9/5) + 32
#     return lambda t: (t - 32) * 5/9
# convert = temperature_converter("c")
# print(convert(100))  

# ////////////////////////////////// 4 Home Task ///////////////////////////////////////////////////////

#5
# def outer():
#     def inner():
#         print("This is inner fanction")

#     inner()

# try:
#     outer()
# except NameError:
#     print("inner not defoind")


#6
# def rectangle_info (w,h):
#     def area ():
#         x=h*w
#         return x
#     def perimetr():
#         y=2*(w+h)
#         return y
#     print("Area: ",area())
#     print('Perimetr: ',perimetr())
# rectangle_info(4,5)


#7
# def calc_average(*args):
#     sum=0
#     cnt=0

#     def total():
#         nonlocal sum,cnt
#         for i in args:
#             sum+=i
#             cnt+=1 
#         print(sum/cnt)
#     return total()
# calc_average(2,4,6)


#8
# def print_receipt(items):
#     def line(name, prise):
#         return f'{name}:{prise}'
#     total=0
#     for name, prise in items.items(): 
#         print(line(name,prise))
#         total+=prise
#     print(f'total: {total}')
# print_receipt({"tea": 12, "bread": 3.5}) 


#9
# def validate_password(pwd):
#     def has_digit():
#         for i in pwd:
#             if i.isdigit():
#                 return True
#         return False
#     def has_upper():
#         for i in pwd:
#             if i.isupper():
#                 return True
#         return False
#     return len(pwd) >=8 and has_digit() and has_upper()
# print(validate_password("Python123"))  # True
# print(validate_password("python123"))  # False


#10
# def make_table(n):
#     def row(i):
#         return f'{n}+{i}={n*i}'
#     for i in range(1,6):
#         print(row(i))

# make_table(7)


#11
# def level1():
#     print('Level 1')
#     def level2():
#         print('Level 2')
#     level2()     
#     def level3():
#         print('Level 3')
#     level3()
# level1()


#12
# def calc_discount(prise,present):
#     def calc_discount():
#         return(prise*10)/100
#     return calc_discount()
# print()


#13
# def make_adder(x):
#     def add(y):
#         return x+y
#     return add
# add5 = make_adder(5)
# add10 = make_adder(10)
# print(add5(3))  
# print(add10(3))


#14
# def power_creator(exp):
#     def power(base):
#         return base ** exp
#     return power
# square = power_creator(2)
# cube = power_creator(3) 
# fourth = power_creator(4)  
# print(square(4)) 
# print(cube(2))   
# print(fourth(2)) 

#15
# def make_multiplier(n):
#     def multiplier(x):
#         return x * n
#     return multiplier
# double = make_multiplier(2) 
# triple = make_multiplier(3) 
# print(double(7))  
# print(triple(7))  

#16
# def make_greeter(hello):
#     def greeter(name):
#         return f"{hello}, {name}!"
#     return greeter
# hi = make_greeter("Salom")
# hello = make_greeter("Hello")
# print(hi("Ali"))  
# print(hello("Zarina"))

# #17/////////////////////////////natavonistam//////////
# def make_adder(x):
#     def add(y):
#         return x + y
#     return add
# add5 = make_adder(5)
# print(type(add5))
# print(add5.__name__)   

#18
# def make_adder(x):
#     def add(y):
#         return x + y
#     return add
# add5 = make_adder(5)
# print(add5.__closure__[0].cell_contents)  

#19
# def outer_func():
#     x = 10  
#     def inner_func():
#         return "Salom"  
#     return inner_func
# my_func = outer_func()
# print(my_func.__closure__) 

#20
# def make_discount(percent):
#     def discount(price):
#         return price * (1 - percent / 100)
#     return discount
# sale10 = make_discount(10) 
# sale25 = make_discount(25) 
# print(sale10(200))  
# print(sale25(200)) 

#21
# def make_converter(rate):
#     def converter(amount):
#         return amount * rate
#     return converter
# usd_to_tjs = make_converter(11)
# print(usd_to_tjs(100))  

#22
# def make_tag(tag):
#     def wrap(text):
#         return f"<{tag}>{text}</{tag}>"
#     return wrap
# bold = make_tag("b")
# print(bold("Hi")) 

#23
# def make_checker(min_len):
#     def check(text):
#         return len(text) >= min_len
#     return check
# check8 = make_checker(8)
# print(check8("qwerty")) 
# print(check8("qwerty123"))  

#24
# def make_in_range(low, high):
#     def check(number):
#         return low <= number <= high
#     return check
# is_teen = make_in_range(13, 19)
# print(is_teen(15))  
# print(is_teen(25)) 

#25
# def make_word_filter(banned):
#     def filter_text(text):
#         for word in banned:
#             text = text.replace(word, "***")
#         return text
#     return filter_text
# clean = make_word_filter({"bad"})
# print(clean("this is bad word"))  

#26
# def make_logger(prefix):
#     def log(message):
#         print(f"{prefix}, {message}")
#     return log
# info = make_logger("INFO")
# error = make_logger("ERROR")

# info("Started") 
# error("File missing") 

#27
# def outer_func():
#     outer_var = 10  
#     def inner_func():
#         outer_var = 20  
#         print("Inner:", outer_var)  
#     inner_func()
#     print("Outer:", outer_var)  
# outer_func()

#28
# def counter():
#     cnt=0
#     def c():
#         nonlocal cnt
#         cnt+=1
#         return cnt
#     return c
# c = counter()
# print(c())  # 1
# print(c())  # 2
# print(c())  # 3

# 29
# def make_counters():
#     cnt1 = 0
#     cnt2 = 0
    
#     def inc1():
#         nonlocal cnt1
#         cnt1 += 1
#         return cnt1
#     def inc2():
#         nonlocal cnt2
#         cnt2 += 1
#         return cnt2
#     return inc1, inc2

# cnt1, cnt2 = make_counters()
# print(cnt1())  # 1
# print(cnt1())  # 1
# print(cnt2())  # 2

#30
# def counter(start=0, step=1):
#     current = start
#     def c():
#         nonlocal current
#         current += step
#         return current
#     return c
# c = counter(10, 5)
# print(c(), c(), c())  # Output: 15 20 25


#31
# def make_countdown(n):
#     def countdown():
#         nonlocal n
#         if n > 0:
#             current = n
#             n -= 1
#             return current
#         return "Done!"
#     return countdown
# cd = make_countdown(3)
# print(cd(), cd(), cd(), cd())  # Output: 3 2 1 Done!

#32
# def make_accumulator():
#     total = 0
#     def accumulate(value):
#         nonlocal total
#         total += value
#         return total
#     return accumulate
# acc = make_accumulator()
# print(acc(10))  # Output: 10
# print(acc(5))   # Output: 15
# print(acc(20))  # Output: 35

#33
# def make_average():
#     total = 0
#     count = 0
#     def add(number):
#         nonlocal total, count
#         total += number
#         count += 1
#         return total / count
#     return add
# avg = make_average()
# print(avg(10))  # Output: 10.0
# print(avg(20))  # Output: 15.0
# print(avg(30))  # Output: 20.0

#34
# def make_history():
#     history = []
#     def add(item):
#         history.append(item)  
#         return history
#     return add
# h = make_history()
# print(h("a"))  # Output: ['a']
# print(h("b"))  # Output: ['a', 'b']

#35
# def make_toggle():
#     state = False
#     def toggle():
#         nonlocal state
#         state = not state  
#         return state
#     return toggle
# t = make_toggle()
# print(t(), t(), t())  # Output: True False True


# ////////////////////////////////////////////////////////////// 5 Home Work /////////////////////////////////////////////////////

# import time
# import functools
# def decorator_1(func):
#     def wrapper():
#         print("Before function")
#         func()
#         print("After function")
#     return wrapper
# def say_hello_1():
#     print("Hello")
# new_func=decorator_1(say_hello_1)
# new_func()
# def decorator(func):
#     def wrapper():
#         print("Before function")
#         func()
#         print("After function")
#     return wrapper
# @decorator
# def say_hello():
#     print("Hello")
# say_hello()
# @decorator
# def say_bye():
#     print("Bye")
# say_hello()
# say_bye()
# new_func_4=decorator_1(say_hello_1)
# new_func_4()
# print("---")
# say_hello_1()
# def stars(func):
#     def wrapper(*args,**kwargs):
#         print("*****")
#         res=func(*args,**kwargs)
#         print("*****")
#         return res
#     return wrapper
# @stars
# def show_python():
#     print("Python")
# show_python()
# def decorator_arg(func):
#     def wrapper(name):
#         print("Before function")
#         func(name)
#         print("After function")
#     return wrapper
# @decorator_arg
# def greet_arg(name):
#     print(f"Hello, {name}")
# greet_arg("Ali")
# def universal_decorator(func):
#     def wrapper(*args,**kwargs):
#         print("Before function")
#         res=func(*args,**kwargs)
#         print("After function")
#         return res
#     return wrapper
# @universal_decorator
# def add_uni(a,b):
#     print(a+b)
# @universal_decorator
# def greet_uni(name):
#     print(f"Hello, {name}")
# add_uni(2,3)
# greet_uni(name="Ali")
# def decorator_return(func):
#     def wrapper(*args,**kwargs):
#         return func(*args,**kwargs)
#     return wrapper
# @decorator_return
# def add_ret(a,b):
#     return a+b
# print(add_ret(2,3))
# def uppercase(func):
#     def wrapper(*args,**kwargs):
#         result=func(*args,**kwargs)
#         return result.upper()
#     return wrapper
# @uppercase
# def say_hello_up():
#     return "Hello, Ali"
# print(say_hello_up())
# def double_result(func):
#     def wrapper(*args,**kwargs):
#         return func(*args,**kwargs)*2
#     return wrapper
# @double_result
# def get_number():
#     return 7
# print(get_number())
# def hello_line(func):
#     def wrapper(*args,**kwargs):
#         print("Hi!")
#         return func(*args,**kwargs)
#     return wrapper
# @stars
# @hello_line
# def say_double():
#     print("Python")
# say_double()
# def count_calls(func):
#     count=0
#     def wrapper(*args,**kwargs):
#         nonlocal count
#         count+=1
#         print(f"Call {count}")
#         return func(*args,**kwargs)
#     return wrapper
# @count_calls
# def say_hi_count():
#     print("Hi")
# say_hi_count()
# say_hi_count()
# def logger(func):
#     def wrapper(*args,**kwargs):
#         print(f"Calling {func.name} with {args}")
#         res=func(*args,**kwargs)
#         print(f"{func.name} returned {res}")
#         return res
#     return wrapper
# @logger
# def add_log(a,b):
#     return a+b
# add_log(2,3)
# def timer(func):
#     def wrapper(*args,**kwargs):
#         start=time.perf_counter()
#         res=func(*args,**kwargs)
#         end=time.perf_counter()
#         print(f"{func.name} took {round(end-start,1)} sec")
#         return res
#     return wrapper
# @timer
# def slow():
#     time.sleep(0.2)
# slow()
# def only_positive(func):
#     def wrapper(*args,**kwargs):
#         if any(isinstance(arg,(int,float)) and arg<0 for arg in args):
#             print("Negative numbers not allowed")
#             return None
#         return func(*args,**kwargs)
#     return wrapper
# @only_positive
# def calc_pos(x):
#     return x*2
# print(calc_pos(6))
# print(calc_pos(-4))
# def safe_divide(func):
#     def wrapper(*args,**kwargs):
#         try:
#             return func(*args,**kwargs)
#         except ZeroDivisionError:
#             return "Cannot divide by zero"
#     return wrapper
# @safe_divide
# def divide(a,b):
#     return a/b
# print(divide(10,2))
# print(divide(5,0))
# def require_login(func):
#     def wrapper(user,*args,**kwargs):

# ///////////////////////////////////////////////////// Home Work //////////////////////////////////////
# class Car:
#     def init(self,brand,year,color,price):
#         self.brand=brand
#         self.year=year
#         self.color=color
#         self.price=price

#     def sell(self):
#         print(f"price of this car is  {self.price}")
#     def info(self):
#         print(f"brand of this car is {self.brand} and year of this car is {self.year} and color of this car is {self.color}")
#     def discout(self):
#         print(f"{self.price -100}")

# car1=Car("Toyota",2020,"Red",20000)

# car2=Car("Honda",2021,"Blue",25000)

# car1.discout()
# car1.info()
# car2.discout()
# car2.info()

# class Employee:
#     def __init__(self,name,position,salary):
#         self.name=name
#         self.position=position
#         self.salary=salary

#     def info(self):
#         print(f'{self.name} - {self.position} - {self.salary}')

#     def add_salary(self,present):
#         res=self.salary * present // 100
#         self.salary+=res

#         print(f'now salary is {self.salary}')

#     def change_position(self,new_position):
#         self.position is self.position
#         print(f'Now new position is {self.position}')

# eml=Employee('Numon','CEO',100)

# eml.info()
# eml.add_salary(50)
# eml.change_position('Admin')


# class Company:
#     def __init__(self, name):
#         self.name=name
#         self.employee=[]

#     def add_employee(self,name):
#         self.employee.append(name)

#     def delete_employee(self,name):
#         self.employee.remove(name)

#     def show_all(self):
#         print(f'Company name - {self.name}')
#         for i in self.employee:
#             print(f'{i} - employee')

# cl=Company("Megafon")

# cl.add_employee('Abdulvahob') 
# cl.add_employee('Numon') 
# cl.add_employee('Ali') 
# cl.add_employee('Arsen') 
# cl.delete_employee('Numon')

# cl.show_all()





# class Product:
#     def init(self, name, cotegory, price, rate, patern,):
#         self.name = name
#         self.cotegory = cotegory
#         self.price = price
#         self.rate = rate
#         self.patern = patern
#     def info(self):
#         print(self.name,self.cotegory,self.price,self.rate,self.patern)
#     def imeetsy(self):
#         return self.patern>0
#     def discount(self, percent):
#         self.price=self.price-self.price*percent/100
# class Customer:
#     def init(self,name,email, balance):
#         self.name=name
#         self.email=email
#         self.balance=balance
#         self.kupil=[]
#     def add_balance(self, amount):
#         self.balance += amount
#     def buy(self, product):
#         if product.patern>0 and self.balance>=product.price:
#             self.balance-=product.price
#             product.patern-=1
#             self.kupil.append(product.name)
#             print(self.name, "приобрёл", product.name)
# class Store:
#     def init(self, name):
#         self.name = name
#         self.products=[]
#         self.customers=[]
#     def add_product(self, product):
#         self.products.append(product)
#     def add_customer(self,customer):
#         self.customers.append(customer)
#     def show_products(self):
#         for product in self.products:
#             product.info()
#     def find_product(self, name):
#         for product in self.products:
#             if product.name == name:
#                 return product

# store = Store("Tecno")
# product1=Product("Телефон", "(Электроника)",1000,"Оценка-",5)
# product2=Product("Ноутбук", "(Электронника)", 200,"Оценка-",4)
# product3=Product("Наушники", "(Электроника)",300,"Оценка-",4)
# product4=Product("Рюкзак", "(Аксессуары)", 500,"Оценка-",5)
# product5=Product("Чехол", "(Аксессуары)", 150,"Оценка-",3)
# print

# store.add_product(product1)
# store.add_product(product2)
# store.add_product(product3)
# store.add_product(product4)
# store.add_product(product5)
# c1 = Customer("Аlijon", "ali@mail.com", 2000)
# c2 = Customer("Numon", "Numon@mail.com", 5000)
# store.add_customer(c1)
# store.add_customer(c2)

# c1.buy(product1)
# c2.add_balance(300)
# c2.buy(product2)
# product3.discount(10)
# store.show_products()
# print("Покупки Аlijin:", c1.kupil)
# print("Покупки Numon:", c2.kupil)



# //////////////////////////////////////// Home Work ///////////////////////////////////////////////////////

# class Student:
#     school='School number 72'


#     def __init__(self,students,name):
#         self.students=students
#         self.name=name

#     def __len__(self):
#         return len(self.students)

#     def __eq__(self, name2):
#             return self.name==name2


# st=Student(['Ali','Vali'],'Ardesher')
# st2=Student(['Ali','Vali'],'Ardesher')

# print(st==st2)

#2
# class Student:

#     def __init__(self,rakam):
#         self.rakam=rakam

#     def __add__(self, number2):
#         return self.rakam + number2.rakam

# st=Student(6)    
# st2=Student(1)    
# print(st+st2)


#3
# class Student:
#     def __init__(self,students):
#         self.students=students

#     def __getitem__(self, index):
#         return self.students[index]


# st=Student(['Ali','Vali', 'Saidvali'])
# print(st[2])


#4
# class Student:
#     next_id=0
#     Students=[]

#     def create(self,name,age):
#         user={
#             'id':self.next_id,
#             'name':name,
#             'age':age
#         }

#         self.Students.append(user)

#         self.next_id+=1

#     def show_students(self):
#         for i in self.Students:
#             print(i)

#     def update(self,id,new_name):
#         for i in self.Students:
#             if i['id']==id:
#                 i['name']=new_name
#                 return

#         print('user not found')

#     def delete(self,id):
#         for i in self.student:
#             if i['id']==id:
#                 self.students.pop(i['id'])

#     def delete(self,id):
#         for i in self.students:
#             if i['id']==id:
#                 self.students.pop(i['id'])


# st1=Student()
# st1.create('sibhatullo',18)
# st1.create('Arsen',15)
# st1.create('Abduvvahob',17)

# st1.delete(2)

# st1.show_students()

# st1.update(2,'Numon')

# st1.show_students()

# class Book:
#     def delete(self,lib):
#         def delete(lib):

# lib = Library()
# lib.add_book(Book("1984", "George Orwell", 1949))
# lib.add_book(Book.from_string("Animal Farm;George Orwell;1945"))
# lib.add_book(Book("Dune", "Frank Herbert", 1965))
# lib.add_book(Book("1984", "George Orwell", 1950))   
# lib.add_book(Book("Future Book", "Unknown", 3000)) 

# print(len(lib))
# print(lib[0])

# for b in lib.find_by_author("George Orwell"):
#     print(b)

# lib.update_year(3, 1966)
# print(lib[2])

# lib.remove_book(1)
# print(len(lib))
# print(Book.count)

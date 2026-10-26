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
#         if any(isinstance(arg,(in)) and arg<0 for arg in args):
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
#     count = 0

#     def __init__(self, title, author, year):
#         Book.count += 1
#         self.id = Book.count
#         self.title = title
#         self.author = author
#         self.year = int(year)

#     @classmethod
#     def from_string(cls, text):
#         title, author, year = text.split(";")
#         return cls(title, author, int(year))

#     @staticmethod
#     def is_valid_year(year):
#         return 1450 <= year <= 2026

#     def __eq__(self, other):
#         if isinstance(other, Book):
#             return self.title == other.title and self.author == other.author
#         return False

#     def __str__(self):
#         return f"#{self.id} '{self.title}' by {self.author} ({self.year})"


# class Library:
#     def __init__(self):
#         self.books = []

#     def add_book(self, book):
#         if not Book.is_valid_year(book.year):
#             print("Error: invalid year")
#             return False
#         if any(b == book for b in self.books):
#             print("Error: book already exists")
#             return False
#         self.books.append(book)
#         return True

#     def find_by_author(self, author):
#         return [b for b in self.books if b.author == author]

#     def update_year(self, book_id, new_year):
#         if not Book.is_valid_year(new_year):
#             print("Error: invalid year")
#             return False
#         for b in self.books:
#             if b.id == book_id:
#                 b.year = int(new_year)
#                 return True
#         return False

#     def remove_book(self, book_id):
#         self.books = [b for b in self.books if b.id != book_id]

#     def __len__(self):
#         return len(self.books)

#     def __getitem__(self, index):
#         return self.books[index]


# lib = Library()
# lib.add_book(Book("1984", "George Orwell", 1949))
# lib.add_book(Book.from_string("Animal Farm;George Orwell;1945"))
# lib.add_book(Book("Dune", "Frank Herbert", 1965))
# lib.add_book(Book("1984", "George Orwell", 1950))   # дубликат
# lib.add_book(Book("Future Book", "Unknown", 3000))  # неверный год

# print(len(lib))
# print(lib[0])

# for b in lib.find_by_author("George Orwell"):
#     print(b)

# lib.update_year(3, 1966)
# print(lib[2])

# lib.remove_book(1)
# print(len(lib))
# print(Book.count)


# ///////////////////////////////////////////////  Home Work ////////////////////////////////////////////////////////////////////////////

# class Owner:
#     def owner(self):
#         print('Animal has owner')


# class Animal(Owner):
#     def sound(self):
#         print('Animal can make a sound')


# class Speed:
#     def speed(self):
#         print('This is fast')


# class Dog(Animal,Speed):
#     def hello(self):
#         print('This is dog')

# d=Dog()
# d.hello()
# d.sound()
# d.speed()
# d.owner()


# class Cat(Animal):
#     def hello(self):
#         print('This is cat')


# c=Cat()
# c.hello()
# c.sound()
# c.owner()

# class Library:
#     def __init__(self,name,shelf):
#         self.name=name
#         self.shelf=shelf

#     def info(self):
#         print(f'{self.name} -- {self.shelf}')

# l=Library('Kitobxonai milli',12345)
# l.info()

# class Department(Library):
#     def __init__(self, name, shelf,department_name):
#         super().__init__(name, shelf)
#         self.department_name=department_name

#     def malumot(self):
#         print(f'{self.name} -- {self.shelf} -- {self.department_name}')

# d1=Department('Kitobxonai milli',12345,'Classic')

# d1.info()
# d1.malumot()

# class Cat:
#     def hello(self):
#         print('This is cat')


# class Dog(Cat):
#     def hello(self):
#         print('This is Dog')


# class Parrot(Dog):
#     def hello(self):
#         print('This is parrot')

# d=Dog()
# d.hello()

# p=Parrot()
# p.hello()



#1
# class Vehicle:
#     def move(self):
#         print("Транспорт движется")
# class Car(Vehicle):
#     def honk(self):
#         print("Би-би!")
# car=Car()
# car.move()
# car.honk()

#2
# class Employee:
#     def work(self):
#         print("Сотрудник работает")

# class Programmer(Employee):
#     def work(self):
#         print("Пишет код")

# class Teacher(Employee):
#     def work(self):
#         print("Проводит урок")
# employee=Employee()
# programmer=Programmer()
# teacher=Teacher()
# employee.work()
# programmer.work()
# teacher.work()


#3
# class Person:
#     def init(self, name, age):
#         self.name=name
#         self.age=age

# class Student(Person):
#     def __init__(self,name,age,group):
#         super().init(name,age)
#         self.group=group
#     def info(self):
#         print(f"Студент: {self.name},|{self.age} лет,|группа {self.group}")

# s=Student("Али",19,"Python-1")
# s.info()


#4
# class Animal:
#     def speak(self):
#         print("Животное издаёт звук")

# class Cat(Animal):
#     def speak(self):
#         super().speak()
#         print("Мяу")

# my_cat = Cat()
# my_cat.speak()        


#5
# class Device:
#     def power(self):
#         print("Устройство включено")

# class Phone(Device):
#     def call(self, number):
#         print(f"Звоню на номер {number}")


# class Smartphone(Phone):
#     def photo(self):
#         print("Фото сделано")

# my_smartphone = Smartphone()
# my_smartphone.power()
# my_smartphone.call("+992123456789")
# my_smartphone.photo()


#6
# class Flyer:
#     def fly(self):
#         print("Лечу")

# class Swimmer:
#     def swim(self):
#         print("Плыву")

# class Duck(Flyer, Swimmer):
#     def quack(self):
#         print("Кря-кря")


# my_duck = Duck()
# my_duck.fly()
# my_duck.swim()
# my_duck.quack()

# print(Duck.__mro__)

#7
# class User:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email

#     def get_info(self):
#         return f"Имя: {self.name}, Email: {self.email}"


# class Admin(User):
#     def __init__(self, name, email, level):
#         super().__init__(name, email)
#         self.level = level

#     def get_info(self):
#         return f"{super().get_info()}, Уровень: {self.level}"


# class Customer(User):
#     def __init__(self, name, email, balance):
#         super().__init__(name, email)
#         self.balance = balance

#     def get_info(self):
#         return f"{super().get_info()}, Баланс: {self.balance}"


# class Guest(User):
#     def __init__(self, name, email):
#         super().__init__(name, email)

#     def get_info(self):
#         return f"{super().get_info()}, Статус: Гость"

# print(Admin("Али", "ali@mail.tj", 3).get_info())


# ////////////////////////////////////////////// Home Work //////////////////////////////////////////

# class Car:
#     country = 'Tajikistan'

#     def __init__(self,brand,model,prise):
#         self.brand=brand
#         self.model=model
#         self.prise=prise

#     def drive(self):
#         print("Drive")

#     @classmethod
#     def salom(cls):
#         print(f"Salom {cls.country}")

#     @staticmethod
#     def v(a,b):
#         return a + b
#     def __str__(self):
#         return self.company

# car1=Car("BMW", "M5compition", 1000000000000000)
# print(Car.v("salom", "Aleykum"))


#1
# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade

#     def __str__(self):
#         return (f"Студент: {self.name}, Возраст: {self.age}, Оценка: {self.grade}")

# student1 = Student("Ali", 20, "3")
# student2 = Student("Vali", 22, "4")
# student3 = Student("Saidvali", 19, "5")

# print(student1)
# print(student2)
# print(student3)

#2
# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

#     def display_info(self):
#         print(f"Автомобиль: {self.brand} {self.model}, Год выпуска: {self.year}")

# car1 = Car("Toyota", "Camry", 2022)
# car2 = Car("BMW", "X5", 2024)
# car3 = Car("Tesla", "Model", 2023)

# car1.display_info()
# car2.display_info()
# car3.display_info()

#3
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def calculate(self):
#         return self.width * self.height

#     def calculate_perimeter(self):
#         return 2 * (self.width + self.height)

# rect = Rectangle(5, 10)

# print(f"Прямоугольник со сторонами: {rect.width} x {rect.height}")
# print(f"Площадь: {rect.calculate()}")
# print(f"Периметр: {rect.calculate_perimeter()}")

#4
# class BankAccount:
#     def __init__(self, owner, balance=0.0):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"Счет пополнен на {amount}. Текущий баланс: {self.balance}")
#         else:
#             print("Сумма пополнения должна быть положительной.")

#     def withdraw(self, amount):
#         if 0 < amount <= self.balance:
#             self.balance -= amount
#             print(f"Снято {amount}. Остаток на счете: {self.balance}")
#         else:
#             print("Ошибка: недостаточно средств или неверная сумма.")

#     def display_info(self):
#         print(f"Владелец счета: {self.owner}, Баланс: {self.balance} руб.")

# my_account = BankAccount("Алексей", 5000.0)

# my_account.display_info()
# my_account.deposit(2000)
# my_account.withdraw(1500)
# my_account.withdraw(10000)
# my_account.display_info()


#5
# class BankAccount:
#     def __init__(self, owner, balance=0.0):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"Счет пополнен на {amount}. Текущий баланс: {self.balance}")
#         else:
#             print("Ошибка: сумма пополнения должна быть положительной.")

#     def withdraw(self, amount):
#         if amount <= 0:
#             print("Ошибка: сумма для снятия должна быть положительной.")
#         elif amount > self.balance:
#             print(f"Отказано в снятии: запрошено {amount}, но на балансе только {self.balance}.")
#         else:
#             self.balance -= amount
#             print(f"Успешно снято: {amount}. Остаток на счете: {self.balance}")

#     def display_balance(self):
#         print(f"Владелец счета: {self.owner} | Баланс: {self.balance}")

# account = BankAccount("Ali", 5000.0)
# account.display_balance()
# account.deposit(1500)
# account.withdraw(2000)
# account.withdraw(10000)
# account.display_balance()

#6
# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def eat(self):
#         print(f"{self.name} кушает.")

# class Dog(Animal):
#     def bark(self):
#         print(f"{self.name} громко лает: Гав-гав!")

# class Cat(Animal):
#     def purr(self):
#         print(f"{self.name} сладко мурлычет: Мур-мур...")

# class Bird(Animal):
#     def sing(self):
#         print(f"{self.name} красиво поёт на ветке.")

# dog = Dog("Сабака", 3)
# cat = Cat("Кошка", 2)
# bird = Bird("птица", 1)

# dog.eat()
# cat.eat()
# bird.eat()

# print("-" * 30)

# dog.bark()
# cat.purr()
# bird.sing()

#7
# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def display_info(self):
#         print(f"Товар: {self.name} — {self.price} руб.")


# class Order:
#     def __init__(self, customer_name):
#         self.customer_name = customer_name
#         self.products = []  # Список товаров в заказе

#     def add_product(self, product):
#         self.products.append(product)
#         print(f"Товар «{product.name}» добавлен в заказ {self.customer_name}.")

#     def calculate_total(self):
#         total = sum(product.price for product in self.products)
#         return total

#     def display_order(self):
#         print(f"\n--- Заказ клиента: {self.customer_name} ---")
#         if not self.products:
#             print("Заказ пуст.")
#         else:
#             for item in self.products:
#                 print(f"- {item.name}: {item.price} руб.")
#             print(f"Итого к оплате: {self.calculate_total()} руб.")


# p1 = Product("Клавиатура", 3500)
# p2 = Product("Мышь", 1800)
# p3 = Product("Монитор", 22000)

# my_order = Order("Дмитрий")
# my_order.add_product(p1)
# my_order.add_product(p2)
# my_order.add_product(p3)
# my_order.display_order()

#8
# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

#     def display_info(self):
#         print(f"«{self.title}» — {self.author}")


# class Library:
#     def __init__(self, name):
#         self.name = name
#         self.books = []

#     def add_book(self, book):
#         self.books.append(book)
#         print(f"Книга «{book.title}» добавлена в библиотеку «{self.name}».")

#     def find_by_author(self, author):
#         print(f"\nПоиск книг автора {author}:")
#         found_books = [book for book in self.books if book.author.lower() == author.lower()]
        
#         if found_books:
#             for book in found_books:
#                 book.display_info()
#         else:
#             print("Книги этого автора не найдены.")

#     def display_all_books(self):
#         print(f"\n--- Список книг библиотеки «{self.name}» ---")
#         if not self.books:
#             print("Библиотека пуста.")
#         else:
#             for book in self.books:
#                 book.display_info()

# library = Library("Городская библиотека")

# b1 = Book("Преступление и наказание", "Фёдор Достоевский")
# b2 = Book("Идиот", "Фёдор Достоевский")
# b3 = Book("Война и мир", "Лев Толстой")

# library.add_book(b1)
# library.add_book(b2)
# library.add_book(b3)

# library.display_all_books()
# library.find_by_author("Фёдор Достоевский")

#9
# from abc import ABC, abstractmethod

# class Payment(ABC):
#     @abstractmethod
#     def process_payment(self, amount):
#         pass


# class CreditCardPayment(Payment):
#     def __init__(self, card_number):
#         self.card_number = card_number

#     def process_payment(self, amount):
#         print(f"Списание {amount} руб. с банковской карты (**** {self.card_number[-4:]}). Успешно!")


# class PayPalPayment(Payment):
#     def __init__(self, email):
#         self.email = email

#     def process_payment(self, amount):
#         print(f"Списание {amount} руб. через аккаунт PayPal ({self.email}). Успешно!")


# class CryptoPayment(Payment):
#     def __init__(self, wallet_address):
#         self.wallet_address = wallet_address

#     def process_payment(self, amount):
#         print(f"Транзакция на сумму {amount} руб. отправлена на криптокошелек ({self.wallet_address[:6]}...). Ожидает подтверждения сети.")


# def make_payment(payment_method, amount):
#     print("Инициализация платежа...")
#     payment_method.process_payment(amount)
#     print("-" * 40)

# card = CreditCardPayment("4276380012345678")
# paypal = PayPalPayment("user@example.com")
# crypto = CryptoPayment("0x12345abcdef7890")

# make_payment(card, 1500)
# make_payment(paypal, 3200)
# make_payment(crypto, 10500)

#10
# class Product:
#     def init(self, name, price):
#         self.name = name
#         self.price = price


# class Electronics(Product):
#     def init(self, name, price, warranty_years):
#         super().init(name, price)
#         self.warranty_years = warranty_years


# class Clothing(Product):
#     def init(self, name, price, size):
#         super().init(name, price)
#         self.size = size


# class Food(Product):
#     def init(self, name, price, expiration_date):
#         super().init(name, price)
#         self.expiration_date = expiration_date



# products = [
#     Electronics("Smartphone", 599.99, 2),
#     Clothing("T-shirt", 19.99, "M"),
#     Food("Chocolate", 1.99, "2026-12-31"),
# ]

# for product in products:
#     print(f"{product.name}: ${product.price}")

#11
# class Dog:
#     def make_sound(self):
#         return "Woof!"


# class Cat:
#     def make_sound(self):
#         return "Meow!"


# class Cow:
#     def make_sound(self):
#         return "Moo!"


# animals = [Dog(), Cat(), Cow()]

# for animal in animals:
#     print(animal.make_sound())

#12
# # class CashPayment:
#     def pay(self, amount):
#         return f"Paid {amount} in cash."


# class CardPayment:
#     def pay(self, amount):
#         return f"Paid {amount} by card."


# class OnlinePayment:
#     def pay(self, amount):
#         return f"Paid {amount} online."


# def process_payment(payment, amount):
#     print(payment.pay(amount))


# payments = [CashPayment(), CardPayment(), OnlinePayment()]

# for payment in payments:
#     process_payment(payment, 100)
#13
# import math

# class Circle:
#     def init(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * self.radius ** 2


# class Rectangle:
#     def init(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height


# class Triangle:
#     def init(self, base, height):
#         self.base = base
#         self.height = height

#     def area(self):
#         return 0.5 * self.base * self.height


# shapes = [
#     Circle(5),
#     Rectangle(4, 6),
#     Triangle(3, 8)
# ]

# for shape in shapes:
#     print(shape.area())
#14
# class Car:
#     def move(self):
#         return "The car drives on the road."


# class Bicycle:
#     def move(self):
#         return "The bicycle rides on the road."


# class Airplane:
#     def move(self):
#         return "The airplane flies through the sky."


# def start_moving(transport):
#     print(transport.move())


# transports = [Car(), Bicycle(), Airplane()]

# for transport in transports:
#     start_moving(transport)
#15
# class EmailNotification:
#     def send(self, message):
#         print(f"Email: {message}")


# class SMSNotification:
#     def send(self, message):
#         print(f"SMS: {message}")


# class PushNotification:
#     def send(self, message):
#         print(f"Push notification: {message}")


# def send_notification(notification, message):
#     notification.send(message)


# send_notification(EmailNotification(), "Your order has shipped.")
# send_notification(SMSNotification(), "Your order has shipped.")
# send_notification(PushNotification(), "Your order has shipped.")






#////////////////////////////////////////// Home Work /////////////////////////////////////////////
# #1
# class Student:
#     def __init__(self,grade):
#         self.__grade=grade
#     def getter(self):
#         return self.__grade
#     def setter(self,new_gropes):
#         if new_gropes>0 and new_gropes<-100:
#             return




#1
# class Book:
#     def __init__(self, title, pages):
#         self.__title = title
#         self.__pages = 0
#         self.set_pages(pages)

#     def get_title(self):
#         return self.__title

#     def get_pages(self):
#         return self.__pages

#     def set_pages(self, pages):
#         if pages > 0:
#             self.__pages = pages
#         else:
#             print("nodurust: бояд аз 0 калон бошад.")


# book1 = Book("дуруст", 500)
# print(book1.get_title()) 
# print(book1.get_pages())  

# book1.set_pages(-10)      
# print(book1.get_pages()) 
            
#2
# class Dog:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age=0
#         self.set_age(age)

#     def get_name(self):
#         return self.__name
    
#     def get_age(self):
#      return self.__age

#     def set_age(self, age):
#         if 0 <= age <= 30:
#             self.__age = age
# d=Dog("Sag",5)
# print(d.get_name())
# print(d.get_age())


#3
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     @property
#     def width(self):
#         return self.__width

#     @width.setter
#     def width(self, value):
#         if value <= 0:
#             raise ValueError("Бар (width) бояд адади мусбат бошад!")
#         self.__width = value

#     @property
#     def height(self):
#         return self.__height

#     @height.setter
#     def height(self, value):
#         if value <= 0:
#             raise ValueError("Баландӣ (height) бояд адади мусбат бошад!")
#         self.__height = value

#     def area(self):
#         return self.__width * self.__height


# if __name__ == "__main__":
#     rect = Rectangle(4.0, 5.0)
#     print(f"Масоҳат: {rect.area()}")    


#4
# class Counter:
#     def __init__(self, count: int = 0):
#         self.__count = max(0, count)

#     def increment(self):
#         self.__count += 1

#     def decrement(self):
#         if self.__count > 0:
#             self.__count -= 1

#     def get_count(self):
#         return self.__count

# c = Counter()
# print(c.get_count())  

# c.decrement()        
# print(c.get_count())   

# c.increment()
# c.increment()
# print(c.get_count())   

# c.decrement()
# print(c.get_count())   
        

#5
# class Counter:
#     def init(self):
#         self.count = 0

#     def increment(self):
#         self.__count += 1

#     def decrement(self):
#         if self.__count > 0:
#             self.__count -= 1

#     def get_count(self):
#         return self.__count

# counter = Counter()

# counter.increment()
# counter.increment()
# print(counter.get_count())

# counter.decrement()
# print(counter.get_count())  

# counter.decrement()
# counter.decrement()
# print(counter.get_count())
#6
# class Light:
#     def __init(self):
#         self.is_on = False

#     def turn_on(self):
#         self.__is_on = True

#     def turn_off(self):
#         self.__is_on = False

#     def is_on(self):
#         return self.__is_on


# light = Light()
# print(light.is_on())

# light.turn_on()
# print(light.is_on())

# light.turn_off()
# print(light.is_on())


#7
# class Wallet:
#     def __init(self):
#         self.money = 0

#     def add_money(self, amount):
#         if amount > 0:
#             self.__money += amount

#     def spend_money(self, amount):
#         if 0 < amount <= self.__money:
#             self.__money -= amount

#     def get_money(self):
#         return self.__money


# wallet = Wallet()
# wallet.add_money(100)
# wallet.spend_money(30)
# print(wallet.get_money())


#8
# class Square:
#     def __init(self, side):
#         if side <= 0:
#             raise ValueError("Tarafosh ziyod bosha")
#         self.side = side

#     def get_side(self):
#         return self.__side

#     def set_side(self, side):
#         if side <= 0:
#             raise ValueError("Tarafosh ziyod bosha")
#         self.__side = side

#     def get_area(self):
#         return self.__side ** 2


# square = Square(5)
# print(square.get_side())
# print(square.get_area())

# square.set_side(3)
# print(square.get_area())

#9
# class Phone:
#     def __init(self):
#         self.battery = 0

#     def charge(self, amount):
#         self.__battery = min(100, max(0, self.__battery + amount))

#     def use(self, amount):
#         self.__battery = min(100, max(0, self.__battery - amount))

#     def get_battery(self):
#         return self.__battery


# phone = Phone()
# phone.charge(70)
# print(phone.get_battery())

# phone.use(25)
# print(phone.get_battery())

# phone.charge(80)
# print(phone.get_battery())
#10
# class User:
#     def __init(self, password):
#         self.set_password(password)

#     def set_password(self, password):
#         if not isinstance(password, str) or len(password) < 6:
#             raise ValueError("Boyad ay 6 raqam ziyod bosha")
#         self.password = password

#     def check_password(self, p):
#         return self.__password == p


# user = User("secret123")
# print(user.check_password("secret123"))
# print(user.check_password("wrong"))


#11
# class Thermostat:
#     def __init(self, target):
#         self.set_target(target)

#13
# class Employee:
#     def __init__(self, salary):
#         self.salary = salary

#     @property
#     def salary(self):
#         return self.__salary

#     @salary.setter
#     def salary(self, value):
#         if value < 0:
#             print("оилик аз 0 кам намешавад!")
#             self.__salary 
#         else:
#             self.__salary = value

#     def raise_salary(self, percent):
#         self.salary += self.__salary * (percent / 100)


# lst = Employee(100)
# lst.raise_salary(12) 
# print(lst.salary)    



#     def get_target(self):
#         return self.target

#     def set_target(self, value):
#         if not 10 <= value <= 30:
#             raise ValueError("Temperatura ay 10 to 30 bosha")
#         self.__target = value


# thermostat = Thermostat(22)
# print(thermostat.get_target())

# thermostat.set_target(25)
# print(thermostat.get_target())

#14
# class Car:
#     def __init(self,speed):
#         self.speed = speed
        
#     def accelerate(self,speed):
#         if speed > 200: 
#             return "Stop"
#         return"Run"     
    
#     def brake(self,n):
#         if n > 0 and n <= 200:
#             self.__speed = n
#             return True
#         return False
    
# d = Car(150)
# print(d.accelerate(150))
# print(d.brake(150))

#15
# class Employee:
#     def __init(self, salary):
#         self.set_salary(salary)

#     def get_salary(self):
#         return self.__salary

#     def set_salary(self, salary):
#         if salary < 0:
#             raise ValueError("Pl nest")
#         self.__salary = salary

#     def raise_salary(self, percent):
#         if percent > 0:
#             self.__salary += self.__salary * percent / 100


# employee = Employee(500)
# print(employee.get_salary())

# employee.raise_salary(10)
# print(employee.get_salary())



### 1 Question


# Дар бораи рекурсия нависед. 

# Ин қисми функсия аст ки функсия бо худаш даъват мекунад то ба натиҷаи охирин расад


### 3 Question
# Контейнерҳоро ба хотир оварда онҳоро нависед. 

# 1. list 
# мисол 
# my_list = [1, 2, 3, 4,]
# print(my_list)

# 2. tuples
# мисол
# my_tuples = (1, 2, 3, 4)
# print(my_tuples)

# 3. Dictionaries

# my_dict = {
#     "key1": "value1",
#     "key2": "value2"
#  }
# print(my_dict)

# 4. Sets
# my_set = {1, 2, 3, 4}
# print(my_set)


### 5 Question
# Кадом методҳои модули datetime ва randome - ро медонед. Бо мисолҳо фаҳмонед.

# datetime.now() - Вакти ҳозираро мегирад
# datetime.date.today() - Санаи хозираро мегирад

# random.randint(a, b) - Адади тасодуфи байни a ва b мегирад
# random.choice(seq) - Элементи тасодуфи аз руйхати дода шуда мегирад



# task 1

# a =float(input("Enter the amount in TJS:"))
    
# R = 8.33
# U = 0.094
# E = 0.084
# uz = 1000

# rub = R * a 
# Usd = U * a
# eur = E * a
# Uzb = uz * a
# print("Rub ->",rub)
# print("USD ->",Usd)
# print("EUR ->",eur)
# print("Uzb_SUM ->",Uzb)




### 2 Question
# Closure(Замыкания) - ро бо мисолҳо фаҳмонед.

# def make_counter():
#     count = 0

#     def counter():
#         nonlocal count
#         count += 1
#         return count

#     return counter

# counter = make_counter()
# print(counter())  
# print(counter())  
# print(counter())








# task 3

# def create(name1):
#     def concatenates(name2):
#         return f"{name2} {name1}"
#     return concatenates

# name1 = input()
# name2 = "Welcome to Softclub"

# closure = create(name1)
# res = closure(name2)
# print(res)


# task 4

# def find_min(lst):
    
#     if len(lst) == 1:
#         return lst[0]
    
#     else:
#         return min(lst[0], find_min(lst[1:]))

# numbers = [2, 3, 54, 2, 4, 1, 5, 3, 2, 54]
# print(find_min(numbers))  


# task 5



# def power(a):
#     if a == 1:
#         return 1
#     else:
#         return a * a + power(a - 1)


# a = int(input())
# print(power(a))  



# task 8

# def sum_series(N):
    
#     sum_result = 1.0
#     factorial = 1.0
    
    
#     for i in range(1, N + 1):
#         factorial *= i  
#         sum_result += 1 / factorial  
    
#     return round(sum_result, 5)

# N = int(input())
# res = sum_series(N)
# print(res)



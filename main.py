numbers = [5,1,5,1,1]
for x_count in numbers:
  output = ''
  for count in range(x_count):
    output = output + 'x'
  print(output)


numbers = [20, 30, 200, 50, 60, 10, 1, 100]
max_num = numbers[0]
for number in numbers:
  if number > max_num:
     max_num = number
print(max_num)


matrix = [
    [10, 20, 30],
    [30, 34, 36],
    [46, 48, 50]
]
print(matrix[2][1])


phone = input('Phone: ')
in_words = {0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
for number in phone:
  print(in_words[int(number)], end = ' ')

def emoji_converter(message):
    msg = message.split(' ')
    dict_emojis = {':)': '🙂', ':(': '☹️', ':|': '😐', ';)': '😉'}
    output = ''
    for word in msg:
        output += dict_emojis.get(word, word) + ' '
    return output

my_message = input('msg> ')
print(emoji_converter(my_message))


def my_intro(my_name, my_age):
    print("hi ", my_name, my_age)

my_intro("kiran", 55)
my_intro("Ramya", 88)


def school_details(my_name, standard, roll_no):
   print(f'Iam {my_name} studying in {standard} std. My roll no is {roll_no}')
school_details('Ramya', '10', '21')


name = input('What is your name? ').capitalize()
favorite_color = input('Favorite color? ').capitalize()
print(name, 'likes', favorite_color)


anniversary = input('Anniversary year: ')
year = 2023 - int(anniversary)
print('Happy', year, 'annivarsary.')
print(2023 - int(input('Anniversary year: ')))


weight_lbs = input('Weight(lbs): ')
print(int(weight_lbs) * 0.45)


name = 'RAMYA'
print(name[1:-1])

h = 'Hello'
name = 'Ram'
age = 20
favorite_color = 'blue'
print(f"{h} myself {name}. Iam {age} year's old.")


intro = 'Hello! have a great day'
print(len(intro))
print(intro[10])
print(intro[:20])
print(len(intro[2:-3]))
print(intro[0:].upper())
print(intro.find('g'))
print(intro.find('have'))
print(intro.replace('have', 'I had'))
print(intro.replace('Hello! ', ''))
print('have' in intro)
print('Had' in intro)
print(intro.title())


print(100+3)
print(100-3)
print(100/3)
print(100//3)
print(100 % 3)
print(10 * 3)
print(10 ** 3)


x = 100
x = x + 3
print(x + 3)
x += 3
print(x)


price = 1000000
has_good_credit = False
if has_good_credit:
   down_payment = price * 0.1
else:
   down_payment = price * 0.2
print(f'down payment: {down_payment}')


has_high_income = True
has_good_credit = False
if has_high_income and has_good_credit:
   print('Eligible for loan')
else:
  print('Not eligible for loan')


has_high_income = True
has_good_credit = True
if not has_high_income and not has_good_credit:
  print('Not eligible for loan')
else:
  print('Eligible for loan')


temp = input('Temperature: ')
if temp > '30':
  print("It's a hot day")
elif temp < '30':
  print("It's a cold day")
else:
   print("It's neithor a hot nor a cold day")


name = input('Name: ')
if len(name) < 3:
   print('name must be aleast 3 character long')
elif len(name) > 50:
  print('name must be not more than 50 character long')
else:
  print('name looks good')


weight = int(input('Weight: '))
unit = input('in (lb) or (kg): ')
if unit == 'lb':
    weight_lb = (weight) * 0.45
    print(f'You are {weight} kilos.')
elif unit == 'kg':
    weight_kg = (weight) / 0.45
    print(f'You are {weight} pounds.')


i = int(input('i: '))
while i > 10:
  print('*' * i)
  i = i - 2
print('done')


secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You won')
        break
else:
  print('Sorry you failed')


letters = ['a', 'b', 'c', 'd']
numbers = [5, 6, 1, 10, 2, 0, 4, 8, 9, 3, 7]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
print(type(numbers))

numbers.append(22)
print(numbers)

numbers.extend([11, 12, 13, 15, 16])
print(numbers)

print(numbers.index(4))
print(letters.index('b'))

print(max(numbers))
print(min(numbers))

print(len(numbers))
print('length of numbers is', len(numbers))

numbers.clear()
print(numbers)

numbers.insert(3, 10)
print(numbers)

print(numbers.count(10))

numbers.remove(10)
print(numbers)

numbers.pop(3)
print(numbers)

letters.reverse()
print(letters)

letter_index = letters.index('a')
print(letter_index)


lists = ['apple', 'banana', 'strawberry', 'orange', 'kiwi']
letters = 'a, b, c, d, e, f, g, h, i'
numbers = [-3, -2, -1, 0, 1, 2, 3]
print(f'{letters} is an alphabet but {numbers} are numbers.')


dictionary = dict(name='Ramya', age=22, gender='female' )
d = {"ff":3, "gg":432}
a = 1, 2, 3
print(a)


def kk(name, **x):
    print(x)
    print(name)

kk(age=5, name=88,ll=98897)


def kk(a, b, *c):
    print(a, b, *c)

kk(1,2,3,4,5)


for z in range(0, 10):
    space = ' ' * z
    print(space + (9 - z) * ' *')


def palindrome(z):
    b = z[::-1]
    if z == b:
         return True
    else:
         return False
y = palindrome('ramya')
print(y)
a = 'apple'
print(palindrome('malayalam'))
print(palindrome('ramya'))


def fun(x):
    reverse_a = a[::-1]
    if a == reverse_a:
        return True
    else:
        return False
y = fun(a)
print(y)


a = [1, 2, 3, 4, 5]
y = 1
for x in a:
    y = x * y
print(y)


b = {1,2,3,4,5}
print(sum(b))

c = 1,2,3,4,5
print(sum(c))

d = (1,2,3,4,5)
print(sum(d))


name = 'my name Is Ramya'
print(name.upper())
print(name.lower())
print(name.casefold())
print(name.title())
print(name.capitalize())
b = name.replace('Ramya', 'Kiran')
print(b)


def myfun(x):
    unique = set(x)
    z = sum(unique)
    return z
a = myfun(y)
print(a)


my = [1,2,3,3,2,1,1,5,8]
unique = set(my)
print(set(my))
y = sum(unique)
print(y)
text = ['kiran', 'kharvi']
text1 = set(text)
print(text1)


# 1
# 1 2
# 1 2 3
# 1 2 3 4 5


def fun():
    b = ''
    for x in range(1,6):
         b = b + ' ' + str(x)
         print(b)
fun()


def fun(x, y):
    for item in x:
        if y == item:
            return True
    return False
c = fun([1,2,3,4,5], 2)
print(c)


def fun():
    for x in num:
        if x > 0:
            print(x)
fun()

num = [2,11,12,14,1,9,22]


def fun(x):
    min_num = 100
    for y in x:
        if y < min_num:
            min_num = y
    return min_num
z = fun(num)
print(z)


a = int(input('number: '))
while a != 0:
    print('$')
    a = int(input('number: '))
    break


a = 'None'
while a:
    print('$')
word = {'name':'Ramya', 'age': 20, 'place': 'kundapur'}
for x,y in word.items():
    print(x,y)


for x in range(1,5):
    print(x, ' ')
    for y in range(x):
        print(y,end=' ')


for x in range(1,6):
    for y in range(x):
        print(x,end='')
    print()


for ooo in range(3):
    for a in range(1,6):
        print(a,end='')
    print()


def fun(a):
    for b in range(1,a+1):
        for c in range(b):
            print(b,end='')
        print()
fun(9)


def fun():
    b = int(input('number: '))
    while b != 0:
        if b % 2 == 0:
            print('number is even')
        else:
            print('number is odd')
        b = int(input('new number: '))
    if b == 0:
        print('number is neither even nor odd')

fun()


def fun():
    z = 1
    while z != 0:
        a = float(input('Enter number 1: '))
        b = float(input('Enter number 2: '))
        c = int(input('[Enter 1 if add; 2 if subtract; 3 if divide; 4 if multiply]\nOperator: '))
        if c == 1:
            print(f'\nans= {a + b}')
        elif c == 2:
            print(f'\nans = {a - b}')
        elif c == 3 and b != 0:
            print(f'\nans = {a / b}')
        elif c == 4:
            print(f'\nans = {a * b}')
        elif c > 4:
            print('\nSorry, the operator can be 1 or 2 or 3 or 4')
        else:
            print('\nSorry, the answer is not defined')
        z = int(input('\n[Enter 1 if yes: 0 if No]\nDo you want to continue?: '))
    print('\nCompleted')


def fun(a):
    for b in range(1,a+1):
        for c in range(b):
            print(b, end=' ')
        print()

fun(5)


# TO GET '#' IN 4 TIMES IN 4 LINES:
def fun(x):
    for a in range (4):
        for y in range(4):
            print('#',end=' ')
        print()

fun(4)


r = 2 ** 3 ** 4
print(r)
print(2 ** 81)

# pass by reference


def fun_1(a):
    a = 3
    print(id(a), 'inside', a)


a = 1
print(id(a), 'before', a)
fun_1(a)
print(id(a), 'after', a)

print()


def fun_2(b):
    b.append(25)
    print(id(b), 'inside', b)


b = [10, 20, 30]
print(id(b), 'before', b)
fun_2(b)
print(id(b), 'after', b)

def fun_2(val):
    z = val + [50]
    print(val)


def fun(val):
    b = val.append(30)
    a = val.pop()
    print(a)

n = [10]
print(n)

fun_2(n)
fun(n)
print(n)


def fun(a):
    count_even = count_odd = 0
    for x in a:
        if x % 2 == 0:
            count_even += 1
        else:
            count_odd = count_odd + 1
    return count_even, count_odd

numbers = [1,2,4,6,5,3,7]
y, z = fun(numbers)
print('Even =', y)
print('Odd =', z)


def fun(a):
    a.append(3)
num = [1,2]
fun(num)
print(num)


# list indexing
num = [1,2,3,4,5,6,7,8,9,10]
print(num[0:5][::-1])
print(num[5:])


  # Nested list
x = [1,2,3,[4,5,6,[7,8,9]]]
print(x[3][3][1])


t = [(1,9),(3,4),(3,5)]
t.sort(key=lambda x: x[1])
print(t)


d = {'name': 'Ramya', 'age': 20, 'place': 'kpur'}
l_num = ['a','b','c','a','d','e','b','c']
def fun_num(a):
    b = {}
    for x in a:
        if x in b:
            b[x] = b[x] + 1
        else:
            b[x] = 1
    y = sorted(b.items(), key=lambda x: x[1])
    return dict(y)

r = fun_num(l_num)
print(r)


m = 'My name is Ramya'
def fun(a, b):
    if b in a:
        y = a.find(b)
        z = y + len(b) - 1
        return True
fun(m,'Ramya')

a = ['R','a','R','l','o',' ','I','a','m',' ', 'R','a','m','y','a']
b = 'Ramya'


def fun(a,b):
    i = -1
    for x in a:
        flag = True
        i = i + 1
        if x == b[0]:
            next_index = i + 1
            for y in b[1:]:
                if a[next_index] == y:
                    next_index = next_index + 1
                else:
                    flag = False
                    break
            if flag:
                return i,next_index - 1
    return 'b is not in the list a'

z = fun(a,b)
print(z)


# STACK
l_num = []
def fun(a):
    q1 = 1
    n = 5
    while q1 == 1:
        q2 = int(input('Do you want to add or remove item? [Enter 1 to add; 0 to remove]: '))
        if q2 == 1:
            if len(a) == n:
                print('Stack is full')
            else:
                q3 = input('Number: ')
                a.append(q3)
        elif q2 == 0:
            if len(a) == 0:
                print('Stack is empty')
            else:
                a.pop()
        else:
            print('Please enter either 0 or 1')
        print(a)
        q1 = int(input('Do you want to proceed? [Enter 1 for Yes, 0 for No]: '))
    if q1 == 0:
        print('Done')
    else:
        print('Please enter either 0 or 1')
        fun(l_num)
    return a

result = fun(l_num)
print(result)


# QUEUE
l_num = []
def fun(a):
    n = 5
    q1 = 1
    while q1 == 1:
        q2 = int(input('Do you want to add or remove item? [Enter 1 to add; 0 to remove]: '))
        if q2 == 1:
            if len(a) == n:
                print('Queue is full')
            else:
                q3 = input('Number: ')
                a.append(q3)
        elif q2 == 0:
            if len(a) == 0:
                print('Queue is empty')
            else:
                a.pop(0)
        else:
            print('Please enter either 0 or 1')
        print(a)
        q1 = int(input('Do you want to proceed? [Enter 1 for Yes, 0 for No]: '))
    if q1 == 0:
        print('Done')
    else:
        print('Please enter either 0 or 1')
        fun(l_num)
    return a

result = fun(l_num)
print(result)


def fun(a,b):
    try:
        c = a / b
    except Exception as ramya:
        print(ramya)
    else:
        print('Nothing is wrong')
        print(c)
fun(2,0)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


class A(object):
    def __init__(self, something):
        print("A init called")
        self.something = something

class B(A):
    def __init__(self, something):
        # Calling init of parent class
        A.__init__(self, something)
        print("B init called")
        self.something = something

obj = B("Something")


class BasicClass:
    theVariable = 1

class ExampleClass:
    age = 22
    name = 'Ramya'
    place = 'Kundapura'

x = ExampleClass()
print(x.name,x.age,x.place)


class BirthdayBoy(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        print(id(self.age))
        self.age = self.age + 1
        print(id(self.age))

x = BirthdayBoy('Ramya')

print(x.age)
print(id(x.age))
x.birthday()
print(id(x.age))

print(x.age)


class Salesperson:
    sales = 0
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname

    def makesale(self, value):
        self.sales = self.sales + value

    def salesreport(self):
        print(f'My total sales are {self.sales}!')

x = Salesperson('Ramya', 'Kharvi')
x.makesale(500)
x.salesreport()


class Vehicle:
    def __init__(self,maxspeed,mileage):
        self.maxspeed = maxspeed
        self.mileage = mileage

x = Vehicle(200, 20)
print(x.maxspeed, x.mileage)


class Vehicle:
    def __init__(self,name,maxspeed,mileage):
        self.name = name
        self.maxspeed = maxspeed
        self.mileage = mileage

class Bus(Vehicle):
    pass

a = Vehicle('School vehicle',250,25)
b = Bus('School Volvo',180, 12)
print(f'Vehicle Name:{b.name}\nSpeed: {b.maxspeed}\nMileage: {b.mileage}')


class Vehicle:
    color = 'White'
    def __init__(self,name,maxspeed,mileage):
        self.name = name
        self.maxspeed = maxspeed
        self.mileage = mileage

class bus(Vehicle):
    pass

class car(Vehicle):
    pass

class bike(Vehicle):
    pass

b = bus('School Volvo', 240, 25)
c = car('BMW', 300, 30)
d = bike('Royal Enfield', 260, 28)

print(f'Vehicle Name: {b.name}, Color: {b.color}, Maxspeed: {b.maxspeed}, Mileage: {b.mileage}')
print(f'Vehicle Name: {c.name}, Color: {c.color}, Maxspeed: {c.maxspeed}, Mileage: {c.mileage}')
print(f'Vehicle Name: {d.name}, Color: {d.color}, Maxspeed: {d.maxspeed}, Mileage: {d.mileage}')


class Vehicle:
    def __init__(self, name):
        self.name = name

    def seating_capacity(self, capacity):
        self.fare_charge = capacity * 100

    def fare(self):
        pass

class Bus(Vehicle):
    def fare(self):
        maintainance_charge = self.fare_charge + 0.1
        final_amount = maintainance_charge + 0.1

a = Vehicle('school vehicle')
a.seating_capacity(200)


class Vehicle:
    def __init__(self, name,maxspeed,mileage):
        self.name = name
        self.maxspeed =maxspeed
        self.mileage = mileage

    def seating_capacity(self,capacity):
        self.capacity = capacity

class Bus(Vehicle):
    pass

a = Vehicle
b = Vehicle('Volvo', 200, 18)
b.seating_capacity(55)
print(b.capacity)
print(f'The seating capacity of {b.name} is {b.capacity} passengers')


class A:
    def __init__(self):
        self.__name = "Kiran"

    def update_name(self, new_name):
        self.__name = new_name

    def dis(self):
        print(self.__name)

class B(A):
    pass


x = B()
x.dis()
x.update_name("ramya")
x.dis()

list_range = list(range(1,101))


def filter_list_by_multiple_of_given_num(x,y):
    return list(filter(lambda z: z % y == 0, x))
new_list = filter_list_by_multiple_of_given_num(list_range,3)
print(new_list)

print('NEWEST')
newest_list = list(filter(lambda x: x % 4 == 0,list_range))
print(newest_list)


# FILTER
#
set_range = set(range(1,51))

divisible_by_3 = set(filter(lambda x:x % 3 == 0,set_range))

print(divisible_by_3)


# # MAP
tup_num = (2,4,10,33,21,40,34,56,71,23,45,61,90)

multiply_by3 = tuple(map(lambda x: x*3,tup_num))
print(multiply_by3)


# REDUCE
from functools import reduce

new_list = [20,34,2,1,6,7,8,9,98,65,30]

subtract = reduce(lambda a,b: b-a,new_list)
print(subtract)


# filter
list_num = [2,33,4,61,72,51,11,1,40,20,60]

divisible_by2 = list(filter(lambda x : x % 2 == 0,list_num))

print(divisible_by2)


# map
sub_list_by2 = list(map(lambda x: x-2,divisible_by2))

print(sub_list_by2)


# reduce
from functools import reduce

multiply_num = reduce(lambda x,y: y-x,sub_list_by2)
print(multiply_num)

list_range = list(range(50,201))

filter_multiple_of_10 = list(filter(lambda x:(x + 2) % 10 == 0,list_range))

print(filter_multiple_of_10)

map_divide_by2 = list(map(lambda x: x//2,filter_multiple_of_10))

print(map_divide_by2)

from functools import reduce

reduce_by_adding = reduce(lambda x,y: x*y, [2,3], 5)

print(reduce_by_adding)


class Student:
    def __init__(self,name,age,std,roll_no):
        self.name = name
        self.age = age
        self.std = std
        self.roll_no = roll_no

    def height(self):
        pass

    def weight(self):
        pass


stud = Student('Ramya', 22, 'BSc 3rd year', 21)
print(stud.name, stud.age, stud.std, stud.roll_no)

stud.height()
stud.weight()


# Public
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def krishna(self):
        print('Inside class ', self.name,'Age ', self.age)


class Student(Person):

    def Ramya(self):
        print('Within class', self.name, self.age)

per1 = Person('Krishna', 60)
stud = Student('Ramya', 23)


per1.krishna()
stud.Ramya()

print('Outside class', per1.age)

print()


# Protected
class Person:
    def __init__(self,name,age):
        self.name = name
        self._age = age

    def krishna(self):
        print('Inside class ', self.name,'Age ', self._age)

class Student(Person):

    def Ramya(self):
        print('Within class', self.name, self._age)

per1 = Person('Krishna', 60)

stud = Student('Ramya', 23)

per1.krishna()
stud.Ramya()

print('Outside class', per1._age)

print()


# Private
class Person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age

    def krishna(self):
        print('Inside class ', self.name, self.__age)

class Student(Person):

    def Ramya(self):
        print('Within class', self.name)
        print('Within class', self.__age)

per1 = Person('Krishna', 60)

stud = Student('Ramya',23)

per1.krishna()
stud.Ramya()

print('Outside class', per1.__age)


class MyEncapsulate():
    def __init__(self,name,age,balance):
         self.name =name
         self.age = age
         self.__account_balance = balance

    def update_balance(self,new_value):
        self.__account_balance = new_value

    def display_balance(self):
        print(self.__account_balance)

encap = MyEncapsulate('Ramya', 23, 0)
encap.display_balance()
print(encap.name)
encap.display_balance()
encap.update_balance(500)

encap.display_balance()


from abc import ABC, abstractmethod

class Phone(ABC):
    @abstractmethod
    def fun(self):
        pass

ph = Phone()
print(ph.fun())

def my_wrapper(func):
    def my_innerFunc():
        print("Inside wrapper.")
        func()
        print("hi hello")
    return my_innerFunc

@my_wrapper
def my_func():
    print("Hello, World!")

my_func()


class Person:
    pass

obj = Person()

def name():
    print(__name__)

print(Person.__name__)
print(obj)

from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def talk(self):
        pass

    def walk(self):
        pass

class Male(Person):
    def talk(self):
        print('Iam male')

male = Male()
print(male)


num = [3,2,5,3,2,3,6,7,8,2]
empty_list = []
for x in num:
    new_count = num.count(x) - 1
    if num.count(x) > 1 and empty_list.count(x) < new_count:
        empty_list.append(x)

print(empty_list)

num = [3,2,5,3,2,3,6,7,8,2]
list_a = []
list_b = []
for x in num:
    if x in list_b:
        list_a.append(x)
    else:
        list_b.append(x)

print(list_a)


def factorial_num(a):
    y = 1
    for x in range(1,a+1):
        y = x * y
    return y

num = factorial_num(2)
print(num)


# recoursive function
def fact(num):
    if num==0 or num==1:
        return 1
    else:
        return num * fact(num-1)

print(fact(3))


# less compile time
def fibonacci(n):
    fib_list = [0,1]
    for x in range(2,n):
        fib_list.append(fib_list[x-1] + fib_list[x-2])
    return fib_list
# for sum return fib_list[n-1]
print(fibonacci(8))


# more compile time
def fibonacci(n):
    fib = [0, 1]
    for x in range(2,n):
        fib1 = fib[x-1] + fib[x-2]
        fib.append(fib1)
    return fib
fibo = fibonacci(5)
print(fibo)


word = input('Word: ').lower()
vowels = ['a', 'e', 'i', 'o', 'u']
count = 0
for x in word:
    if x in vowels:
        count = count + 1
    else:
        continue
print(count)


word = input('Word: ').lower()
vowels = ['a', 'e', 'i', 'o', 'u']
empt_dict = {}
for x in vowels:
    empt_dict[x] = word.count(x)

print(empt_dict)


word = input('Word: ').lower()
vowels = ['a', 'e', 'i', 'o', 'u']
empt_dict = {}
for x in vowels:
    count = 0
    for y in word:
        if x == y:
            count = count + 1
        else:
            continue
    empt_dict[x] = count

print(empt_dict)


def fun_str(word):
    reverse = word[::-1]
    return reverse
print(fun_str('Ramya'))

list_num = [3,1,7,8,9,0]


def fun_list(num):
    left = 0
    right = len(list_num) - 1
    sort_list = sorted(list_num)
    while left != right:
        sum = sort_list[left] + sort_list[right]
        if sum == num:
            print((sort_list[left], sort_list[right]))
        if sum <= num:
            left = left + 1

        else:
            right = right - 1

fun_list(10)


class A:
    def __init__(self,name,age,place):
        self.__name = name
        self._age = age
        self.place = place

    def fun2(self):
        print(self.__name)

class B(A):
    def fun3(self):
        print(self._age)

obj_a = A('Ramya',22,'Kundapur')
obj_b = B('Kiran',25,'Kundapur')

obj_b.fun2()
obj_b.fun3()

print(obj_a.place)
print(obj_a._age)
print(obj_a.__name)


class A:
    def __init__(self,name,age):
        self._name = name
        self.age = age

    def fun(self):
        print(self._name)

obja = A('Ramya', 22)

obja.fun()

print(obja._name)


def only_even(fun):
    def inner_even(*b):
        z = list(filter(lambda x:x % 2 == 0,b))
        fun(z)
    return inner_even

@only_even
def fun_num(*b):
    print(*b)

fun_num(4,5,6,7,8,9,10)


class Encapsul:
    def __init__(self, place):
        self.__place = place

    def dis(self):
        print(self.__place)

    def update(self, x):
        self.__place= x

encap = Encapsul('Kundapur')

encap.dis()
encap.update("udupi")
encap.dis()

from abc import ABC, abstractmethod

class Student(ABC):
    def __init__(self, name, place):
        self.name = name
        self.place = place

    @abstractmethod
    def talk(self):
        pass

    @abstractmethod
    def walk(self):
        pass

class MaleStudent(Student):
    def __init__(self,name,place):
        pass

    def talk(self):
        print('male voice')

    def walk(self):
        pass

male_stud = MaleStudent('Ramya', 'Kundapur')
print(male_stud)

import datetime

x = datetime.datetime(2023,3,24)
print(x.strftime('%'))

class XYZ:

    def fun2(self):
        print(self)

    @classmethod
    def fun(cls):
        print(cls)


    @staticmethod
    def fun_2():
        print('ABCD')

x = XYZ()
x.fun2()
x.fun()
XYZ.fun()
XYZ.fun_2()

from abc import ABC, abstractmethod


class Person(ABC):

    __max_age = 100
    __min_age = 50

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.__salary = salary


    @abstractmethod
    def talk(self):
        pass

    @abstractmethod
    def walk(self):
        pass

    def salary_display(self):
        print(self.__salary)

    def salary_update(self,sal_update):
        pin = int(input('Enter pin: '))
        if pin == 3322:
            self.__salary = sal_update
        else:
            print('Invalid pin cannot update salary')

    @classmethod
    def display_max_age(cls):
        print(cls.__max_age)

    @classmethod
    def update_max_age(cls, max_age_update ):
        Person.__max_age = max_age_update

    @classmethod
    def display_min_age(cls):
        print(Person.__min_age)

    @classmethod
    def update_min_age(cls, min_age_update):
        cls.__min_age = min_age_update

class Male(Person):

    def talk(self):
        print('male: loud voice')

    def walk(self):
        print('male: walks fast')


class Female(Person):

    def talk(self):
        print('female: soft voice')

    def walk(self):
        print('female: walks slow')

class Other(Person):
    def talk(self):
        print('other: harsh voice')

    def walk(self):
        print('other: walks in medium speed')


female = Female('Riya', 21, 25000)
male = Male('Ravi', 22, 24000)
other = Other('Sukesh', 24, 23000)

from abc import ABC, abstractmethod


class Person(ABC):

    __max_age = 100
    __min_age = 50
    __pin = 3322

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.__salary = salary


    @abstractmethod
    def talk(self):
        pass

    @abstractmethod
    def walk(self):
        pass

    def salary_display(self):
        val = self.pin_validation()
        if val:
            print(self.__salary)
            return
        print('Invalid pin cannot update salary')

    def salary_update(self):
        val = self.pin_validation()
        if val:
            salary = int(input('New salary: '))
            self.__salary = salary
            print('Salary updated')
            return
        print('Invalid pin cannot update salary')


    def pin_validation(self):
        pin = int(input('Enter pin: '))
        if pin == Person.__pin:
            return True
        return False



    @classmethod
    def display_max_age(cls):
        print(cls.__max_age)

    @classmethod
    def update_max_age(cls, max_age_update ):
        Person.__max_age = max_age_update

    @classmethod
    def display_min_age(cls):
        print(Person.__min_age)

    @classmethod
    def update_min_age(cls, min_age_update):
        cls.__min_age = min_age_update

class Male(Person):

    def talk(self):
        print('male: loud voice')

    def walk(self):
        print('male: walks fast')


class Female(Person):

    def talk(self):
        print('female: soft voice')

    def walk(self):
        print('female: walks slow')

class Other(Person):
    def talk(self):
        print('other: harsh voice')

    def walk(self):
        print('other: walks in medium speed')


female = Female('Riya', 21, 25000)
male = Male('Ravi', 22, 24000)
other = Other('Sukesh', 24, 23000)

object_map = {1: female, 2: male, 3:other}
flag = True

while flag:
    query_1 = int(input('Enter 1 for female; 2 for male; 3 for other; 4 to discontinue: '))
    if query_1 in object_map:
        obj = object_map[query_1]
        query_2 = int(input('Enter 1 for update and 2 for display: '))
        if query_2 == 1:
            obj.salary_update()

        elif query_2 == 2:
            obj.salary_display()
        else:
            print('Please enter either 1 or 2')

    elif query_1 == 4:
        print('Program discontinued')
        flag = False

    else:
        print('Please enter either 1, 2 or 3')

import copy

l1 = [1,2,3,4,[6,7,[11,12]]]
shallow_l1 = copy.copy(l1)
print(l1)
print(shallow_l1)
# shallow_l1[4].append(8)
# print('after change')
print(id(l1), id(shallow_l1))
print(id(l1[1]),id(l1[4]))
print(id(shallow_l1[1]),id(shallow_l1[4]))
print('----------')


l1 = [1,2,3,4,[6,7,[11,12]]]
deep_l1 = copy.deepcopy(l1)
print(l1)
print(deep_l1)
# deep_l1[4].append(8)
# print('after change')
print(id(l1), id(deep_l1))
print(id(l1[1]),id(l1[4]),id(l1[4][2]), id(l1[4][0]))
print(id(deep_l1[1]),id(deep_l1[4]), id(deep_l1[4][2]), id(deep_l1[4][0]))

class Stack:

    def __init__(self):
        self.__stack_size = abs(int(input('Enter size of stack: ')))
        self.__list_num = []

    def push(self,x):
        if len(self.__list_num) == self.__stack_size:
            print('Stack is full')
        else:
            self.__list_num.append(x)

    def pop(self):
        if len(self.__list_num) == 0:
            return 'Stack is empty'
        else:
            return self.__list_num.pop()

    def display(self):
        print(self.__list_num)


stack = Stack()

x = stack.pop()
print("Pop item is: ", x)
stack.display()

from collections import deque


class Queue:

    def __init__(self):
        self.__queue_size = abs(int(input('Enter size of queue: ')))
        self.__que = deque()

    def enqueue(self, x):
        if len(self.__que) == self.__queue_size:
            print('Queue is full')
        else:
            self.__que.append(x)

    def dequeue(self):
        if len(self.__que) == 0:
            print('Queue is empty')
        else:
            return self.__que.popleft()

    def display(self):
        print(self.__que)


que = Queue()
que.enqueue(3)
que.enqueue(10)
que.enqueue(33)
que.dequeue()
que.dequeue()
que.dequeue()
que.dequeue()
que.display()

import requests

x = requests.post('https://reqres.in/api/users/', data={'name' : 'Ramya'})
print(x.json())
print(x.status_code)

x = requests.get('https://reqres.in/api/users/1')
print(x.json())
print(x.content)
print(x.text)
print(x.encoding)
print(x.status_code)
print(x.headers)

x = requests.get('https://reqres.in/api/users/23')
print(x.json())
print(x.status_code)

x = requests.put('https://reqres.in/api/users/2',data={'name':'Ramya'})
print(x.json())
print(x.status_code)

x = requests.patch('https://reqres.in/api/users/2',data={'place':'kundapura'})
print(x.json())
print(x.status_code)

x = requests.delete('https://reqres.in/api/users/2')
print(x.json())
print(x.status_code)

x = requests.head('https://reqres.in/api/users/',data={'age': 22})
print(x.headers)
print(x.status_code)

import json

x = json.loads('{"name":"Ramya"}')
y = json.dumps({"name": "Ramya", 'num': (1, 2, 3)})
print(x)
print(y)
print(type(x))
print(type(y))

import requests


def get_api_email(url):
    list_api_email = []
    response = requests.get(url)
    z = response.json()
    for x in z["data"]:
        list_api_email.append(x["email"])
    return list_api_email


email = get_api_email('https://reqres.in/api/users?page=1')
print(email)
import json

import requests


class Api:
    def __init__(self,url):
        self.url = url

    def get_data(self,key_data,key_val):
        list_api_val = []
        response = requests.get(self.url)
        data_response = response.json()[key_data]

        if type(data_response) == list:
            for item in data_response:
                list_api_val.append(item[key_val])
            return list_api_val

        elif type(data_response) == dict:
            return data_response[key_val]

        else:
            return data_response

    def post_data(self,key_data):
        response = requests.post(self.url, params={'name':'Ramya'})
        data_response = response.json()[key_data]
        return data_response

    def put_data(self):
        response = requests.put(self.url)
        data_response = response.content
        return data_response


api_call = Api('https://reqres.in/api/users?page=1')
api_call_2 = Api('https://reqres.in/api/users/5')
api_call_3 = Api('https://reqres.in//api/users/2')
print(api_call.get_data('total_pages',''))
print(api_call_2.get_data('data','first_name'))
print()
print(api_call.post_data('createdAt'))
print(api_call_3.put_data())


import requests

class Student:
    def __init__(self, url):
        self.url = url

    def upload_stud_details(self):
        name = input('name: ')
        ph_no = int(input('Enter 10 digit Ph.No: '))
        roll_no = int(input('Roll: '))
        response = requests.post(self.url, data={"name": name, "roll": roll_no, "phone": ph_no})
        upload = response.json()
        print(upload)

    def get_all_stud_data(self):
        response = requests.get(self.url)
        get_data = response.json()
        print(get_data)

    def update_stud_data(self):
        update_id = input('Which Id to update: ')
        response = requests.put(f'{self.url}{update_id}')
        print(response)

    def delete_stud_data(self):
        del_id = int(input('Enter Id to delete: '))
        val = f'{self.url}{del_id}'
        print(val)
        response = requests.delete(val)
        print(response.json())


# stud = Student('https://reqres.in/api/users')
stud = Student('http://192.168.0.179:8000/student/')
# stud.upload_stud_details()
# stud.get_all_stud_data()
stud.update_stud_data()
# stud.delete_stud_data()
stud.get_all_stud_data()


def fun_file():
    name = input('Name: ').capitalize()
    age = int(input('Age: '))
    ph_no = int(input('Phone: '))
    if len(str(ph_no)) == 10 and len(str(age)) == 2:
            file = open('/users/kavyavagle/Document/' + (input('Enter Filename: ')), 'w')
            file.write(f'Hello everyone.\nIam {name}. Iam {age} year old. My phone no is {ph_no}.')
            file.close()
    else:
        print('Invalid ph_no or age. Please enter 10 digit Phone no or proper age.')

fun_file()


def create_my_file():
    name = input('Name: ').title()
    age = int(input('Age: '))
    ph_no = int(input('Phone: '))
    if len(str(ph_no)) == 10 and len(str(age)) == 2:
        with open('/users/kavyavagle/Document/' + (input('Enter Filename: ')), 'w') as myfile:
            myfile.write(f'Hello everyone.\nIam {name}. Iam {age} year old. My phone no is {ph_no}.')

    else:
        print('Invalid ph_no or age. Please enter 10 digit Phone no or proper age.')


create_my_file()


import requests
import csv


def csv_file_fun():
    list_rows = []
    response = requests.get('https://reqres.in/api/users/')
    data = response.json()['data']
    list_headers = list(data[0].keys())

    for val in data:
        z = list(val.values())
        list_rows.append(z)

    with open('New_csv_file.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(list_headers)
        csv_writer.writerows(list_rows)


csv_file_fun()


import requests
import xlsxwriter


def csv_file_fun():
    response = requests.get('https://reqres.in/api/users/')
    data = response.json()['data']
    list_headers = list(data[0].keys())
    list_rows = []
    for val in data:
        z = list(val.values())
        list_rows.append(z)

    my_workbook = xlsxwriter.Workbook('/Users/kavyavagle/Document/My_url_Workbook.xlsx')
    worksheet = my_workbook.add_worksheet()
    row = 0
    column = 0

    for title in list_headers:
        worksheet.write(row,column,title)
        column = column + 1

    for id, email, first_name, last_name, avatar in list_rows:
        row = row + 1
        worksheet.write(row,0,id)
        worksheet.write(row,1,email)
        worksheet.write(row,2,first_name)
        worksheet.write(row,3,last_name)
        worksheet.write(row,4,avatar)

    my_workbook.close()

csv_file_fun()

print("Generator")


def generator_fun(max_num):
    num = 1
    while num <= max_num:
        yield num
        num = num + 1


for i in generator_fun(5):
    if i % 3 == 0:
        print(i)

print("Iterator")
class Iterator:
    def __init__(self):
        self.num = 1
        self.max = 5

    def __iter__(self):
        return self

    def __next__(self):
        if self.num < self.max:
            value = self.num
            self.num = self.num + 1
            return value
        else:
            raise StopIteration


iter_obj = Iterator()
for num in iter_obj:
    print(num)
iter(iter_obj)


import requests


class ApiFile:
    def __init__(self,url):
        self.url = url
        self.__data_store = None

    def get_api_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            self.__data_store = response.json()
        else:
            print('Failed to store response')

    def create_store_data_in_file(self,filepath):
        with open(filepath, 'w') as api_data_file:
            api_data_file.write(f'{self.__data_store}')

    def display_api_data(self):
        print(self.__data_store)


api_obj = ApiFile('https://reqres.in/api/users/')
api_obj.get_api_data()
api_obj.create_store_data_in_file('/Users/kavyavagle/Document/reqres_api_data_file.json')
api_obj.display_api_data()


def range_num(val):

    # base condition
    if val == 0:
        return

    # recursive call
    range_num(val-1)

    print(val)

range_num(5)


def sum_num(num):
    if num == 0:
        return num
    else:
        sum = num + sum_num(num-1)
        return sum

print('Sum of numbers =', sum_num(5))


def multiply_num(num):
    if num == 1:
        return num
    else:
        multiplication = num * multiply_num(num - 1)
        return multiplication

print('Multiplication of numbers =', multiply_num(5))


def fibonacci_series(num):
    if num == 1 or num == 0:
        return num
    else:
        fibonacci_num = fibonacci_series(num - 2) + fibonacci_series(num - 1)

        z = fibonacci_num
        return z


print(fibonacci_series(5))


def binary_search(list_num, desired_num):
    list_num.sort()
    lower_index = 0
    higher_index = len(list_num) - 1
    while lower_index <= higher_index:
        mid_index = (lower_index + higher_index) // 2
        if list_num[mid_index] == desired_num:
            return mid_index

        elif list_num[mid_index] < desired_num:
            lower_index = mid_index + 1

        else:
            higher_index = mid_index - 1

    return

num_list = [3, 4, 2, 5, 1, 6]
index_desired_num = binary_search(num_list, int(input('Enter desired num: ')))
print('The desired num is in index:', index_desired_num)

import requests
import psycopg2


class ReqresApi:
    def __init__(self, url):
        self.url = url
        self.__response = None
        self.conn = psycopg2.connect(host='localhost', dbname='db_ramya', user='postgres', password='krs291996', port=5432)
    def get_api(self):
        req = requests.get(self.url)
        self.__response = req.json()['data']

    def display_api(self):
        print(self.__response)

    def syn_api(self):
        self.get_api()

        with self.conn.cursor() as cur:
            for data in self.__response:
                try:
                   sql = f"INSERT INTO public.ApiReqres(id, email, first_name, last_name, avatar)" \
                          f"VALUES({data['id']},\'{data['email']}\', \'{data['first_name']}\', \'{data['last_name']}\', \'{data['avatar']}\')"
                   print(sql)
                   cur.execute(sql)
                except Exception as e:
                    print(e)
            self.conn.commit()
            cur.execute("SELECT * FROM ApiReqres")
            results = cur.fetchone()
            print(results)


req_api_obj = ReqresApi('https://reqres.in/api/users/')
req_api_obj.get_api()
req_api_obj.display_api()
req_api_obj.syn_api()


def create_file():
    with open('/python_projects/python_postgres_project/service.py', 'w') as pyt_sql_file:
        pyt_sql_file.write('')

    with open('/python_projects/python_postgres_project/setting.py', 'w') as pyt_sql_file:
        pyt_sql_file.write('')


create_file()
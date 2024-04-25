# n_tuple = (10, 20)
# print(n_tuple[0])

from collections import namedtuple

# tuple = namedtuple('tuple', 'a b')
# tuple = namedtuple('tuple', ['a', 'b']) #-->shunaqa yozsa ham xatoga kirmidi
# tuple = namedtuple('tuple', 'a, b') #-->bu ham xatoga kirmidi
# t1 = tuple(15, 25)
# print(t1.b)

# print(type(namedtuple)) #--> tuple --> function

# bu usulni dictionery ko'rinishda qilsa ham bo'ladi chunki dictionary mutable

# student = ('Zuhriddin', 16, 'zuhriddinxursanov7@gmail.com')

# Studen1 = namedtuple('Studen1', 'Name')
# Student1 = namedtuple('Student', ['name', 'age', 'email'])
# zuhriddin = Student1(name='Zuhriddin', age=16, email='zuhrriddinxursanov7@gmail.com')
# print(zuhriddin[1])
# zuhriddin.name = 'Ali' # --> o'zgartirib bo'midi chunki --.immutable
# print(Student1)
# print(zuhriddin)

# class Student:
#    def __init__(self, name, age, email):
#        self.name = name
#        self.age = age
#        self.email = email
# Student2  = Student1
# print(Student2)

# from collections import namedtuple

# Comma = namedtuple('Comma', ['a', '_b'])
# c1 = Comma(32, 42)
# print(c1)


# n_tuple = (11, 22, ('malika', 'nozimabonuxamidova@gmai.com'), 16)
# print(id(n_tuple))
# n_tuple[1].append('nozima')
# print(id(n_tuple))
# print(hash(n _tuple))

from collections import namedtuple

# Dad = namedtuple("Dad", ['name', 'children'])
# d1 = Person('Shavkat', ['Nozima', 'Xadicha'])
# print(id(d1.children))
# d1.children.append('Madina')
# print(d1)
# print(id(d1.children))

from collections import namedtuple

# Student = namedtuple('Student', ['full_name', 'age', 'gender'], defaults=[16, 'female'])
# nozimabonu = Student('Nozima')
# print(nozimabonu)

# Student = namedtuple("Student", "full_name age height")
# n1 = ['Nozimabonu Hamidova', '17' 1.72]
# nozima = (Student._bonu(n1))
# print(nozima.height)

# print(nozima._asdict())


# Fruit = namedtuple('Fruit', ['name', 'color', 'tami'])
# args = ['apple', 'red', 'nordon']

# db = {'name': 'banana', 'color': 'yellow', 'tami': 'shirin'}
# print(Friut(**db))

# ananas = Fruit('ananas', 'brown', 'nordon, shirin')
# new_fruit = ananas._replace(color='yellow')
# print(new_fruit.color)


# num_list = [112, 223, 332, 443, 554, 665]
# print(len(num_list))
# print(max(num_list))
# print(min(num_list))


# print(num_list[1:])  # [223, 332, 443, 554, 665]
# print(num_list[0:3]) # [112  , 223 , 332]
# print(num_list[0::2])  # my_arr[start:stop:step]
# print(num_list[::-1])
# messages = 'Hello world', 'Salom'
# messages = 'Fruit'
# print(messages[::-1])
# print(num_list[-1::])

# print(num_list[1:8:3])
# num_list = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

# print(num_list[-6:-1:2])
# m1 = [1, 2, 3]
# m2 = [1, 2, 3]
# print(id(m1))
# print(id(m2))

# world = ('Hello',)
# print(type(world))

# number_tuple1 = (10, 20, 30)
# number_tuple2 = tuple({40, 50})
# number_tuple1 = (number_tuple1 + number_tuple2)
# print(number_tuple1)
#db = (10,)
#for i in db:
#     print(i)

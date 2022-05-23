# Контрольная работа

# 1
def fact(x):
    if(x==1 or x==0): 
        return 1
    else: 
        return x*fact(x-1)

# 2
def filter_even(li):
    new_li = list(filter(lambda x: x if x%2==0 else None, li))
    return new_li

# 3
def square(li):
    new_li = list(map(lambda x: x**2, li))
    return new_li

# 4
def bin_search(li, element):
    check = list(filter(lambda x: x != element, li))
    if check != li:
        out = li.index(element)
        return(out)
    else:
        return -1

# 5
def is_palindrome(string):
    str1 = ''.join(x for x in string if x.isalpha())
    str1 = str1.lower()
    x = 0
    y = 1
    while x <= len(str1)//2:
        if str1[x] != str1[len(str1) - y]:
            print('No')
            break            
        else:
            x += 1
            y += 1
    else:
        print('Yes')

# 6
def calculate(path2file):
    f0 = open(path2file)
    li = f0.readlines()
    x = 0
    str1 = ''
    while x < len(li):
        str0 = li[x].split()
        a = int(str0[1])
        b = int(str0[2])
        if str0[0] == '+':
            res = int(a + b)
            res = str(res)
        elif str0[0] == '-':
            res = int(a - b)
            res = str(res)
        elif str0[0] == '*':
            res = int(a * b)
            res = str(res)
        elif str0[0] == '//' and a > 0 and b > 0:
            res = int(a // b)
            res = str(res)
        elif str0[0] == '%' and a > 0 and b > 0:
            res = int(a % b)
            res = str(res)
        elif str0[0] == '**' and a > 0 and b > 0:
            res = int(a ** b)
            res = str(res)        
        if x == 0:
            str1 = res
        else:
            str1 = str1 + ',' + res
        x += 1
    return str1

#7
def substring_slice(path2file_1,path2file_2):   
    f1 = open(path2file_1)
    f2 = open(path2file_2)
    li1 = f1.readlines()
    li2 = f2.readlines()
    x = 0
    str1 = ''
    while x < len(li2):
        li20 = li2[x].split()
        a = int(li20[0])
        b = int(li20[1])
        slice0 = li1[x][a:b+1]
        if x == 0:
            str1 = slice0
        else:
            str1 = str1 + ' ' + slice0
        x += 1
    return str1

# 8
import json
import re
def decode_ch(sting_of_elements):
    with open('G:\\Университет\\Практикум по программированию\\2 семестр\\periodic_table.json', 'r', encoding='utf-8') as fh:
        periodic_table = json.load(fh)
    new_li = re.sub(r'([A-Z])', r' \1', sting_of_elements).split()
    str0 = ''
    x = 0
    while x < len(new_li):
        a = periodic_table.get(new_li[x])
        str0 = str0 + a
        x += 1
    return str0

# 9
class Student():
    default_grades = [3,4,5]

    def __init__ (self, name, surname, grades):
        self.name = name
        self.surname = surname
        if grades:
            self.grades = grades
        else:
            self.grades = self.default_grades
        self.fullname = name + ' ' + surname

    def greeting(self):
        return 'Hello, I am Student' 

    def mean_grade(self):
        sum0 = sum(self.grades)
        res = sum0 / len(self.grades)
        return res

    def is_otlichnik():
        if Student.mean_grade >= 4.5:
            return 'YES'
        else:
            return 'NO'

    def __add__(self, Student):
        return self.name + ' is friends with ' + Student.name

    def __str__(self):
        return self.fullname
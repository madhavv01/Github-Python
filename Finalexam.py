#NAME: Madhav Jariwala
#STUDENT ID - 2397671


#PART 1

import sqlite3

def students(connection): # students table
    cursor = connection.cursor()
    cursor.execute('''
    create table if not exists students( 
    id integer primary key,
    name text not null,
    age integer,
    marks integer
    )  
    ''')
    connection.commit()
    cursor.close()

def courses(connection): # course table
    cursor = connection.cursor()
    cursor.execute('''
    create table if not exists courses(
    id integer primary key,
    name text not null
    )  
    ''')
    connection.commit()
    cursor.close()
    

def student_courses(connection): # student_courses table
    cursor = connection.cursor()
    cursor.execute('''
    create table if not exists student_courses(
    student_id integer,
    course_id integer
    foreign key (student_id) references students (id)
    foreign key (course_id) references course (id)
    )  
    ''')
    connection.commit()
    cursor.close()
    
def insert_to_students(connection, name, age, marks): # inserting data to students table
    cursor = connection.cursor()
    cursor.execute ('''
    insert into students (name, age, marks) values (?, ?, ?)
    ''', (name, age, marks))
    connection.commit()
    cursor.close()
    
   
def update_record(connection, student_id, name, age, marks): # updating data in students table
    cursor = connection.cursor()
    cursor.execute('''
    update students set name = ?, age = ?, marks = ? where student_id = ?
    ''', (name, age, marks, student_id))
    connection.commit()
    cursor.close()
    
def delete_record(connection, user_id):
    cursor = connection.cursor()
    cursor.execute ('delete from students where id =?', (user_id,))
    connection.commit()
    cursor.close()

def read_all_records(connection):
    cursor = connection.cursor() # displaying data
    cursor.execute('''
    SELECT * FROM students
    ''')
    records = cursor.fetchall()
    cursor.close()
    for record in records:
        print(record)
        
    
def insert_courses(connection, name): # inserting data to courses table
    cursor = connection.cursor()
    cursor.execute ('''
    insert into courses (name) values (?)
    ''', (name,))
    connection.commit()
    cursor.close()
    

def update_courses(connection, course_id, name): # updating data
    cursor = connection.cursor()
    cursor.execute('''
    update courses set name = ? where course_id = ?
    ''', (name, course_id))
    connection.commit()
    cursor.close()
    

def delete_courses(connection, course_id): # deleting data from courses table
    cursor = connection.cursor()
    cursor.execute ('delete from courses where course_id =?', (course_id,))
    connection.commit()
    cursor.close()
    

def read_all_records(connection):
    cursor = connection.cursor() # displaying data
    cursor.execute('''
    SELECT * FROM courses
    ''')
    records = cursor.fetchall()
    cursor.close()
    for record in records:
        print(record)
        
     
def insert_to_student_courses(connection, student_id, course_id): #inserting data
    cursor = connection.cursor()
    cursor.execute ('''
    insert into student_courses (student_id, course_id) values (?, ?)
    ''', (student_id, course_id))
    connection.commit()
    cursor.close()
    

def update_student_courses(connection, student_id, course_id): # updating
    cursor = connection.cursor()
    cursor.execute('''
    update student_courses set course_id = ? where student_id = ?
    ''', (course_id, student_id))
    connection.commit()
    cursor.close()
    
  
def delete_student_courses(connection, student_id): # deleting
    cursor = connection.cursor()
    cursor.execute ('delete from student_courses where student_id =?', (student_id,))
    connection.commit()
    cursor.close()
    

def read_all_records(connection):
    cursor = connection.cursor() # displaying data
    cursor.execute('''
    SELECT * FROM student_courses
    ''')
    records = cursor.fetchall()
    cursor.close()
    for record in records:
        print(record)




        

    
    
# Task 2

# base class Animal
class Animal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound
        
# classes derived from Animal

class Mammal(Animal): #child class
    def __init__(self, name, age, sound, color):
        super().__init__(name, age, sound)
        self.color = color

class Bird(Animal): #child class
    def __init__(self, name, age, sound, flight_speed):
        super().__init__(name, age, sound)
        self.flight_speed = flight_speed
        
# perform_sound_concert(animals) 
def perform_sound_concert(self, animals): 
        for animal in animals:
            print(f"{animal.name} makes {animal.sound}")     
        
# Overloading make_sound() method in the Animal class

def make_sound(self):
    if self.sound:
        print(self.sound)
    else:
        print("No sound available.")
        
# Overriding make_sound() method in both the mammal and bird

lion = Mammal("Lion", 12, "Roaring", "White")
eagle = Bird("Eagle", 5, "Screech", 80)
    
lion.make_sound()
eagle.make_sound()







#Task 3: Counter to find frequency of each word
from collections import Counter 

sentence = "Hi, I am Madhav Jariwala. This is my final exam."

counts = Counter(sentence.split())

for word, count in counts.items():
    print(f"The word '{word}' appears {count} times.")
    
    
# Task 4: frequency of each letter in a string.
from collections import defaultdict

sentence = "Hi, I am Madhav Jariwala. This is my final exam."

counts = defaultdict(int)

for letter in sentence:
    counts[letter] = counts[letter] + 1

for letter, count in counts.items():
    print(f"The letter '{letter}' appears {count} times.")
    
    
#Task 5: element-wise sum of two arrays.

import numpy as npy

a = npy.array([54, 82, 96])
b = npy.array([12, 58, 102])

c = a + b
print(c)

# Task 6: numbers divisible by both 3 and 5 from a tuple. 

def div_numbers(input_tuple):
    result = []
    for element in input_tuple:
        if element % 3 == 0 and element % 5 == 0:
            result.append(element)
    return result


# Task 7: finding the index of the second occurrence of a specified element in a tuple.

def find_sec_index(input_tuple, ele):
    count = 0
    for index, value in enumerate(input_tuple):
        if value == ele:
            count = count + 1
            if count == 2:
                return index
    return -1       

# Task 8: checking if a value exists in a dictionary. 
 
def key(dict, key):
    return key in dict   

# Task 9: calculating the average value of the keys in a dictionary.

def average(dict):
    total = 0
    count = 0
    for key in dict:
        total = total + dict[key]
        count = count + 1
    return total / count


# Task 10: finding the key with the maximum value in a dictionary. 

def max_key(dictionary):
    max_key = None
    max_value = float('-abc')
    for key, value in dictionary.items():
        if value > max_value:
            max_key = key
            max_value = value
    return max_key
    



    
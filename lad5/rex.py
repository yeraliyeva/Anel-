#1)Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
import re
show = re.compile('ab*')
string = input("Write your text: ")
m = show.search(string)
if m:
    print('Match found:', m.group())
else:
    print('No match')

#2) Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
import re
show = re.compile('ab{2,3}')
string = input("Write your text: ")
m = show.search(string)
if m:
    print('Match found:' , m.group())
else:
    print('No match:(')

#3) Write a Python program to find sequences of lowercase letters joined with a underscore.
import re

pattern = re.compile('[a-z]+_[a-z]+')

string = input("Write your text: ")

m = pattern.findall(string)

if m:
    print('Match found:', m)
else:
    print('No match')


#4)Write a Python program to find the sequences of one upper case letter followed by lower case letters.

import re

pattern = re.compile('[A-Z][a-z]+')

string = input("Write your text: ")

m = pattern.findall(string)

if m:
    print('Match found:', m)
else:
    print('No match')


#5#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

import re

pattern = re.compile('a.*b$')

string = input("Write your text: ")

m = pattern.match(string)

if m:
    print('Match found:', m.group())
else:
    print('No match')


#6)Write a Python program to replace all occurrences of space, comma, or dot with a colon.

import re


def replace_with_colon(text1):
    # result = text1.replace(' ', ':').replace(',', ':').replace('.', ':')
    
    return re.sub(r'[ ,.]', ':', text)


text = input("Write your text: ")

print(replace_with_colon(text))


#7)Write a python program to convert snake case string to camel case string.

import re

def match_to_upper(match):
    return match.group(1).upper()

def convert_snake_to_camel(snake_str):
    camel_str = re.sub(r'_([a-zA-Z])', match_to_upper, snake_str)
    return camel_str


snake_case_string = input()
camel_case_string = convert_snake_to_camel(snake_case_string)
print(camel_case_string)


#8)Write a Python program to split a string at uppercase letters.

import re

def split_at_uppercase(string):
    parts = re.findall('[A-Z][^A-Z]*', string)
    return parts

string = input()
result = split_at_uppercase(string)
print(result)


#9)Write a Python program to insert spaces between words starting with capital letters.

import re

def insert_spaces(text):
    result = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
    return result

text = input()
result = insert_spaces(text)
print(result)


#10)Write a Python program to convert a given camel case string to snake case.

import re


def camel_to_snake(match):
    return match.group(1) + "_" + match.group(2).lower()


def convert_camel_to_snake(snake_str):
    camel_str = re.sub(r'([a-z])([A-Z])', camel_to_snake, snake_str)
    return camel_str


camel_case_string = input()
snake_case_string = convert_camel_to_snake(camel_case_string)
print(snake_case_string)


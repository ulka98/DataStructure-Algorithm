from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)

''' 
# Exercise 1:
# Write a function in python that can reverse a string using stack data structure. 
# reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"
'''

def reverse_string(string):
    stack = Stack()
    for char in string:
        stack.push(char)
        reverse_string = ""
        while not stack.is_empty():
            reverse_string += stack.pop()
    return reverse_string
# Test the function
print(reverse_string("We will conquere COVID-19")) # Output: "91-DIVOC ereuqnoc lliw eW"

'''
# Exercise 2:
# Write a function in python that checks if paranthesis in the string are balanced or not. Possible parantheses are "{}',"()" or "[]". 
is_balanced("({a+b})")     --> True
is_balanced("))((a+b}{")   --> False
is_balanced("((a+b))")     --> True
is_balanced("))")          --> False
is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True
'''
def check_balanced_paranthesis(string):
    stack =Stack()
    opening = "({["
    closing = ")}]"
    matching = {")":"(", "}":"{", "]":"["}
    for char in string:
        print(char)
        if char in opening:
            stack.push(char)
        elif char in closing:
            if stack.is_empty():
                return False
            if stack.peek() ==matching[char]: # check if the top of the stack is the matching opening bracket
                stack.pop()
            else:
                return False
    return stack.is_empty()
# Test the function
print(check_balanced_paranthesis("({a+b})"))     # Output: True
print(check_balanced_paranthesis("))((a+b}{"))   # Output: False
print(check_balanced_paranthesis("((a+b))"))     # Output: True
print(check_balanced_paranthesis("))"))          # Output: False
print(check_balanced_paranthesis("[a+b]*(x+2y)*{gg+kk}")) # Output: True
print(check_balanced_paranthesis("()(")) # Output: False 


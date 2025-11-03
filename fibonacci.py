#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)

#Use functions
#One for validating and returning user input:
def num_of_terms():
  while True:
    user_input = input("How many terms do you want?") 
    if user_input.isdigit():
      number_of_terms = int(user_input)
      return number_of_terms 
    else:
      print("Error! Please enter a positive integer")
    
#One for generating the Fibonacci sequence:
def fibonacci_sequence(num):
  a = 0
  b = 1
  fibonacci_list = [] #an empty list to store the numbers
  
  for i in range (num):
    fibonacci_list.append(a) #Add the current number to the list
    temp = a 
    a = b
    b =  temp + b
  return fibonacci_list
  
#One for printing the sequence:
def print_sequence(seq):
  print("Fibonacci sequence:")
  for num in seq: 
    print (num, end=" ")
  print()

terms = num_of_terms() #validating and returning user input
sequence = fibonacci_sequence(terms) #generating the Fibonacci sequence
print_sequence(sequence) #printing the sequence

#Grading Comments:
# Your code crashes when you enter 0.

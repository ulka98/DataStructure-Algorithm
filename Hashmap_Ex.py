''''
#################Exercise: Hash Table########################
1. nyc_weather.csv contains new york city weather for first few days in the month of January. '
Write a program that can answer following:
a. What was the average temperature in first week of Jan
b. What was the maximum temperature in first 10 days of Jan
Figure out data structure that is best for this problem

2. nyc_weather.csv contains new york city weather for first few days in the month of January. '
Write a program that can answer following:
a. What was the temperature on Jan 9?
b. What was the temperature on Jan 4?
Figure out data structure that is best for this problem


poem.txt Contains famous poem "Road not taken" by poet Robert Frost. You have to read this file in python 
and print every word and its count as show below. Think about the best data structure that you can use to 
solve this problem and figure out why you selected that specific data structure.
 'diverged': 2,
 'in': 3,
 'I': 8

Implement hash table where collisions are handled using linear probing. We learnt about linear probing in the video tutorial. Take the hash table implementation that uses chaining and modify methods to use linear probing. Keep MAX size of arr in hashtable as 10.
'''

import csv
import pandas as pd
import numpy as np

class Hashmap:

    def __init__(self):
        self.MAX = 20
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

     #insert function
    def __setitem__(self,key, value):
        h = self.get_hash(key)
        found = False
        # address collision using chaining
        for ix, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key: # check if the key already exists, then update the value
                self.arr[h][ix] = (key, value)
                found = True
                break
        if not found:
            self.arr[h].append((key, value))

    # get function
    def __getitem__(self, key):
        h = self.get_hash(key)
        if self.arr[h] is None:
            return None
        elif isinstance(self.arr[h], list):
            for element in self.arr[h]:
                if element[0] == key:
                    return element[1]
        else:
            if self.arr[h][0] == key:
                return self.arr[h][1]
        return None
    
    # delete function
    def __delitem__(self, key):
        h = self.get_hash(key)
        if self.arr[h] is None:
            print("Key not found")
            return
        elif isinstance(self.arr[h], list): 
            for ix, element in enumerate(self.arr[h]):
                if element[0] == key:
                    del self.arr[h][ix]
                    return
        else:
            if self.arr[h][0] == key:
                self.arr[h] = None
                return
        print("Key not found")

# Example usage
hash_map = Hashmap()

#reading the csv file
with open('DSA/nyc_weather.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader) # Skip header
    for row in reader:
        date = row[0]
        tempetaure = float(row[1])
        hash_map[date] = tempetaure
file.close()
print(hash_map.arr)
# Example of getting the temperature on a specific date
print(hash_map['Jan 9'])  # Output: Temperature on  Jan 9

# a. What was the average temperature in first week of Jan
first_week_temps = [hash_map['Jan 1'], hash_map['Jan 2'], hash_map['Jan 3'], hash_map['Jan 4'], hash_map['Jan 5'], hash_map['Jan 6'], hash_map['Jan 7']]
average_temp = sum(first_week_temps) / len(first_week_temps)
print(f"Average temperature in first week of Jan: {round(average_temp,2)}")
# b. What was the maximum temperature in first 10 days of Jan
max = 0
for i in range(1, 11):
    if hash_map[f'Jan {i}'] > max:
        max = hash_map[f'Jan {i}']
print(f"Maximum temperature in first 10 days of Jan: {round(max,2)}")

# a. What was the temperature on Jan 9? 
print(hash_map['Jan 9'])  # Output: Temperature on Jan 9
# b. What was the temperature on Jan 4?
print(hash_map['Jan 4'])  # Output: Temperature on Jan 4

# Reading the poem file and counting word occurrences

with open('DSA/poem.txt', 'r') as file:
    text = file.read()
file.close()
words = text.split()
word_counter = {}
for word in words:
    if word in word_counter:
        word_counter[word] += 1
    else:
        word_counter[word] = 1
# Print word counts
for word, count in word_counter.items():
    print(f"'{word}': {count}")

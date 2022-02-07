#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

# You will see a string defined called 'Belgium'. Add code to print:

# a) A line of hyphens the same length as the Belgium string, followed by
# b) The string with the comma separators replaced by colons ':'., followed by
# c) The population of Belgium (the second field) plus the population of the
# capital city (the fourth field). Hint: the answer should be 11183818

# Part a) A line of hyphens the same length as the Belgium string
print(len(Belgium))  # prints out the length of the Belgium string = 81

line_of_hypens = "-"  # create variable for hypen.
print(line_of_hypens * (len(Belgium)))      # prints out 81 hypens

# Part b) The string with the comma separators replaced by colons ':'
print(Belgium.replace(",", ":"))  # prints string replacing all commas to colons

population_belgium = Belgium[8:16]
print(population_belgium)  # output 10445852

city_number = Belgium.index("737966")
print(city_number) # position 26

population_of_the_capital_city = Belgium[26:32]
print(population_of_the_capital_city)

total_population = population_belgium + population_of_the_capital_city
print(total_population)
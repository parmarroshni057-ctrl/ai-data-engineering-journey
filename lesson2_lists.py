salaries = [2500, 3000, 3500, 4000]

print("Salaries:", salaries) # print the list of salaries

print(salaries[0]) # print the first salary
print(salaries[2]) # print the third salary
print(len(salaries)) # print the number of salaries in the list

salaries.append(4500) # add a new salary to the list

print("Updated Salaries:", salaries) # print the updated list of salaries
print("Total Amount of Salaries:", sum(salaries)) # print the total amount of salaries

print(salaries[-4]) # print the fourth salary from the end of the list

print(salaries[-3:]) # print the last three salaries from the list

print(salaries[:2]) # print the first two salaries from the list
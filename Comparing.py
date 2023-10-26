from collections import defaultdict
import pickle

# Create defaultdict objects with a list as the default factory
Dict1 = defaultdict(list)
Dict2 = defaultdict(list)

with open('C:/Users/jagad/Python_projects/Sign_language_to_words/my_dict.pkl', 'rb') as file:
    Dict1 = pickle.load(file)

with open('C:/Users/jagad/Python_projects/Sign_language_to_words/my_dict1.pkl', 'rb') as file:
    Dict2 = pickle.load(file)

#print("Loaded defaultdict:", Dict2)

keylist = list(Dict1.keys())

# Initialize an empty list to store the values
values_list_saved = []
values_list_new = []

# Iterate through the dictionary and append values to the list
for key in Dict1:
    values_list_saved.extend(Dict1[key])

for key in keylist:
    for i in Dict1[key]:
        print(i)
        print(Dict2[key])
        if i in Dict2[key]:
            values_list_new.append(i)
            print("Element is present")
        else:
            print("Element is not present")

# Calculate the percentage
percentage = (len(values_list_new) / len(values_list_saved)) * 100

print(f"Percentage of elements from list1 present in list2: {percentage:.2f}%")

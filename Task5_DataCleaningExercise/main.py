"""
Sales department performance analysis
The HR department wants to analyze the performance of the employees in the sales department.
Data Reading
Rachel wrote a text file employee_revenue.txt including all necessary information, but she needs help to extract the necessary information.
Start by uploading the employee_revenue file to the working directory.
📌 Use the .read() method to open the text file in read mode and assign it to the variable "data".
"""
#Open the file in read mode
file=open("employee_revenue.txt","r")
data=file.read()

#Print the data
print(data)

"""
Data Cleaning
You can see that the data needs to be cleaned and information has to be extracted from these lines.
To be able to clean the data, you need to separate the text into lines.
📌 Use the .splitlines() method.
"""
#Seperate the data into lines
lines=data.splitlines()
print(lines)
"""
Clean the data line by line
Start to clean the data for the first line.
📌 Use the .strip() method to remove the whitespaces from the edges of the string.
"""
#Take the first line
string=lines[0]
print(string)
#Remove the whitespaces from the edges
string=string.strip(" ")
"""
Next, you need to fix the capitalization issues.
📌 Use the .lower() method to convert the text to lowercase.
📌 Then use the .capitalize() method to capitalize the first letter.
"""
#Convert the string to lowercase
string = string.lower()
string

#Capitalize the first character
string=string.capitalize()
string

"""
Information Extraction
To extract the information, you need to split the sentence into words.
📌 Use the .split() method.
"""
#Split the sentece into words
split_string = string.split(" ")
split_string
"""
You might noticed that the first element in the list is the name and the third element is the number of calls.
📌 Use the indeces to extract the name and number of calls.
"""
#Use the index 0 to access the name element
name=split_string[0]
#Use the index 2 to access the number of calls element
call_number=split_string[0]
call_number

"""
So far so good!
But as you can see the sentence order is not the same after the 7th element.
To extract the average deal size you need to come up with a different approach. You can use the "$" sign to find the corresponding element.
📌 Loop over the list to find the element that includes the "$" sign.
📌 Then, use the .split() method to divide the string into the number and the $ sign.
"""
#Find the element with the "$" sign
for i in split_string:
  #Divide the number from it
  if "$" in i:
    average_deal_size=i.split("$")[0]
#Print the average deal size
average_deal_size

"""
Similarly, we can use the string "dollars" to extract the revenue, which is the element right before "dollars".
📌 Use the .index() method to identify the index for the "dollars" element.
📌 Then, use this index to specify and extract the revenue.
"""
#Find the index of element "dollars"
dollars_index=split_string.index("dollars")
dollars_index

#Subtract one from the index to identify the index of the revenue element
revenue_index=dollars_index-1

#Extract the revenue
revenue=split_string[revenue_index]
revenue

#Great! You extracted all necessary information.
#📌 Print the information and check the types of the data.
#Print out the extracted information
print("name: ",name)
print("number of calls: ",call_number)
print("average deal size: ",average_deal_size)
print("revenue: ",revenue)

#Check the types
print("name type: ",type(name))
print("number of calls type: ",type(call_number))
print("average deal size type: ",type(average_deal_size))
print("revenue type: ",type(revenue))

# As you can see, we have the type string for all the data, but the average deal size, number of calls, and the revenue need to be integers.
# 📌 Convert the data using the int() function and check again.
average_deal_size=int(average_deal_size)
call_number=int(call_number)
revenue=int(revenue)

#Print out the information again
print("name type: ",type(name))
print("number of calls type: ",type(call_number))
print("average deal size type: ",type(average_deal_size))
print("revenue type: ",type(revenue))

"""
Now, you need to apply all the methods and functions to the list that contains the different strings of all employees.
📌 Create an empty lists for storing names, number of calls, average deal sizes, and revenues.
📌 Use a for loop to iterate through the list with the whole data.
📌 Print out the necessary information.
"""
#Create empty lists for the names, number of calls, average deal sizes, revenues
names = []
call_numbers = []
average_deal_sizes = []
revenues = []

# Loop over the whole data
for employee in lines:

    # Clean the string
    employee = employee.strip(" ")
    employee = employee.lower()
    employee = employee.capitalize()

    # Split the clean string
    split_employee = employee.split(" ")

    # Extract the name
    name = split_employee[0]
    call_number = split_employee[2]

    # Extract the average deal size
    for i in split_employee:
        if "$" in i:
            average_deal_size = i
    average_deal_size = average_deal_size.split("$")[0]

    # Extract the revenue
    dollars_index = split_employee.index("dollars")
    revenue_index = dollars_index - 1
    revenue = split_employee[revenue_index]

    # Convert to the correct data types
    average_deal_size = int(average_deal_size)
    call_number = int(call_number)
    revenue = int(revenue)

    # Append the information to the lists
    names.append(name)
    call_numbers.append(call_number)
    average_deal_sizes.append(average_deal_size)
    revenues.append(revenue)
    # Print out the information
    print("name: ", names)
    print("number of calls: ", call_numbers)
    print("average deal size: ", average_deal_sizes)
    print("revenue: ", revenues)

"""
Finally, you can make the process even easier and reusable by defining functions.
📌 Define the function "clean_extract".
📌 Use the retured values by assigning them to variables.
"""
#Create empty lists again
names = []
call_numbers = []
average_deal_sizes = []
revenues = []


# Define a function to clean and extract the data
def clean_extract(lines):
    for employee in lines:
        employee = employee.strip(" ")
        employee = employee.lower()
        employee = employee.capitalize()

        split_employee = employee.split(" ")
        name = split_employee[0]
        call_number = split_employee[2]

        for i in split_employee:
            if "$" in i:
                average_deal_size = i
                average_deal_size = average_deal_size.split("$")[0]

        dollars_index = split_employee.index("dollars")
        revenue_index = dollars_index - 1
        revenue = split_employee[revenue_index]

        average_deal_size = int(average_deal_size)
        call_number = int(call_number)
        revenue = int(revenue)

        names.append(name)
        call_numbers.append(call_number)
        average_deal_sizes.append(average_deal_size)
        revenues.append(revenue)

    return names, call_numbers, average_deal_sizes, revenues

#Assign returned values to variables
names,call_numbers,average_deal_sizes,revenues=clean_extract(lines)

#Print out the information
print("name: ",names)
print("number of calls: ",call_numbers)
print("average deal size: ",average_deal_sizes)
print("revenue: ",revenues)

"""
Performance Analysis Report
Now that you cleaned the string and extracted all the information using the function, you can create performance analysis report for the last month.
📌 Assign IDs to each employee.
📌 Create dictionaries.
📌 Sort the dictionaries.
First, check how many employees there are and assign the IDs.
📌 Use the len() and range() function.
"""
#Check the number of employees
print(len(names))
#Generate IDs
IDs=list(range(0,11))
print(IDs)
#Check the number of IDs
len(IDs)

"""
With the IDs ready, you need to assign the IDs to the employees.
📌 Use the zip() function to pair the employee with the ID.
📌 Convert the zip object into a dictionary.
"""
#Pair the names with the IDs in a dictionary
dictionary1=dict(zip(IDs,names))
dictionary1
#Pair the names with the revenues
dictionary2=dict(zip(revenues,names))
dictionary2
sorted_dictionary=sorted(dictionary2)[0:3]

for i in sorted_dictionary:
  print(dictionary2[i])

#Find the best performing employees (descending order)
sorted_dictionary=sorted(dictionary2,reverse=True)[0:3]

for i in sorted_dictionary:
  print(dictionary2[i])
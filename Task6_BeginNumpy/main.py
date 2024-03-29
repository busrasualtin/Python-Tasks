# NumPy
# Rachel is very happy with the way you cleaned and structured the employee data last time,
# but she wants to take things one step further.
# The sales team wants to track the performance of the employees not only by the revenue they generated,
# but also taking the number of calls and the average deal size into account.
# For that, Rachel wants you to create a software for reporting.
# To be able to perform calculations on the data you decide that creating a data structure using Numpy will be best.

# First, you need to get the data. You created lists with the relevant information in the last chapter.
# 📌 Copy and paste the lists "names", "call_numbers", "average_deal_size", and "revenues" you created in chapter 3 and assign them to variables.
names = ['Ben', 'Omer', 'Karen', 'Celine', 'Sue', 'Bora', 'Rose', 'Ellen', 'Bob', 'Taylor,', 'Jude']
call_numbers = [300, 10, 500, 70, 100, 100, 600, 800, 200, 450, 80]
average_deal_size = [8, 6, 24, 32, 5, 25, 25, 40, 15, 10, 12]
revenues = [2400, 60, 12000, 2275, 500, 770, 4000, 6000, 800, 1200, 500]

# You plan to create a data structure using NumPy.
# 📌 Import the NumPy library as.
# !pip install numpy
import numpy as np

# Next, you need to prepare an array in which you will store the values. The initial array will be empty. Since it will hold numerical data, the data type should be integer.
# 📌 Create an empty array using .array().
# 📌 Use the dtype parameter to specify the data type.
data = np.array([], dtype=int)

# Now that your empty array is ready, you need to transfer the data from the lists to the array. You create 2 functions functions for this.
# append_names function: A function that takes the "names" list and adds the index of each name to the "data" array.
# 📌 Use a for loop and the .append() method for the indexes.
# append_performance_measures function: A function that takes one of the remaining lists to add the sales performance data like number of calls, average deal size and revenue to the "data" array.
# 📌 Use the .append() method.
#Define the append_names function
def append_names(names_list):
  global data
  for i in names_list:
    data = np.append(data, names.index(i))
#Define the append_performance_measures function
def append_performance_measures(feature_list):
  global data
  data = np.append(data, feature_list)

# Call the functions to add the data to the array and print the array and its shape to see the result.
# 📌 Use the .shape() method.
#Use the append_names and append_sales_performance_measures to add the data
append_names(names)
append_performance_measures(call_numbers)
append_performance_measures(average_deal_size)
append_performance_measures(revenues)
#Print the array and its shape to see the result
print(data)
print(data.shape)

# But like this, your array is not very structured.
# You need a 2D-array to be able to work better with it. The original data was 4 lists each with 11 values.
# So, the "data" array should have 4 rows and 11 columns. Print the result afterwards.
# 📌 Use the .reshape() method to rearrange the values in the array.
#Use the .reshape() method to change the array structure to 4 rows and 11 columns
data = data.reshape(4, 11)

#Print the resulting array and its shape
print(data)
print(data.shape)


# Inside the array you can access the values in different ways.
# Print each row separately.
# 📌 Write down the array name and the index of the row you want to access.
#Print the name indexes
print(data[0])
#Print the number of calls
print(data[1])
#Print the average deal sizes
print(data[2])
#Print the revenues
print(data[3])


# Print a specific value.
# 📌 Give the index of the row and the column of the value you want to access.
# For example, to get the revenue generated by Ellen, specify the value in the 3rd row and 7th column.
#Print the revenue generated by Ellen
print(data[3,7])


# Analyzing the data
# Great, your array is ready!
# The sales team has a formula that they use to calculate the performance score of an employee.
# Performance=(Average deal size x Revenue)/Number of calls
# 📌 Create a function called “calculate_performance” to implement this formula. It should take the employee name as an input.
#Define the function calculate_performance
def calculate_performance(employee_name):
  idx = names.index(employee_name)
  number_of_calls = data[1, idx]
  avg_deal_size = data[2, idx]
  revenue = data[3, idx]

  performance=(avg_deal_size * revenue)/number_of_calls
  return performance

# Try it out
# Let's check Ellen's performance score and print the result.
#Use the calculate performance function to print Ellen's performance
print(calculate_performance("Ellen"))

# Calculate the performance of each employee
# Now you need to calculate the performance score of each employee and add these scores to a list.
# 📌 Create an empty list "performance_scores" to hold the scores.
# 📌 Use a for loop to convert the scores into integer type data and append it to the list "sperformance_scores".
#Calculate the performance of each employee
performance_list = []
for name in names:
  performance=int(calculate_performance(name))
  performance_list.append(performance)

# Add the scores to the "data" array
# Next, you need to add the scores to your "data" array and print the result.
# 📌 Use the .concatenate() method to add the "performance_scores" list to the "data" array.
#Add the "performance_scores" list to the "data" array
data = np.concatenate((data, [performance_list]), axis=0)

#Print the resulting array
print(data)

# Find out the best and worst performing employees
# Finally, you need to determine the best and worst performing employees.
# 📌 Use the .argmax() and .argmin() methods to find the index of the best and worst performing employees.
idx_best_employee = np.argmax(data[4])
idx_worst_employee = np.argmin(data[4])
#Print out the results
print(f"Best Performing Employee: {names[idx_best_employee]}")
print(f"Worst Performing Employee: {names[idx_worst_employee]}")
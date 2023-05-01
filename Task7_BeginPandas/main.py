# Pandas
# The sales department wants to compare the performances of this and last year.
# Firstly, they delivered your team the performance review from last year.
# The data is in a comma-separated format, a .csv file called “employee_revenue_lastyear.csv”.
# It is in tabular form and includes information about 11 employees.

# Importing libraries
# First, you need to import the required libraries.
#
# 📌 Import the Pandas and NumPy libraries.
import pandas as pd
import numpy as np

# Get the data from last year
# Next, you need to get the data from the .csv file that the sales team provided.
# 📌 Use the .read_csv() function of the Pandas library to import the data from "employee_revenue_lastyear.csv" and assign it to the variable "last_year".
last_year = pd.read_csv("employee_revenue_lastyear.csv")

# Check the imported data
# It is important to check if everything is included.
# But you don't need to see the whole DataFrame, it will be enough to see the first and last rows.
# 📌 Use the .head() function to get the first n-rows of the DataFrame:
#
# Without specifying any number to get the first 5 rows by default.
# Give a number n as an argument to print the first n-rows, for example 8.
last_year.head()
last_year.head(8)

# Use the .tail() function to get the last n-rows of the DataFrame:
# Without specifying any number to get the last 5 rows by default.
# Give a number n as an argument to print the last n-rows, for example 6.
last_year.tail()
last_year.tail(6)

# Another way to quickly get the number of rows and columns is using the shape attribute.
# 📌 Use the shape attribute to display the number of rows and columns.
last_year.shape

# If you want to get more details about the DataFrame, you can use the .info() function.
# 📌 Use the .info() function to get more details about the DataFrame.
last_year.info()

# Add information to the DataFrame
# Now you should have enough insights about the DataFrame. :)
# You know that the data in the DataFrame is from 2021.
# This information should be included, so you decide to add the column "Year".
# 📌 Add the column "Year" to the DataFrame and pass the value "2021" to its rows.
# Then display the DataFrame to see the result.
last_year["Year"] = 2021
last_year

# Get the data from this year
# You also need to add the data from this year to be able to compare both years.
# You already prepared this data in task 6.
# 📌 Copy and paste the NumPy arrays "names", "call_numbers", "average_deal_sizes", and "revenues" from task 6.
names = np.array(['Ben', 'Omer', 'Karen', 'Celine', 'Sue', 'Bora', 'Rose', 'Ellen', 'Bob', 'Taylor', 'Jude'])
call_numbers = np.array([300, 10, 500, 70, 100, 100, 600, 800, 200, 450, 80])
average_deal_sizes = np.array([8, 6, 24, 32, 5, 25, 25, 40, 15, 10, 12])
revenues = np.array([2400, 60, 12000, 2275, 500, 770, 4000, 6000, 800, 1200, 500])

# Now create a DataFrame using these arrays.
#
# 📌 Create a dictionary with the arrays.
# Specify the column names in the keys.
# 📌 Convert the dictionary to a Pandas DataFrame "current_year" and use the .head() function to check it.
dictionary = {
    "name" : names,
    "calls" : call_numbers,
    "avg_deal_size" : average_deal_sizes,
    "revenue" : revenues
}
current_year = pd.DataFrame(dictionary)
current_year.head()

# Similar to what we did with last year's data, add the year information.
# 📌 Add the column "Year" to the DataFrame and pass the value "2022" to its rows.
# Then use the .head() function to see the result.
current_year["Year"] = 2022
current_year.head()

# Compare the two DataFrames
# Now that you printed the DataFrame "current_year", print "last_year" as well to compare them.
# 📌 Use the .head() function to print the DataFrame "last_year".
last_year.head()
# You notice that the column names of the two DataFrames are different. You need to fix this problem.
# 📌 Assign the column names of "last_year" to "current_year" by using the columns attribute.
current_year.columns = last_year.columns

# Concatenate two DataFrames
# Now that the two DataFrames have the same column names.
# You can merge - or concatenate - them into a single DataFrame "all_data".
# 📌 Use the .concat() function with the argument "axis" set to 0.
# Then display the DataFrame.
all_data = pd.concat([last_year,current_year], axis=0)
all_data

# Check the data
# This worked out well, but you noticed that the indexes are incorrect.
# You need to reset them.
# 📌 Use the .reset_index() function.
# Set the arguments "drop" and "inplace" to "True".
# Then display the DataFrame.
all_data.reset_index(drop = True, inplace = True)
all_data

# Next, you need to check the entries for missing values.
# 📌 Use the isna.() and .any() function to see if there are missing values in the DataFrame.
all_data.isna().any()

# From the output, you see that there are missing values in the columns "Average deal size" and "Revenue".
# You decide to fix this problem by filling the missing values using with the mean of the respective column.
# 📌 Use the .fillna() function to fill the missing values.
# Use the .mean() function to set the argument "value" to the mean of "all_data".
# Again, set "inplace" to "True".
all_data.fillna(value=np.mean(all_data), inplace = True)
all_data

# Also, there may be some duplicated rows, you need to drop them.
# 📌 Use the .drop_duplicates() method to remove any duplicated rows.
# 📌 Reset the indexes again using the reset_index() function.
all_data.drop_duplicates(inplace = True)
all_data.reset_index(drop = True)
all_data

# Data analysis
# Statistical analysis
# The DataFrame is ready, great!

# Now you can use it to analyse the overall performance of the employees over the last two years.
# You prepare a summary of the statistics.
# 📌 Use the .describe() method.
all_data.describe()
# 📌 Prepare a summary of the statistics for the data from 2021
all_data[all_data["Year"] == 2021].describe()
# 📌 Prepare a summary of the statistics for the data from 2022.
all_data[all_data["Year"] == 2022].describe()

# You also want to rank the employees by the generated revenue.
# 📌 Use the .sort_values() method to sort the values by the column “Revenue”.
all_data.sort_values(by="Revenue")

# As you did with the .describe() function, you can also use conditions to filter information.
# 📌 Sort the revenue values of 2022.
all_data[all_data["Year"] == 2021].sort_values(by="Revenue")

# Finally, you can count how many times an employee appears in the DataFrame to determine which employee has worked for the company for two years.
# 📌 Use the value_counts() function for the column "Name".
all_data["Name"].value_counts()
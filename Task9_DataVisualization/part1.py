
import seaborn as sns #importing seaborn library and using as sns
planets = sns.load_dataset("planets") #loading planets library from seaborn
planets.head()

#now we import planets dataset from seaborn to our project

#protecting the original structure and copying the dataset
df = planets.copy() #df=dataframe
df.head() #first 5 rows

df.tail() #last 5 rows

#dataset structural informations
df.info()

#just want to see attributes and their structures
df.dtypes

#i want to change method's type from object to categorical because advanced functions can understand that it is categorical but some of special functions can be confused about it.
import pandas as pd
df.method = pd.Categorical(df.method)

df.dtypes #when we run again we can see the change clearly

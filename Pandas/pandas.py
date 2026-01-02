# print(3+4)
# print(3-4)
# print(3*4)
# print(3/4)



# print("Monu"*5)


# my_dict = {"Name":"Monu","age":23,"class":"c.s.e"}
# for key,value in my_dict.items():
#     print(key,value)

# print(sorted(my_dict.items()))


# data = {
#     "Name": ["Alice", "Bob", "Charlie"],
#     "Age": [20, 22, 19]
# }

# df = pd.DataFrame(data)
# print(df)
# print(pd.__version__)


# importing required libraries
import pandas as pd

# reading the dataset
# data = pd.read_csv(r"C:\Users\monus\OneDrive\Desktop\Python\basicOperators\Sample.csv")


# viewing the first few rows using head()
# print(data.head())

martdata = pd.read_csv(r"C:\Users\monus\OneDrive\Desktop\Python\basicOperators\data.csv")


# viewing the first few rows using head()
# print(martdata.head())


# viewing the number of rows and columns
# print(martdata.shape)
# print(martdata.to_string())

# selecting a single column by column name
# print(martdata['Name'].to_string())



# selecting a multiple columns by column names
# print(martdata[['Name','Age']])


# selecting  rows by their position
print(martdata.iloc[:5])


# selecting  columns by their position
print(martdata.iloc[:,:2])


# selecting rows by given condition
print(martdata[martdata['Pclass']==1])

import pandas as pd

data_frame = pd. DataFrame({
'roll no': [ 102, 101, 104, 103, 105],
'name' : ['Aravind', 'Rahul', 'Prateek', 'Piyuesh', 'Kartik'],
'grade': ['B', 'B', 'A', 'C', 'A'],
'marks': [ 15, 15, 20, 4, 22],
'city' : ['Gurugram', 'Delhi', 'Delhi', 'Gurugram', 'Hyderabad' ]

})
# print(data_frame)

data_frame.sort_values(by=['grade','marks'], ascending=[True,False])  
print(data_frame.reset_index())
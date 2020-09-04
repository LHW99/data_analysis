import numpy as np
import pandas as pd 

# creating a series with pandas
new = pd.Series([1,2,3])

# assigning indicies
new.index = (
  ['Canada',
  'United States',
  'Japan']
)

# creating a data frame (like a data table)
df = pd.DataFrame({
  'Column A': [54, 66, 33, 12],
  'Column B': ['dro', 'huh', 'wee', 'tiy'],
  'Column C': ['no', 'yes', 'no', 'no']
})

# assigning indicies
df.index = [
  'Row A',
  'Row B',
  'Row C',
  'Row D'
]

# inserting new column
cd = pd.Series(
  [1, 0],
  index=['Row B', 'Row D'],
  name = 'Column D'
)

df['Column D'] = cd

# turns every value in column d to 2
# df['Column D'] = 2

# you can create a new column using a combination of other columns
df['Column E'] = df['Column B'] + df['Column C']

print df
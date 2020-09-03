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

print df['Column A'] > 50
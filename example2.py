#!/usr/local/bin/python3

import pandas as pd
data = (
    {
        'Tags': [ 'one', 'two', 'three' ],
        'Counts': [10, 20, 30],
        'Colors': [ 'red', 'blue', 'gree' ],
    }
)
df = pd.DataFrame(data)
print('The tags series:')
series = df['Tags']
print(series)
grades = pd.Series([90, 80, 70, 65, 77, 98, 32, 99, 88, 86], name='Grades')
print('The grades series:' + str(grades))
grades.describe()
print('The average grade is:' + str(grades.mean()))
df2 = pd.DataFrame(grades)
print('The grades dataframe:' + str(df2))
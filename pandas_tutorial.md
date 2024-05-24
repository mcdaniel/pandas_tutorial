# Pandas

## Overview

Pandas is a python package for data analysis used for managing, querying and processing data in python.  It is part of the Anaconda distribution, which is large suite of tools for data processing.  Installing pandas is platform dependent, so check your local distrubution for information on how to process.  For example, 

The basic unit of data is called a **DataFrame**, which is a 2-dimensional object representing a collection of data.  Each DataFrame is organized as a set of rows and columns, which you can conceptually think about as a spreadshet.  Each column has a name (generally) and rows contain data for an example of each of the things you are recording.  The table cells can hold text, numnber, floating point, categorical data, and more.  The data in a column is called a **series**.

##### Simple Example (example1.py)

    import pandas as pd
    data = (
        {
            "Tags": [ "one", "two", "three" ],
            "Counts": [10, 20, 30],
            "Colors": [ "red", "blue", "gree" ],
        }
    )
    df = pd.DataFrame(data)
    print(df)

## Working with Series

Much of the work you will do relates to the processing of the data, and most of that will be extracting, projecting, creating, and manipulating series.  The simplist way to think about it is to remain thinking of the DataFrame as a table of data.

The most basic operation on at DataFrame is to access one of the series.  To do this, you just access it by the name of the field, just like an associative array with the key being the series name and the value being the array of values.

You can also create series on the fly and use pandas functions to operate on and sumarize the data in the sample.  You can also create DataFrames on the fly using the series.

#### Series examples (example2.py)

    series = df["Tags"]
    print(series)
    grades = pd.Series([90, 80, 70, 65, 77, 98, 32, 99, 88, 86], name="Grades")
    print("The grades series:" + str(grades))
    grades.describe()
    print("The average grade is:" + str(grades.mean()))
    df2 = pd.DataFrame(grades)
    print("The grades dataframe:" + str(df2))
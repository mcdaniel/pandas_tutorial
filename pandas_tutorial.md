# Pandas, Mathplotlib, and Seaborn

## Overview

Pandas is a python package for data analysis used for managing, querying and processing data in python.  It is part of the Anaconda distribution, which is large suite of tools for data processing.  Installing pandas is platform dependent, so check your local distrubution for information on how to process.  For example, 

The basic unit of data is called a **DataFrame**, which is a 2-dimensional object representing a collection of data.  Each DataFrame is organized as a set of rows and columns, which you can conceptually think about as a spreadshet.  Each column has a name (generally) and rows contain data for an example of each of the things you are recording.  The table cells can hold text, numnber, floating point, categorical data, and more.  The data in a column is called a **series**.

##### Simple Example (example1.py)

    import pandas as pd
    data = (
        {
            "Counts": [10, 20, 30],
            "Colors": [ "red", "blue", "gree" ],
        }
    )
    df = pd.DataFrame(data)
    print(df)

## Working with Series

Much of the work you will do relates to the processing of the data, and most of that will be extracting, projecting, creating, and manipulating series.  The simplist way to think about it is to remain thinking of the DataFrame as a table of data like you might see in Excel or SQL.

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

## Getting Data into Pandas

Most of the time you will not be creating all of your data within a pyython program, but loading it from an external source.  The simplest way to do this is to use the built in Pandas functions.  The one I use most frequently is the read function for CSV (comma separated value) data format.  It is super simple, where you give it a file name and call the appropriate function.  The supported types include csv, excel, json, etc.  You can also export the data to different data types in a similar manner.  You simply call a "to" function on the DataFrame and it create the external file.  

Both the read and to functions have a lot of optional arguments you can pass into the call.  For example, you can export to a CSV and include a parameter of "index=false" to stop the export from including an index column.

#### Data loading example (example3.py)

    # Load files
    letfreq = pd.read_csv("data/wordle_freq.csv")
    print(letfreq)
    bigrams = pd.read_csv("data/wordle_bigram.csv")
    print(bigrams)
    trigrtam = pd.read_csv("data/wordle_trigram.csv")
    print(trigrams)

    # Export files
    letfreq.to_json("data/frequencies.json")

Ok, now we have our data in memory and ready to do something with it.  We will contiue here with manipulating the data within Pandas, but if you are acheing to jump right in and start looking at the data, you can jump down to the visualization part of this tutorial which covers [Mathplotlib](#mathplotlib), and thereafter to is child [Seaborn](#seaborn).

## Mathplotlib

Now that we have some data, we are going to want to do something with it.  For now, we just want to visuailze it, which means we want to create some figures that allow us to see something interesting about the data.  

The first thing to understand is a bit of terminology.  Within Mathplotlib, you operate on graphs where are valled **Figure**s, which may contain one more **Axes**.  Axes are specified in terms of x-y or x-y-z coordinate in whatever coordinate system you are using.


## Seaborn
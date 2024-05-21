# Pandas

## Overview

Pandas is a python package for data analysis used for managing, querying and processing data in python.  It is part of the Anaconda distribution, which is large suite of tools for data processing.  Installing pandas is platform dependent, so check your local distrubution for information on how to process.  For example, 

The basic unit of data is called a **DataFrame**, which is a 2-dimensional object representing a collection of data.  Each DataFrame is organized as a set of rows and columns, which you can conceptually think about as a spreadshet.  Each column has a name (generally) and rows contain data for an example of each of the things you are recording.  The table cells can hold text, numnber, floating point, categorical data, and more.  

The data in a column is called a **series**.

Data in the cells 

### Simple Example

    import pandas as pd

    df = pd.DataFrame(
        {
            "Tags": [ "one", "two", "three" ],
            "Counts": [10, 20, 30],
            "Colors": [ "red", "blue", "gree" ],
        }
    )
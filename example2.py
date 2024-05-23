#!/usr/local/bin/python3

import pandas as pd
data = (
    {
        "Tags": [ "one", "two", "three" ],
        "Counts": [10, 20, 30],
        "Colors": [ "red", "blue", "gree" ],
    }
)
df = pd.DataFrame(data)
print("The tags series:")
series = df["Tags"]
print(series)
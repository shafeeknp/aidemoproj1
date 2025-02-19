import pandas as pd

# creating data fram for test
data = {
    "Name": ["Tom", "nick", "krish", "jack"],
    "Age": [20, 21, 19, 18],
    "City": ["NY", "LA", "SF", "SD"],
}
df = pd.DataFrame(data)
print(df)  # print data frame
df.replace("nick", "Nick", inplace=True)  # replace NY with New York
print(df)  # print data frame
df.replace

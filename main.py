import pandas as pd

def column_change(df, col_name):
    # makes a list of unique values from column
    unique_vals = df[col_name].unique()
    print(unique_vals)

    # list to hold dictionary values
    nums = []

    # append the nums from 0 to the length of unique vals
    for x in range(len(unique_vals)):
        nums.append(x)

    # makes dictionary from values
    # 'Wii': 1, 'PS5': 2....
    diction = dict(zip(unique_vals, nums))
    print(diction)

    # replace in value in specified column with the mathcing value
    df.replace({col_name: diction}, inplace=True)
    return df


df = pd.read_csv('/Users/kevinbanze/Desktop/Video_Games_Sales_as_at_22_Dec_2016 2.csv')

column_change(df, 'Platform')
column_change(df, 'Genre')
column_change(df, 'Publisher')
column_change(df, 'Developer')
column_change(df, 'Rating')
print(df)
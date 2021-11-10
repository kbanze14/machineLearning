import pandas as pd

platformdict = {
    'Wii': 1,
    'NES': 2,
    'GB': 3,
    'DS': 4,
    'X360': 5,
    'PS3': 6,
    'PS2': 7,
    'SNES': 8,
    'GBA': 9,
    'PS4': 10,
    '3DS': 11,
    'N64': 12,
    'PS': 13,
    'XB': 14,
    'PC': 15,
    '2600': 16,
    'PSP': 17,
    'XOne': 18,
    'WiiU': 19,
    'GC': 20,
    'GEN': 21,
    'DC': 22,
    'PSV': 23,
    'SAT': 24,
    'SCD': 25,
    'WS': 26,
    'NG': 27,
    'TG16': 28,
    '3DO': 29,
    'GG': 30,
    'PCFX': 31
}
df = pd.read_csv('/Users/kevinbanze/Desktop/Video_Games_Sales_as_at_22_Dec_2016 2.csv')

df.replace({'Platform': platformdict}, inplace = True)
print(df['Platform'])
import pandas as pd
import numpy as np
import re

df = pd.read_csv(
    r"D:\Python\data analysis projects\fifa 21\fifa21 raw data v2.csv",
    low_memory=False
)

# print(df["Weight"].unique())


# def convert_weights(weight):
# # Handle missing values or NaN
#     if pd.isna(weight):
#         return np.nan
    
#     # Convert from Kg
#     if "kg" in weight.lower():
#         weight = weight.replace("kg", "").strip() # Remove 'Kg' and strip any spaces
#         return float(weight)
    
#     # Convert from lbs to Kg
#     elif "lbs" in weight.lower():
#         weight = x=weight.replace("lbs", "").strip() # Remove 'lbs' and strip any spaces
#         weight = np.round(float(weight) * 0.45359237, 2)
#         return weight

#     return np.nan

# print(df["Weight"].apply(convert_weights))
# print(df["Weight"].sample(frac=0.2))

# app_test = "85kg"
# if "kg" in app_test.lower():
#     print(True)
# else:
#     print(False)


un_matched = []
# for row in df["playerUrl"]:
#     if matches := re.search("^(http:\/\/).+(\/)$", row):
#         start, end = matches.groups()
#         if start == "http://" and end == "/":
#             continue
#         else:
#             un_matched.append(row)


# pattern = r"^\d{2}\-\S{3}\-\d{2}$"

# for row in df["Joined"]:
#     if re.match(pattern=pattern, string=row):
#         continue
#     else:
#         un_matched.append(row)

# from typing import Literal


# def extract_money_unit(money: str) -> None | Literal['K'] | Literal['M'] | Literal['Free Agent']:
#     money = money.strip("€").lower()
#     if money[-1].isalpha():
#         if "k" in money:
#             return "K"
#         elif "m" in money:
#             return "M"
#     else:
#         return "Free Agent"


# print(extract_money_unit('€103.5M'))
# print(extract_money_unit('€180K'))

import colorama
import time

col = ['Penalties', 'Composure', 'Defending', 'Marking', 'Standing Tackle',
        'Sliding Tackle', 'Goalkeeping', 'GK Diving', 'GK Handling',
        'GK Kicking', 'GK Positioning', 'GK Reflexes', 'Total Stats',
        'Base Stats', 'W/F', 'SM', 'A/W', 'D/W', 'IR', 'PAC', 'SHO', 'PAS',
        'DRI', 'DEF', 'PHY', 'Hits']
colorama.init()

for i in col:
    title = f"column name: {i}"
    print(colorama.Fore.YELLOW + colorama.Style.BRIGHT + title + colorama.Style.RESET_ALL)
    print("missing data:".upper(), df[i].isna().sum())
    print(f"count of {i}: {df[i].count()}")
    print("dataType: ", df[i].dtype)
    print("unique data", df[i].unique())
    print("-" * 30, "\n\n")
    time.sleep(5)

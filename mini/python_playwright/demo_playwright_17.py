import re
import pandas as pd
from pathlib import Path
from random import randrange
from playwright.sync_api import sync_playwright, expect


df_1 = pd.read_excel(Path(__file__).parent.joinpath("newspaper/newspaper_info_v1.xlsx"))
df_2 = pd.read_excel(Path(__file__).parent.joinpath("newspaper/newspaper_info_v2.xlsx"))
df_3 = pd.read_excel(Path(__file__).parent.joinpath("newspaper/newspaper_info_v3.xlsx"))

df = pd.concat([df_1, df_2, df_3], ignore_index=True)
df = df.drop_duplicates(["报刊名称", "主办单位"])
print(df.loc[df.duplicated(["报刊名称"], keep=False), ])

df.to_excel(Path(__file__).parent.joinpath("newspaper/newspaper_df.xlsx"), index=False)


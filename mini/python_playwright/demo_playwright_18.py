import re
import pandas as pd
from pathlib import Path
from random import randrange
from playwright.sync_api import sync_playwright, expect


data_df = pd.read_excel(Path(__file__).parent.joinpath("input/上市企业数据.xlsx"), converters={"stock_code": str})
info_df = pd.read_excel(Path(__file__).parent.joinpath("input/TRD_Co.xlsx"), converters={"stock_code": str})

data = pd.merge(data_df, info_df, how="left", on=["stock_code"])

data.to_excel(Path(__file__).parent.joinpath("input/上市企业数据_v2.xlsx"), index=False)


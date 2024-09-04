import streamlit as st 
import pandas as pd 
from pathlib import Path
import plotly.express as px 

def read_data():
    data_path = Path(__file__).parents[2] / "data"
    df = pd.read_csv(data_path / "cleaned_yh_region.csv",index_col=0, parse_dates=[0])
    df.index = df.index.year
    return df 

print(read_data())
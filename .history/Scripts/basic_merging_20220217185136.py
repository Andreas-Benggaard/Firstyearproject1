from pydoc import describe
import pandas as pd 
from statistics import mean
import numpy as np 
import statsmodels.api as sm 
import json 




def merge_data(attr_file): 
    with open("attributes.json", "r") as infile:
        attributes = json.load(infile)
    weather_data_file = f'{attributes["files"]["base_path"]}{attributes["files"]["weather"]}'
    weather_data = pd.read_csv(f'{attributes["files"]["base_path"]}{attributes["files"]["weather"]}', sep=",")
    



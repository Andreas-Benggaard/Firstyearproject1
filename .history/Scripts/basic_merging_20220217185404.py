from pydoc import describe
import pandas as pd 
from statistics import mean
import numpy as np 
import statsmodels.api as sm 
import json 




def merge_data(attr_file): 
    with open("attributes.json", "r") as infile:
        attributes = json.load(infile)
    weather_data = pd.read_csv(f'{attributes["Files"]["Base_path"]}{attributes["Files"]["Weather"]}', sep=",")
    if weather_data.isnull().values.any(): 
        return "Missing data"
    weather_data[["country","region"]]= weather_data["iso3166-2"].str.split("-",expand=True)
    nl_data = weather_data[weather_data["country"] == attributes["Country"]]

merge_data("attribues.json")

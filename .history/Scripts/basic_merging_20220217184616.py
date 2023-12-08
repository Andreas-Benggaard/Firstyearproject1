import pandas as pd 
from statistics import mean
import numpy as np 
import statsmodels.api as sm 
import json 




with open("attributes.json", "r") as infile:
    tmp = json.load(infile)
    print(tmp)

    
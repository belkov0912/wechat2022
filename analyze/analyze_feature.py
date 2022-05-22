import numpy as np
import pandas as pd
import json


with open('../data/annotations/labeled.json') as f:
    features = json.load(f)

print(features)
import numpy as np
import pandas as pd
import json

with open('../data/annotations/labeled.json') as f:
    features = json.load(f)

df = pd.DataFrame(features)

# print(df.describe())

df['title_length'] = df['title'].apply(lambda x: len(x))

import pandas as pd
import json

filepath = "Lucas97de/Training-Python/Json/example_2.json"

df = pd.read_json(filepath)

print(df)
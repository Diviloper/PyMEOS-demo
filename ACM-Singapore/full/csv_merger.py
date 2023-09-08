import pandas as pd

df = pd.concat(
    [
        pd.read_csv('singapore-0.csv'),
        pd.read_csv('singapore-1.csv'),
        pd.read_csv('singapore-2.csv'),
    ]
)

df.to_csv('singapore.csv', index=False)

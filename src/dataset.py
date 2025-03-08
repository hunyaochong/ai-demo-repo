import pandas as pd

data = {
    "Name": ["Alice", "Bob"],
    "Age": [24, 26],
    "City": ["New York", "Los Angeles"],
}
df = pd.DataFrame(data)

df.head(2)

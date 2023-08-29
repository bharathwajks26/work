import pandas as pd

data = {'customer_id': [1, 2, 3, 4, 5, 6, 7],
        'age': [25, 30, 22, 40, 30, 30, 25]}

df = pd.DataFrame(data)
freq = df['age'].value_counts().sort_index()

print("Age Frequency Distribution:")
print(freq)

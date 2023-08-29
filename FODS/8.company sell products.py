import pandas as pd

data = {
    'product_name': ['Product A', 'Product B', 'Product A', 'Product C', 'Product B', 'Product A', 'Product C'],
    'quantity': [100, 80, 70, 50, 120, 90, 60]
}
data1 = pd.DataFrame(data)
sales = data1.groupby('product_name')['quantity'].sum()
sorted = sales.sort_values(ascending=False)
top5 = sorted.head(5)
print("Top 5 products in the past month:")
print(top5)

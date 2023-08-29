import pandas as pd
data = {
    'customer ID': [101, 102, 101, 103, 104, 102, 101],
    'order date': ['2023-07-01', '2023-07-02', '2023-07-03', '2023-07-03', '2023-07-04', '2023-07-05', '2023-07-06'],
    'product name': ['A', 'B', 'A', 'C', 'B', 'A', 'C'],
    'order quantity': [3, 5, 2, 1, 2, 4, 3]
}
order = pd.DataFrame(data)
order['order date'] = pd.to_datetime(order['order date'])
total = order['customer ID'].value_counts()
ave = order.groupby('product name')['order quantity'].mean()
early = order['order date'].min()
latest = order['order date'].max()

print("Total number of orders made by each customer:")
print(total)
print("\nAverage order quantity for each product:")
print(ave)
print("\nEarliest order date:", early)
print("Latest order date:", latest)

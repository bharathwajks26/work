import numpy as np

scores = np.array([
    [85, 90, 78, 92],[95, 90, 78, 92],
    [76, 88, 95, 84],[92, 78, 88, 91],
    [89, 82, 85, 87],[99, 82, 85, 87],
    [76, 88, 95, 84],[92, 78, 88, 91],
    [79, 82, 85, 87],[89, 82, 85, 87],
    [85, 90, 78, 92],[85, 56, 78, 92],
    [46, 88, 95, 84],[92, 78, 88, 91],
    [89, 82, 85, 87],[89, 82, 85, 87],
    [76, 81, 95, 84],[92, 78, 88, 91],
    [89, 82, 85, 87],[89, 82, 85, 87],
    [85, 90, 78, 92],[85, 90, 78, 92],
    [76, 88, 95, 84],[92, 78, 88, 91],
    [89, 62, 85, 87],[89, 74, 85, 87],
    [76, 88, 50, 84],[92, 78, 88, 91],
    [89, 82, 85, 87],[89, 82, 85, 67],
    [85, 90, 78, 92],[85, 90, 78, 92],
    [76, 88, 95, 84],[92, 78, 68, 91],
    [89, 82, 85, 97],[89, 82, 85, 87],
    [56, 88, 95, 84],[92, 78, 88, 91],
    [89, 82, 85, 87],[39, 82, 85, 87],
])

names = ['sub1', 'sub2', 'sub3', 'sub4']  # Replace with actual subject names

avg = np.mean(scores, axis=0)

print("Average scores per subject:")
for subject, ave in zip(names, avg):
    print(f"{subject}: {ave:.2f}")

high = np.max(avg)
print("Highest average score:", high)

'''sample out put 
Average scores per subject:
sub1: 83.95
sub2: 82.28
sub3: 84.58
sub4: 87.95
Highest average score: 87.95
'''
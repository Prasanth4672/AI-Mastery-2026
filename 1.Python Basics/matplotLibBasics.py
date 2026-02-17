import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# # Basic Plot
# x = [1, 2, 3, 4, 5]
# y = [2, 3, 5, 7, 11]
# plt.plot(x, y)
# plt.title("Basic Plot")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.show()

# # Scatter Plot
# x = [1, 2, 3, 4, 5]
# y = [5, 7, 4, 6, 8]
# plt.scatter(x, y, color='red')
# plt.title("Scatter Plot")       
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.show()

# # Bar Chart
# categories = ['A', 'B', 'C', 'D']
# values = [5, 7, 3, 8]
# plt.bar(categories, values, color='green')
# plt.title("Bar Chart")
# plt.xlabel("Categories")
# plt.ylabel("Values")
# plt.show()

# # Histogram
# data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
# plt.hist(data, bins=5, color='blue', edgecolor='black')
# plt.title("Histogram")
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.show()

# Seaborn Heatmap
data = [[1, 2, 3], [4, 5, 6
], [7, 8, 9]]
sns.heatmap(data, annot=True, cmap='coolwarm')
plt.title("Seaborn Heatmap")
plt.show()# Line Plot with Seaborn
x = np.linspace(0, 10, 100)
y = np.sin(x)
sns.lineplot(x=x, y=y)
plt.title("Line Plot with Seaborn")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

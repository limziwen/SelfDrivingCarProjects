import numpy as np
import matplotlib.pyplot as plt

n_pts = 8
random_x1_values = np.random.normal(10, 2, n_pts)
## returns an array of random normally distributed numbers, median is 10, standard deviation is 2, with n_pts many data points
'''
random_x2_values = np.random.normal(12,2, n_pts)
## x = x1, y = x2 , in graph

top_region = np.array([random_x1_values, random_x2_values]).T
## each point has x1 and x2 values
##Transposed
bottom_region = np.array([np.random.normal(5, 2, n_pts), np.random.normal(6, 2, n_pts)]).T

_, ax = plt.subplots(figsize=(4,4))
ax.scatter(top_region[:, 0], top_region[:,1], color = 'r')
ax.scatter(bottom_region[:, 0], bottom_region[:,1], color = 'b')
plt.show()
'''

print(random_x1_values)

# 导入matplotlib框架中的pyplot方法
import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c='red', edgecolors='none', s=10)

# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置每个坐标轴的取值范围
plt.axis([0, 600, 0, 11000])

plt.show()
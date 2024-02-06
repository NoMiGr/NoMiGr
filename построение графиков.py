





import matplotlib.pyplot as plt

def plot_graph(x_values, y_values):
    plt.plot(x_values, y_values)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Simple Graph')
    plt.show()

# Пример использования функции
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plot_graph(x, y)



#Question 5: Plot Tesla Stock Graph

#Use the make_graph function to graph the Tesla Stock Data, also provide a title for the graph.

import matplotlib.pyplot as plt

def make_graph(data, x, y, title):
    plt.figure(figsize=(10,6))
    plt.plot(data[x], data[y], label=y)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()

# Call the function for Tesla stock data
make_graph(tesla_data, 'Date', 'Close', 'Tesla Stock Price')

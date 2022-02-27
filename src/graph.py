import matplotlib.pyplot as plt

# TODO Need to pass in x and y values
# TODO What is the best graph type for our purposes
"""
TODO I think we should have two 'types' of graphs: one graph that shows how one sorting algorithm 
fairs against each of the test cases and another where we see how one sorting algorithm fairs against
each of the different test cases. this would lead to n*m graphs with n being the number of sorting
algorithms and m being the different test cases
"""
def create_graph():
    GRAPH_TITLE = 'GRAPH TITLE'
    X_AXIS_LABEL = 'X AXIS LABEL'
    Y_AXIS_LABEL = 'Y AXIS LABEL'
    
    # x axis values
    x = [1, 2, 3, 4, 5, 6]
    # corresponding y axis values
    y = [2, 4, 1, 5, 2, 6]

    # plotting the points
    plt.plot(x, y, color='green', linestyle='dashed', linewidth=3,
            marker='o', markerfacecolor='blue', markersize=12)

    # setting x and y axis range
    plt.ylim(1, 8)
    plt.xlim(1, 8)

    # naming the x axis
    plt.xlabel(X_AXIS_LABEL)
    # naming the y axis
    plt.ylabel(Y_AXIS_LABEL)

    # giving a title to my graph
    plt.title(GRAPH_TITLE)

    # function to show the plot
    plt.show()

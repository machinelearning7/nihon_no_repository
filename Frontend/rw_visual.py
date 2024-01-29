import matplotlib.pyplot as plt

from random_walk import Randomwalk

# Keep making random walk as long as the program is active.
while True:
    # Make a random walk.
    rw = Randomwalk(50_000)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10, 6))
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors= 'none', s=1)

    # Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors= 'none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors= 'none', s=100)

    # Remove the axes
    ax.get_xaxis().set_visible(True)
    ax.get_yaxis().set_visible(True)
    plt.show() 

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break


   




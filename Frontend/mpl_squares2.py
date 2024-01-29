import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)
 
#Set chart title and lable axes

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

plt.show()



#we create a list called squares to hold the data that we'll plot,
#then we follow another common Matplotlib convention by calling the subplots() function
#this function can generate one or more plots in the same figure.
#the variable fig represents the entire figure or collection of plots that are generated
#the function plt.show() opens Matplotlib's viewer and displays the plot, as shown in Figure 15-1 p. 307
#the viewer allows you to zoom and navigate the plot and clicking on the disk icon can save plot images

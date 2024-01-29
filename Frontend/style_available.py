#ignore this, was supposed to be run from TERMINAL


import matplotlib.pyplot as plt
plt.style.available
['seaborn-dark', 'seaborn-darkgrid ', 'seaborn-ticks', 'fivethirtyeight']

input_values = [ 1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(input_values, squares, linewitdth=3)
plt.style. use('seaborn')



plt.show()
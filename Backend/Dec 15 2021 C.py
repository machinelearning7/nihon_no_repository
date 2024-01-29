alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

alien_0 = {'color': 'green', 'speed': 'slow'}
print(alien_0['points'])

#better to set a default value error 'No point value assigned'. Otherwise Py will return the value 'None'
alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)




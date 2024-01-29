# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['color'] = 'medium'
        alien['points'] = 10
            
# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")     
# doesn't seem to work output doesn't change, figured it out used == for yellow, medium and 10 (mistake)
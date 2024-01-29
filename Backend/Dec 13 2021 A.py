guests = ['mum', 'sis', 'eitan', 'dad']
print(guests)
first_guest = guests.pop(0)
print(f"\n{first_guest.title()}, you are invited to a dinner party. RSVP.")
second_guest = guests.pop(1)
print(f"\n{second_guest.title()}, you are invited to a dinner party. RSVP.")
#why did it skip 'sis'?
last_guest = guests.pop()
print(f"\n{last_guest.title()}, you are invited to a dinner party. RSVP.")

guests = ['mum', 'sis', 'eitan', 'dad']
print(guests)
guests.append('gombrich')
print(guests)
#using append to add to list
guests = ['mum', 'sis', 'eitan', 'dad']
print(guests)
guests.insert(0, 'gombrich')
print(guests)
guests = ['mum', 'sis', 'eitan', 'dad']
print(guests)
guests.insert(2, 'gombrich')
print(guests)
#inserted gombrich in middle of list depending on position 0,1,2,3,etc

 and



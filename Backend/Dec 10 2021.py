0.1 + 0.1
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print (bicycles[-1])
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)
friends = ['susan', 'lale', 'christine', 'carolyn', 'nicole']
print(friends)
print(friends[0])
print(friends[1].title())
print(friends[2].title())
message = f"My best friend is {friends[2].title()}."
print(message)


motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles.insert(2, 'ducati')
print(motorcycles)
motorcycles = ['honda','yamaha','suzuki']
del motorcycles[0]
print(motorcycles)
del motorcycles[1]
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcyle)



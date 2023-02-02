# create list
cars = ['maruti', 'hyundai', 'tata', 'honda']
print(cars)

# replace item
cars[3] = 'kia'
print(cars)
print(f'Last item in list is {cars[-1]}')

# iterate list
for car in cars:
    print(car)

# iterate list alternate way
i = 0
while i < len(cars):
    car = cars[i]
    print(car)
    i = i + 1

# empty list
colors = []
colors.append('red')
colors.append('green')
colors.append('blue')
colors.append('yellow')
print(colors)

# calculate average
numlist = list()
while True:
    inp = input("Enter a number: ")
    try:
        val = float(inp)
        numlist.append(val)
    except:
        if inp.lower() == 'done': break

print(f"Sum is: {sum(numlist)}, Average is: {sum(numlist) / len(numlist)}")

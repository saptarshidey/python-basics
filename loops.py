i = 10
while i > 0:
    if i % 2 == 0:  # even number
        print(i)
    i = i - 1

while True:
    line = input('>>> ')
    if line.startswith('#'):
        continue
    elif line.lower() == "exit" or line.lower() == "exit()":
        break
    print(line)

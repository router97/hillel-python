# Homework 6 - Vladyslav

print("type end to finish")

# task - Frame

while True:
    side = input("side: ")
    if not side == 'end' and int(side.isdigit()) == False:
        continue
    if side == 'end':
        exit()
    side = int(side)
    print("#"*side, "\n", ("#" + ' ' * (side-2) + '#\n') * (side-2) , "#"*side, sep = '')
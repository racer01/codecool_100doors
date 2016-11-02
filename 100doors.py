# 100doors

doors = []


# 2: 2, 4, 6, 8
# 3: 3, 6, 9
def OpenDoors(n):
    counter = n
    while counter < len(doors):
        doors[counter] = not doors[counter]
        counter += n


def main():
    for i in range(101):  # init; 101 because 0->100
        doors.append(False)

    for i in range(1, len(doors)):
        OpenDoors(i)
    opened = []
    for i in range(1, len(doors)):  # beautifying output
        if doors[i]:
            opened.append(str(i))
    print("The following doors are open:")
    print(", ".join(opened))
main()

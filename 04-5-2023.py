#  Python Code 
floor = "<<<<<<><><><><<<<><><><><><<<<><><><><><>>>><<><><><><><><><><>>>><<<<<><><><><><<<<<><><><><><><<<<><><><><><><><><><><><<<<<<><><<><><>>>< <>><<><<>><><<><><><><><><><<<<<<<<<>><<><><<<><><><><<<<<<>>>>>>>>>>> <>><><><>><<<><><><><<><><<><><><><><><><<<<><><><>><<>>>>><><><>><<<><><><><><><>><><><><><><><><><><><><><><><><><<<><><><><><><><><><><><><><><><><><>>>><><><><><><><><><>><<<<<<<<<<>>>>><<<<<>>>><<<<>><<><< ><><><><><><><><><><<<<<<<><><<><<><<><<><><><><><<>><><>><><><><><<>< <<<<>><<<<><><<<><>>><<><>>>>><>>><<><<><><><><<>><><><><><><><><><><> <><><><><><<<<><><<<<><<<>>>>>>>>><<><<<>>>>><<<<<<<<<>>>><<><>><><<>< <>><<>><<>><"
floors = floor.replace(" ", "")
result = 0
for i in floors:
    if i == '<':
        result += 1
    elif i == '>':
        result -= 1
print("He ended up on Floor", result)

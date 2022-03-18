map1 = [
    [12, 0, 1, 0],
    [1, 0, 1, 0],
    [1, 0, 1, 0],
    [1, 0, 0, 24]
]
map2 = [
    [12, 1, 0, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 0],
    [0, 0, 0, 24]
]
map = map2

# 1. step
current_position_x = 0
current_position_y = 0

print("Current current_position_y = ", current_position_y)
print("Current current_position_x = ", current_position_x)
can_move_right = map[current_position_y][current_position_x+1] == 0
can_move_bottom = map[current_position_y+1][current_position_x] == 0

if can_move_right:
    print("Should move right")
    current_position_x = current_position_x + 1
if can_move_bottom:
    print("Should move down")
    current_position_y = current_position_y + 1

# 2. step 2
print("Current current_position_y = ", current_position_y)
print("Current current_position_x = ", current_position_x)
can_move_right = map[current_position_y][current_position_x+1] == 0
can_move_bottom = map[current_position_y+1][current_position_x] == 0

if can_move_right:
    print("Should move right")
    current_position_x = current_position_x + 1
if can_move_bottom:
    print("Should move down")
    current_position_y = current_position_y + 1

    
# 3. step 3
print("Current current_position_y = ", current_position_y)
print("Current current_position_x = ", current_position_x)
can_move_right = map[current_position_y][current_position_x+1] == 0
can_move_bottom = map[current_position_y+1][current_position_x] == 0

if can_move_right:
    print("Should move right")
    current_position_x = current_position_x + 1
if can_move_bottom:
    print("Should move down")
    current_position_y = current_position_y + 1

# 4. step 4
print("Current current_position_y = ", current_position_y)
print("Current current_position_x = ", current_position_x)
can_move_right = map[current_position_y][current_position_x+1] == 0
can_move_bottom = map[current_position_y+1][current_position_x] == 0

if can_move_right:
    print("Should move right")
    current_position_x = current_position_x + 1
if can_move_bottom:
    print("Should move down")
    current_position_y = current_position_y + 1

# 5. step 5
print("Current current_position_y = ", current_position_y)
print("Current current_position_x = ", current_position_x)
can_move_right = map[current_position_y][current_position_x+1] == 0
can_move_bottom = map[current_position_y+1][current_position_x] == 0

if can_move_right:
    print("Should move right")
    current_position_x = current_position_x + 1
if can_move_bottom:
    print("Should move down")
    current_position_y = current_position_y + 1

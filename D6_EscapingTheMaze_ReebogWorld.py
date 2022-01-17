def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    while wall_in_front():
        turn_left()
    move()
    if not wall_on_right():
        turn_right()
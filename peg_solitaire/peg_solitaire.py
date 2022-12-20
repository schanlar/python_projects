"""
peg_solitaire.py
A simple Python approach to play the classic game peg solitaire
@author: Savvas Chanlaridis
@version: v2021-12-04
"""


def create_board():
    """
    This function creates a rectangular that contains all possible coordinates.
    Then it populates each coordinate with a value:
        - Occupied positions are represented with the value 1;
        - Non-occupied positions are represented with the value 0;
        - Forbidden position -> None value.

    It returns 3 list objects:
        - A 1D list with all possible coordinates (F4, G2, etc);
        - A 1D list with the corresponding values of each coordinate (1,0, or None type);
        - A 1D list with coordinates which correspond to forbidden areas of the board (A1, B6 etc)
    """

    x_axis_coordinates = ["1", "2", "3", "4", "5", "6", "7"]
    y_axis_coordinates = ["A", "B", "C", "D", "E", "F", "G"]

    forbidden_coordinates = [
        "A1",
        "A2",
        "B1",
        "B2",
        "F1",
        "F2",
        "G1",
        "G2",
        "A6",
        "A7",
        "B6",
        "B7",
        "F6",
        "F7",
        "G6",
        "G7",
    ]

    # Create a rectangular that contains all possible coordinates
    full_grid_coordinates = []
    for y in y_axis_coordinates:
        for x in x_axis_coordinates:
            full_grid_coordinates.append(y + x)

    # Initialize each coordinate with a meaningful value
    full_grid_values = []
    for coordinate in full_grid_coordinates:
        if coordinate in forbidden_coordinates:
            full_grid_values.append(None)
        elif coordinate == "D4":
            full_grid_values.append("0")
        else:
            full_grid_values.append("1")

    return full_grid_coordinates, full_grid_values, forbidden_coordinates


def display_board(board_values):
    """
    The function displays the game board
    with the current values
    """

    print("  1 2 3 4 5 6 7")
    print(
        "A     {} {} {}    ".format(board_values[2], board_values[3], board_values[4])
    )
    print(
        "B     {} {} {}    ".format(board_values[9], board_values[10], board_values[11])
    )
    print(
        "C {} {} {} {} {} {} {}".format(
            board_values[14],
            board_values[15],
            board_values[16],
            board_values[17],
            board_values[18],
            board_values[19],
            board_values[20],
        )
    )
    print(
        "D {} {} {} {} {} {} {}".format(
            board_values[21],
            board_values[22],
            board_values[23],
            board_values[24],
            board_values[25],
            board_values[26],
            board_values[27],
        )
    )
    print(
        "E {} {} {} {} {} {} {}".format(
            board_values[28],
            board_values[29],
            board_values[30],
            board_values[31],
            board_values[32],
            board_values[33],
            board_values[34],
        )
    )
    print(
        "F     {} {} {}    ".format(
            board_values[37], board_values[38], board_values[39]
        )
    )
    print(
        "G     {} {} {}    ".format(
            board_values[44], board_values[45], board_values[46]
        )
    )


def move_up(yx_start, board_coordinates, board_values):
    """
    This function moves up the y-position by two (y -> y+2)
    and returns the new values for the whole board.
    It assumes a valid input for the starting yx point on the board.
    """
    y_start = yx_start[0]
    x = yx_start[1]

    # Allowed y-positions from where you
    # can move upwards
    move_from_y = ["G", "F", "E", "D", "C"]

    # Corresponding terminal y-positions
    move_to_y = ["E", "D", "C", "B", "A"]

    # y-positions between initial and terminal y
    in_between = ["F", "E", "D", "C", "B"]

    for initial_y, terminal_y, in_between_y in zip(move_from_y, move_to_y, in_between):
        if initial_y == y_start:
            yx_end = terminal_y + x
            yx_between = in_between_y + x

    for idx, val in enumerate(board_coordinates):
        if val == yx_start:
            board_values[idx] = "0"
        if val == yx_between:
            board_values[idx] = "0"
        if val == yx_end:
            board_values[idx] = "1"

    return board_values


def check_move_up(start_yx, board_coordinates, board_values, verbatim=True):
    """
    This function checks if all the requirements for an upward movement are fulfilled.
    It returns True if the move can be executed, or False if there is an invalid move.
    """

    start_y = start_yx[0]
    x = start_yx[1]  # The x-coordinate remains the same in up-movement

    move_from_y = ["G", "F", "E", "D", "C"]
    in_between = ["F", "E", "D", "C", "B"]
    move_to_y = ["E", "D", "C", "B", "A"]

    # Flag variables
    value_at_start_ok = False
    value_at_end_ok = False
    value_in_between_ok = False
    can_move_upwards = False

    # Check if starting y-coordinate is
    # B or A -> cannot move upwards
    if start_y not in move_from_y:
        if verbatim:
            print("You cannot move up from here!")
        return can_move_upwards
    else:

        # Move from position y to position y+2
        for i, f, b in zip(move_from_y, move_to_y, in_between):
            if i == start_y:
                end_yx = f + x
                between_yx = b + x
                # print(end_yx, between_yx)

        # Check if the ending position is out of board
        # Check if the starting position has a peg
        # Check if the ending position has a peg
        # Check if the in-between position has a peg
        for coordinate, value in zip(board_coordinates, board_values):

            if (coordinate == start_yx) and (value == "1"):
                # print('Value at start ok!')
                value_at_start_ok = True

            if (coordinate == end_yx) and (value is None):
                if verbatim:
                    print("Moving peg will fall out of bounds!")
                return can_move_upwards

            if (coordinate == end_yx) and (value == "0"):
                # print('Value at end ok!')
                value_at_end_ok = True

            if (coordinate == between_yx) and (value == "1"):
                # print('Value in between ok!')
                value_in_between_ok = True

        if (value_at_start_ok) and (value_in_between_ok) and (value_at_end_ok):
            can_move_upwards = True
            return can_move_upwards
        elif not value_at_start_ok:
            if verbatim:
                print("Given peg position does not have a peg!")
            return can_move_upwards
        elif not value_in_between_ok:
            if verbatim:
                print("No peg at next position to jump over!")
            return can_move_upwards
        elif not value_at_end_ok:
            if verbatim:
                print("Landing position is occupied!")
            return can_move_upwards


def move_down(yx_start, board_coordinates, board_values):
    """
    This function moves down the y-position by two (y -> y-2)
    and returns the new values for the whole board.
    It assumes a valid input for the starting yx point on the board.
    """
    y_start = yx_start[0]
    x = yx_start[1]

    # Allowed y-positions from where you
    # can move downwards
    move_from_y = ["A", "B", "C", "D", "E"]

    # Corresponding terminal y-positions
    move_to_y = ["C", "D", "E", "F", "G"]

    # y-positions between initial and terminal y
    in_between = ["B", "C", "D", "E", "F"]

    for initial_y, terminal_y, in_between_y in zip(move_from_y, move_to_y, in_between):
        if initial_y == y_start:
            yx_end = terminal_y + x
            yx_between = in_between_y + x

    for idx, val in enumerate(board_coordinates):
        if val == yx_start:
            board_values[idx] = "0"
        if val == yx_between:
            board_values[idx] = "0"
        if val == yx_end:
            board_values[idx] = "1"

    return board_values


def check_move_down(start_yx, board_coordinates, board_values, verbatim=True):
    """
    This function checks if all the requirements for an downward movement are fulfilled.
    It returns True if the move can be executed, or False if there is an invalid move.
    """

    start_y = start_yx[0]
    x = start_yx[1]  # The x-coordinate remains the same in down-movement

    move_from_y = ["A", "B", "C", "D", "E"]
    in_between = ["B", "C", "D", "E", "F"]
    move_to_y = ["C", "D", "E", "F", "G"]

    # Flag variables
    value_at_start_ok = False
    value_at_end_ok = False
    value_in_between_ok = False
    can_move_downwards = False

    # Check if starting y-coordinate is
    # F or G -> cannot move upwards
    if start_y not in move_from_y:
        if verbatim:
            print("You cannot move down from here!")
        return can_move_downwards
    else:

        # Move from position y to position y-2
        for i, f, b in zip(move_from_y, move_to_y, in_between):
            if i == start_y:
                end_yx = f + x
                between_yx = b + x
                # print(end_yx, between_yx)

        # Check if the ending position is out of board
        # Check if the starting position has a peg
        # Check if the ending position has a peg
        # Check if the in-between position has a peg
        for coordinate, value in zip(board_coordinates, board_values):

            if (coordinate == start_yx) and (value == "1"):
                # print('Value at start ok!')
                value_at_start_ok = True

            if (coordinate == end_yx) and (value is None):
                if verbatim:
                    print("Moving peg will fall out of bounds!")
                return can_move_downwards

            if (coordinate == end_yx) and (value == "0"):
                # print('Value at end ok!')
                value_at_end_ok = True

            if (coordinate == between_yx) and (value == "1"):
                # print('Value in between ok!')
                value_in_between_ok = True

        if (value_at_start_ok) and (value_in_between_ok) and (value_at_end_ok):
            can_move_downwards = True
            return can_move_downwards
        elif not value_at_start_ok:
            if verbatim:
                print("Given peg position does not have a peg!")
            return can_move_downwards
        elif not value_in_between_ok:
            if verbatim:
                print("No peg at next position to jump over!")
            return can_move_downwards
        elif not value_at_end_ok:
            if verbatim:
                print("Landing position is occupied!")
            return can_move_downwards


def move_right(yx_start, board_coordinates, board_values):
    """
    This function moves right the x-position by two (x -> x+2)
    and returns the new values for the whole board.
    It assumes a valid input for the starting yx point on the board.
    """
    y = yx_start[0]
    x_start = yx_start[1]

    # Allowed x-positions from where you
    # can move right
    move_from_x = ["1", "2", "3", "4", "5"]

    # Corresponding terminal x-positions
    move_to_x = ["3", "4", "5", "6", "7"]

    # x-positions between initial and terminal x
    in_between = ["2", "3", "4", "5", "6"]

    for initial_x, terminal_x, in_between_x in zip(move_from_x, move_to_x, in_between):
        if initial_x == x_start:
            yx_end = y + terminal_x
            yx_between = y + in_between_x

    for idx, val in enumerate(board_coordinates):
        if val == yx_start:
            board_values[idx] = "0"
        if val == yx_between:
            board_values[idx] = "0"
        if val == yx_end:
            board_values[idx] = "1"

    return board_values


def check_move_right(start_yx, board_coordinates, board_values, verbatim=True):
    """
    This function checks if all the requirements for a right movement are fulfilled.
    It returns True if the move can be executed, or False if there is an invalid move.
    """

    y = start_yx[0]  # The y-coordinate remains the same in right-movement
    start_x = start_yx[1]

    move_from_x = ["1", "2", "3", "4", "5"]
    in_between = ["2", "3", "4", "5", "6"]
    move_to_x = ["3", "4", "5", "6", "7"]

    # Flag variables
    value_at_start_ok = False
    value_at_end_ok = False
    value_in_between_ok = False
    can_move_right = False

    # Check if starting x-coordinate is
    # 6 or 7 -> cannot move right
    if start_x not in move_from_x:
        if verbatim:
            print("You cannot move right from here!")
        return can_move_right
    else:

        # Move from position x to position x+2
        for i, f, b in zip(move_from_x, move_to_x, in_between):
            if i == start_x:
                end_yx = y + f
                between_yx = y + b
                # print(end_yx, between_yx)

        # Check if the ending position is out of board
        # Check if the starting position has a peg
        # Check if the ending position has a peg
        # Check if the in-between position has a peg
        for coordinate, value in zip(board_coordinates, board_values):

            if (coordinate == start_yx) and (value == "1"):
                # print('Value at start ok!')
                value_at_start_ok = True

            if (coordinate == end_yx) and (value is None):
                if verbatim:
                    print("Moving peg will fall out of bounds!")
                return can_move_right

            if (coordinate == end_yx) and (value == "0"):
                # print('Value at end ok!')
                value_at_end_ok = True

            if (coordinate == between_yx) and (value == "1"):
                # print('Value in between ok!')
                value_in_between_ok = True

        if (value_at_start_ok) and (value_in_between_ok) and (value_at_end_ok):
            can_move_right = True
            return can_move_right
        elif not value_at_start_ok:
            if verbatim:
                print("Given peg position does not have a peg!")
            return can_move_right
        elif not value_in_between_ok:
            if verbatim:
                print("No peg at next position to jump over!")
            return can_move_right
        elif not value_at_end_ok:
            if verbatim:
                print("Landing position is occupied!")
            return can_move_right


def move_left(yx_start, board_coordinates, board_values):
    """
    This function moves left the x-position by two (x -> x-2)
    and returns the new values for the whole board.
    It assumes a valid input for the starting yx point on the board.
    """
    y = yx_start[0]
    x_start = yx_start[1]

    # Allowed x-positions from where you
    # can move left
    move_from_x = ["7", "6", "5", "4", "3"]

    # Corresponding terminal x-positions
    move_to_x = ["5", "4", "3", "2", "1"]

    # x-positions between initial and terminal x
    in_between = ["6", "5", "4", "3", "2"]

    for initial_x, terminal_x, in_between_x in zip(move_from_x, move_to_x, in_between):
        if initial_x == x_start:
            yx_end = y + terminal_x
            yx_between = y + in_between_x

    for idx, val in enumerate(board_coordinates):
        if val == yx_start:
            board_values[idx] = "0"
        if val == yx_between:
            board_values[idx] = "0"
        if val == yx_end:
            board_values[idx] = "1"

    return board_values


def check_move_left(start_yx, board_coordinates, board_values, verbatim=True):
    """
    This function checks if all the requirements for a left movement are fulfilled.
    It returns True if the move can be executed, or False if there is an invalid move.
    """

    y = start_yx[0]  # The y-coordinate remains the same in right-movement
    start_x = start_yx[1]

    move_from_x = ["7", "6", "5", "4", "3"]
    in_between = ["6", "5", "4", "3", "2"]
    move_to_x = ["5", "4", "3", "2", "1"]

    # Flag variables
    value_at_start_ok = False
    value_at_end_ok = False
    value_in_between_ok = False
    can_move_left = False

    # Check if starting x-coordinate is
    # 1 or 2 -> cannot move right
    if start_x not in move_from_x:
        if verbatim:
            print("You cannot move left from here!")
        return can_move_left
    else:

        # Move from position x to position x+2
        for i, f, b in zip(move_from_x, move_to_x, in_between):
            if i == start_x:
                end_yx = y + f
                between_yx = y + b
                # print(end_yx, between_yx)

        # Check if the ending position is out of board
        # Check if the starting position has a peg
        # Check if the ending position has a peg
        # Check if the in-between position has a peg
        for coordinate, value in zip(board_coordinates, board_values):

            if (coordinate == start_yx) and (value == "1"):
                # print('Value at start ok!')
                value_at_start_ok = True

            if (coordinate == end_yx) and (value is None):
                if verbatim:
                    print("Moving peg will fall out of bounds!")
                return can_move_left

            if (coordinate == end_yx) and (value == "0"):
                # print('Value at end ok!')
                value_at_end_ok = True

            if (coordinate == between_yx) and (value == "1"):
                # print('Value in between ok!')
                value_in_between_ok = True

        if (value_at_start_ok) and (value_in_between_ok) and (value_at_end_ok):
            can_move_left = True
            return can_move_left
        elif not value_at_start_ok:
            if verbatim:
                print("Given peg position does not have a peg!")
            return can_move_left
        elif not value_in_between_ok:
            if verbatim:
                print("No peg at next position to jump over!")
            return can_move_left
        elif not value_at_end_ok:
            if verbatim:
                print("Landing position is occupied!")
            return can_move_left


def remaining_moves(board_coordinates, board_values, show_help=True):
    """
    This function checks if there are any remaining moves left.
    It gives the option to show how many moves are available in
    each direction if show_help is enabled.
    """

    can_move_up = False
    can_move_down = False
    can_move_right = False
    can_move_left = False

    up_counter, down_counter, right_counter, left_counter = 0, 0, 0, 0

    for coordinate in board_coordinates:
        if check_move_up(
            coordinate,
            board_coordinates=board_coordinates,
            board_values=board_values,
            verbatim=False,
        ):
            can_move_up = True
            up_counter += 1

        if check_move_down(
            coordinate,
            board_coordinates=board_coordinates,
            board_values=board_values,
            verbatim=False,
        ):
            can_move_down = True
            down_counter += 1

        if check_move_right(
            coordinate,
            board_coordinates=board_coordinates,
            board_values=board_values,
            verbatim=False,
        ):
            can_move_right = True
            right_counter += 1

        if check_move_left(
            coordinate,
            board_coordinates=board_coordinates,
            board_values=board_values,
            verbatim=False,
        ):
            can_move_left = True
            left_counter += 1

    if can_move_up or can_move_down or can_move_right or can_move_left:
        if show_help:
            print("\n" + "Available moves:")
            print("--" * 10)
            print("UP MOVEMENTS: {}".format(up_counter))
            print("DOWN MOVEMENTS: {}".format(down_counter))
            print("RIGHT MOVEMENTS: {}".format(right_counter))
            print("LEFT MOVEMENTS: {}".format(left_counter))
            print("--" * 10)
        return True
    else:
        return False


def peg_counter(board_values):
    """
    This function counts the number of existing pegs
    on the board.
    """
    total_pegs = 0
    for peg in board_values:
        if peg == "1":
            total_pegs += 1

    return total_pegs


def main():

    direction_options = ["U", "D", "R", "L"]

    yx_coordinates, yx_values, yx_forbidden_coordinates = create_board()
    display_board(yx_values)

    while remaining_moves(board_coordinates=yx_coordinates, board_values=yx_values):
        user_move = input(
            "Enter peg position followed by move (L, R, U, or D): "
        ).upper()

        # Check if the length of the alpharithmetic is at least 3
        # so it can be parsed to coordinate + direction
        if len(user_move) != 3:
            # In this case ignore the rest of code and
            # continue with the next iteration
            print("Something wrong with your input!")
            continue

        start_from_coordinate = user_move[0] + user_move[1]
        direction = user_move[2].upper()

        # Check if input is out of board, invalid, or has a wrong direction
        input_is_valid = False
        direction_is_valid = False
        while True:
            if start_from_coordinate in yx_forbidden_coordinates:
                print("Given peg position is out of board!")
                user_move = input(
                    "Enter peg position followed by move (L, R, U, or D): "
                ).upper()
                start_from_coordinate = user_move[0] + user_move[1]
                direction = user_move[2].upper()
            elif start_from_coordinate not in yx_coordinates:
                print("Something wrong with your input!")
                user_move = input(
                    "Enter peg position followed by move (L, R, U, or D): "
                ).upper()
                start_from_coordinate = user_move[0] + user_move[1]
                direction = user_move[2].upper()
            else:
                input_is_valid = True

            if direction in direction_options:
                direction_is_valid = True
            else:
                print("Direction is not L or R or U or D!")
                user_move = input(
                    "Enter peg position followed by move (L, R, U, or D): "
                ).upper()
                start_from_coordinate = user_move[0] + user_move[1]
                direction = user_move[2].upper()

            if input_is_valid and direction_is_valid:
                break

        # Check if the move is valid
        ok_to_move = False
        while not ok_to_move:

            if user_move.endswith("U"):  # This can also be written as direction == 'U'
                ok_to_move = check_move_up(
                    start_from_coordinate,
                    board_coordinates=yx_coordinates,
                    board_values=yx_values,
                )
                if ok_to_move:
                    # Update the board values after the movement
                    yx_values = move_up(
                        start_from_coordinate,
                        board_coordinates=yx_coordinates,
                        board_values=yx_values,
                    )
                    display_board(yx_values)
                else:
                    user_move = input(
                        "Enter peg position followed by move (L, R, U, or D): "
                    ).upper()
                    start_from_coordinate = user_move[0] + user_move[1]
                    direction = user_move[2].upper()

            elif user_move.endswith(
                "D"
            ):  # This can also be written as direction == 'D'
                ok_to_move = check_move_down(
                    start_from_coordinate,
                    board_coordinates=yx_coordinates,
                    board_values=yx_values,
                )
                if ok_to_move:
                    # Update the board values after the movement
                    yx_values = move_down(
                        start_from_coordinate,
                        board_coordinates=yx_coordinates,
                        board_values=yx_values,
                    )
                    display_board(yx_values)
                else:
                    user_move = input(
                        "Enter peg position followed by move (L, R, U, or D): "
                    ).upper()
                    start_from_coordinate = user_move[0] + user_move[1]
                    direction = user_move[2].upper()

            elif user_move.endswith(
                "R"
            ):  # This can also be written as direction == 'R'
                ok_to_move = check_move_right(
                    start_from_coordinate,
                    board_coordinates=yx_coordinates,
                    board_values=yx_values,
                )
                if ok_to_move:
                    # Update the board values after the movement
                    yx_values = move_right(
                        start_from_coordinate,
                        board_coordinates=yx_coordinates,
                        board_values=yx_values,
                    )
                    display_board(yx_values)
                else:
                    user_move = input(
                        "Enter peg position followed by move (L, R, U, or D): "
                    ).upper()
                    start_from_coordinate = user_move[0] + user_move[1]
                    direction = user_move[2].upper()

            elif user_move.endswith(
                "L"
            ):  # This can also be written as direction == 'L'
                ok_to_move = check_move_left(
                    start_from_coordinate,
                    board_coordinates=yx_coordinates,
                    board_values=yx_values,
                )
                if ok_to_move:
                    # Update the board values after the movement
                    yx_values = move_left(
                        start_from_coordinate,
                        board_coordinates=yx_coordinates,
                        board_values=yx_values,
                    )
                    display_board(yx_values)
                else:
                    user_move = input(
                        "Enter peg position followed by move (L, R, U, or D): "
                    ).upper()
                    start_from_coordinate = user_move[0] + user_move[1]
                    direction = user_move[2].upper()

    print("No more moves. The number of remaining pegs is:", peg_counter(yx_values))


if __name__ == "__main__":
    main()

import time
import os
import sys

sys.path.append('./cpp')  # Ensure the cpp directory is in the PYTHONPATH

if os.name == 'posix':
    from cpp import a_star_parking_module  # Import the Linux version
elif os.name == 'nt':
    # from cpp import a_star as  a_star_parking_module# Import the Windows version
    # import ctypes
    # ctypes.CDLL("a_star.dll")
    # import ctypes

    # current_directory = os.getcwd()  # This gets the current directory where your script is running
    # dll_path = os.path.join(current_directory, 'cpp', 'a_start.pyd')  # This constructs the full path to the DLL
    # ctypes.CDLL(dll_path)
    pass
else:
    raise EnvironmentError("Unsupported OS")


def parking_spaces_to_ids_for_cpp(parking_spaces):
    return [
        [space.car.id if space.car is not None else -1 for space in row]
        for row in parking_spaces
    ]


def move_car_to_destination_cpp(parking_spaces, destination, id):
    start_state = parking_spaces_to_ids_for_cpp(parking_spaces)
    target_car_id = id
    
    start_time = time.time()

    # Call the a_star_parking function from your C++ module
    moves = a_star_parking_module.a_star_parking(start_state, target_car_id, destination)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time for Cpp version: {elapsed_time} seconds")

    for move in moves:
        direction, (src_x, src_y), (dest_x, dest_y) = move

        if direction == 'right':
            parking_spaces[src_x][src_y].car.move_right()
        elif direction == 'up':
            parking_spaces[src_x][src_y].car.move_up()
        elif direction == 'left':
            parking_spaces[src_x][src_y].car.move_left()
        elif direction == 'down':
            parking_spaces[src_x][src_y].car.move_down()

    return moves

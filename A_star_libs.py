import time
import os
import sys

sys.path.append('./cpp')  # Ensure the cpp directory is in the PYTHONPATH

if os.name == 'posix':
    #linux
    from cpp import a_star_parking_module
    from rust import a_star_parking_module_rust
elif os.name == 'nt':
    #windows
    #from rust import a_star_parking_module_rust
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
    
    parking_spaces[destination[0]][destination[1]].setAsDestination()

    start_time_calculation = time.time()

    # Call the a_star_parking function from your C++ module
    moves = a_star_parking_module.a_star_parking(start_state, target_car_id, destination)

    end_time_calculation = time.time()
    elapsed_time_calculation = end_time_calculation - start_time_calculation
    print(f"Elapsed time for Cpp version: {end_time_calculation} seconds")

    # start_time_moving = time.time()

    # for move in moves:
    #     direction, (src_x, src_y), (dest_x, dest_y) = move

    #     if direction == 'right':
    #         parking_spaces[src_x][src_y].car.move_right()
    #     elif direction == 'up':
    #         parking_spaces[src_x][src_y].car.move_up()
    #     elif direction == 'left':
    #         parking_spaces[src_x][src_y].car.move_left()
    #     elif direction == 'down':
    #         parking_spaces[src_x][src_y].car.move_down()

    # end_time_moving = time.time()
    # elapsed_time_moving = end_time_moving - start_time_moving

    # parking_spaces[destination[0]][destination[1]].unsetAsDestination()

    return moves, elapsed_time_calculation, #elapsed_time_moving


def move_car_to_destination_rust(parking_spaces, destination, id):
    start_state = parking_spaces_to_ids_for_cpp(parking_spaces)
    target_car_id = id
    
    parking_spaces[destination[0]][destination[1]].setAsDestination()

    start_time_calculation = time.time()

    # Call the a_star_parking function from your Rust module
    moves = a_star_parking_module_rust.a_star_parking_py(start_state, target_car_id, destination)

    end_time_calculation = time.time()
    elapsed_time_calculation = end_time_calculation - start_time_calculation
    print(f"Elapsed time for Rust version: {elapsed_time_calculation} seconds")

    # start_time_moving = time.time()

    # for move in moves:
    #     direction, (src_x, src_y), (dest_x, dest_y) = move

    #     if direction == 'right':
    #         parking_spaces[src_x][src_y].car.move_right()
    #     elif direction == 'up':
    #         parking_spaces[src_x][src_y].car.move_up()
    #     elif direction == 'left':
    #         parking_spaces[src_x][src_y].car.move_left()
    #     elif direction == 'down':
    #         parking_spaces[src_x][src_y].car.move_down()

    # end_time_moving = time.time()
    # elapsed_time_moving = end_time_moving - start_time_moving

    # parking_spaces[destination[0]][destination[1]].unsetAsDestination()

    return moves, elapsed_time_calculation, #elapsed_time_moving


def free_up_space_rust(parking_spaces, destination):
    start_state = parking_spaces_to_ids_for_cpp(parking_spaces)
    target_car_id = -1

    start_time_calculation = time.time()

    # Call the a_star_parking function from your Rust module
    moves = a_star_parking_module_rust.a_star_parking_py(start_state, target_car_id, destination)

    end_time_calculation = time.time()
    elapsed_time_calculation = end_time_calculation - start_time_calculation
    print(f"Elapsed time for freeing up space Rust version: {elapsed_time_calculation} seconds")

    start_time_moving = time.time()

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

    end_time_moving = time.time()
    elapsed_time_moving = end_time_moving - start_time_moving


    return moves, elapsed_time_calculation, elapsed_time_moving

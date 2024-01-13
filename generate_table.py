from functools import partial

import numpy as np

from check_trajectory import check_trajectory

release_angles_range = np.arange(30, 60, 2) # degrees
distances_range = np.arange(0.5, 8, 0.1) # metres
release_velocities_range = np.arange(1, 15, 0.1) # metres per second

def determine_optimal_velocity(distance: float, release_angle: float) -> float:
    viable_velocities = filter(release_velocities_range,
                               partial(check_velocity, distance=distance,
                                       release_angle=release_angle))

    if len(viable_velocities) == 0:
        raise 'No posible trajectories'

    return sum(viable_velocities) / len(viable_velocities)

if __name__ == '__main__':
    for distance in distances_range:
        for release_angle in relese_angles_range:
            print(distance, release_angle, determine_optimal_velocity(distance, release_angle))
    
    print('Hello, world!')

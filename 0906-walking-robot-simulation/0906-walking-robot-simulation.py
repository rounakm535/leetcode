class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        """
        Returns the maximum Euclidean distance squared that the robot ever gets from the origin.
        """
        # Initialize the robot's position and direction
        x, y = 0, 0
        dx, dy = 0, 1  # initial direction is north (0, 1)

        # Create a set of obstacles for fast lookup
        obstacle_set = set(tuple(obstacle) for obstacle in obstacles)

        # Initialize the maximum distance squared
        max_distance_squared = 0

        # Iterate over the commands
        for command in commands:
            if command == -2:  # turn left
                dx, dy = -dy, dx
            elif command == -1:  # turn right
                dx, dy = dy, -dx
            else:  # move forward
                for _ in range(command):
                    new_x, new_y = x + dx, y + dy
                    if (new_x, new_y) not in obstacle_set:
                        x, y = new_x, new_y
                    else:
                        break
                    # Update the maximum distance squared
                    max_distance_squared = max(max_distance_squared, x**2 + y**2)

        return max_distance_squared
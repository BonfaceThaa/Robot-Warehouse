grid = []
# function to populate the grid
for i in range(0, 10):
    k = []
    for j in range(0, 10):
        k.append(j)
    grid.append(k)


class Robot:
    """
    class representing the robot object.
    """

    def __init__(self, current_position):
        self.current_position = current_position
        self.carried_crate_id = 0

    def move_commands(self, commands):
        """
        Function to take commands for moving robot.
        """
        commands_list = commands.split(" ")
        for i in commands_list:
            print("Current Command: ", i)
            self.move_robot(i)

    def boundary_check(self, position):
        """
        check if position is within the grid.
        """
        if 0 <= position[0] <= 9 and 0 <= position[1] <= 9:
            return True
        else:
            return False

    def move_robot(self, direction):
        """
        use current position of robot to move one step in the provided direction.
        """
        if direction == 'E' or direction == 'W':
            self.move_horizontally(direction)
        elif direction == 'N' or direction == 'S':
            self.move_vertically(direction)
        else:
            print('Please provide a correct direction')

    def move_horizontally(self, direction):
        """
        Function to move robot horizontally
        """
        y = self.current_position[1]

        if direction == 'E':
            if self.boundary_check([self.current_position[0], y+1]):
                self.current_position[1] += 1
            else:
                print("Out of grid space request")

        else:
            if self.boundary_check([self.current_position[0], y-1]):
                self.current_position[1] -= 1
            else:
                print("Out of grid space request")

    def move_vertically(self, direction):
        """
        function to move robot vertically
        """
        x = self.current_position[0]
        if direction == 'S':
            if self.boundary_check([x+1, self.current_position[1]]):
                self.current_position[0] += 1
            else:
                print("Out of grid space request")
        else:
            if self.boundary_check([x - 1, self.current_position[1]]):
                self.current_position[0] -= 1
            else:
                print("Out of grid space request")

    def claw_commands(self, command):
        """
        Function to take commands for claw of the robot
        """
        crate_id = 0

        if command == 'G' and self.carried_crate_id == 0:
            for k,v in Crate.crates.items():
                if self.current_position == v:
                    self.carried_crate_id = k

        elif command == 'D' and self.carried_crate_id != 0:
            if self.current_position not in Crate.crates.values():
                Crate.update_location(id=self.carried_crate_id, position=self.current_position)
                self.carried_crate_id = 0


class Crate:
    """
    class representing a crate object
    """
    crates = {}

    def __init__(self, id, position):
        self.id = id
        self.position = position
        self.crates[self.id] = self.position

    @staticmethod
    def update_location(id, position):
        """
        function to update crate location based on new grid position
        """
        Crate.crates[id] = position


if __name__ == "__main__":
    c1 = Crate(1, [5, 5])
    c1 = Crate(2, [0, 9])
    # r1 = Robot([9, 0])
    # r1.move_commands('N N N N E E E E E')
    # r1.claw_commands('G')
    # r1.move_commands('S W S')
    # r1.claw_commands('D')
    # print("Crates positions", c1.crates)
    # print("Robot position: ", r1.current_position)



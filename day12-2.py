from dataclasses import dataclass


@dataclass
class Waypoint():
    x: int = 0
    y: int = 0

    def translate(self, x, y):
        self.x += x
        self.y += y

    def rotate(self, clockwise):

        if clockwise:
            rotated_x = self.y * -1
            rotated_y = self.x
        else:
            rotated_x = self.y
            rotated_y = self.x * -1

        self.x = rotated_x
        self.y = rotated_y

    def move_forward(self, amount):
        cases = {
            0: self.move_north,
            90: self.move_east,
            180: self.move_south,
            -180: self.move_south,
            270: self.move_west,
            -90: self.move_west,
            -270: self.move_east,
        }

        cases[self.rotation](amount)

    def move_north(self, amount):
        print('move north', amount)
        self.translate(0, -amount)

    def move_south(self, amount):
        print('move south', amount)
        self.translate(0, amount)

    def move_east(self, amount):
        print('move east', amount)
        self.translate(amount, 0)

    def move_west(self, amount):
        print('move west', amount)
        self.translate(-amount, 0)

@dataclass
class Ferry(Waypoint):
    waypoint:Waypoint = Waypoint(x=10, y=-1)

    def rotate(self, rot):
        raise NotImplementedError

    def move_forward(self, amount):
        raise NotImplementedError

    def move_north(self, amount):
        super().move_north(amount)
        self.waypoint.move_north(amount)

    def move_south(self, amount):
        super().move_south(amount)
        self.waypoint.move_south(amount)

    def move_east(self, amount):
        super().move_east(amount)
        self.waypoint.move_east(amount)

    def move_west(self, amount):
        super().move_west(amount)
        self.waypoint.move_west(amount)

    def move_forward(self, times):

        self.x += self.waypoint.x * times
        self.y += self.waypoint.y * times

    def follow_instructions(self, instructions):

        def rotate_right(rotation):
            for i in range(int(rotation/90)):
                self.waypoint.rotate(True)

        def rotate_left(rotation):
            for i in range(int(rotation/90)):
                self.waypoint.rotate(False)


        instructions_map = {
            'N': self.waypoint.move_north,
            'S': self.waypoint.move_south,
            'E': self.waypoint.move_east,
            'W': self.waypoint.move_west,
            'L': rotate_left,
            'R': rotate_right,
            'F': self.move_forward,
        }

        for i in instructions:
            instructions_map[i[0]](i[1])

def get_instructions():
    return [(line[0], int(line[1:])) for line in open('day12-input.txt')]

def main():
    instructions = get_instructions()

    ferry = Ferry()
    ferry.follow_instructions(instructions)

    end_x = ferry.x
    end_y = ferry.y

    print('end X', end_x)
    print('end Y', end_y)
    print('result', abs(end_x + end_y))

def main_debug():
    ferry = Ferry()

    ferry.follow_instructions()
    ferry.move_forward(10)

    print(ferry)
    print(ferry.waypoint)

    ferry.waypoint.move_north(3)
    print(ferry)
    print(ferry.waypoint)

    ferry.move_forward(7)

    print(ferry)
    print(ferry.waypoint)

    ferry.waypoint.rotate(True)

    print(ferry)
    print(ferry.waypoint)

    ferry.move_forward(11)

    print(ferry)
    print(ferry.waypoint)

if __name__ == "__main__":
    main()
    # main_debug()
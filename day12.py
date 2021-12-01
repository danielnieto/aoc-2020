from dataclasses import dataclass


@dataclass
class Ferry():
    x: int = 0
    y: int = 0
    rotation: int = 90

    def translate(self, x, y):
        self.x +=  x
        self.y += y

    def rotate(self, rot):
        self.rotation += rot

        if self.rotation >= 360:
            self.rotation -= 360

        if self.rotation <= -360:
            self.rotation += 360

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

    def follow_instructions(self, instructions):
        instructions_map = {
            'N': self.move_north,
            'S': self.move_south,
            'E': self.move_east,
            'W': self.move_west,
            'L': lambda rot: self.rotate(-rot),
            'R': lambda rot: self.rotate(rot),
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


if __name__ == "__main__":
    main()
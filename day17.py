def get_input():
    mat = []
    for line in open('day17-sample.txt'):
        mat.append([c for c in line.strip()])

    return mat

def initialize_z(mat, index, dimension):
    mat.insert(index, [['.']*dimension]*dimension)

def get_neighbors(x,y,z, mat):
    neighbors = []
    for iz in range(z-1, z+2):
        for iy in range(y-1, y+2):
            for ix in range(x-1, x+2):
                if z not in mat:
                    initialize_z(mat, z, len(mat[0]))


    return []


def main():
    mat = []
    mat.insert(0, get_input())
    print(get_neighbors(0,0,0, mat))


if __name__ == "__main__":
    main()
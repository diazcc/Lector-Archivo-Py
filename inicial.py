import sys

def showLines(file, n):
    try:
        with open(file, 'r') as file:
            for i, line in enumerate(file, 1):
                if i > n:
                    break
                print(line, end='')

    except FileNotFoundError:
        print(f'El archivo "{file}" no se encontró.')

if __name__ == "__main__":
    if len(sys.argv) == 3:
        file = sys.argv[1]
        n = int(sys.argv[2])
        showLines(file, n)

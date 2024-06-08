import argparse
from generator import Generator

def main():
    parser = argparse.ArgumentParser(description='Generate Mega Million numbers.')
    parser.add_argument('-n', '--number_of_draw', type=int, required=True, help='Number of draws to generate.')
    parser.add_argument('-w', '--avoid_numbers_white', nargs='*', type=int, default=[], help='White numbers to avoid.')
    parser.add_argument('-y', '--avoid_numbers_yellow', nargs='*', type=int, default=[], help='Yellow numbers to avoid.')
    parser.add_argument('-d', '--duplicate_number', action='store_true', help='Allow duplicate numbers across all sets.')

    args = parser.parse_args()

    generator = Generator(args.number_of_draw, args.avoid_numbers_white, args.avoid_numbers_yellow, args.duplicate_number)
    result = generator.generate()

    for draw in result:
        print(f"White: {draw[:-1]}, Yellow: {draw[-1]}")

if __name__ == "__main__":
    main()
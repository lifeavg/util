import random
import argparse

def nif_letter(num: int) -> str:
    return "TRWAGMYFPDXBNJZSQVHLCKE"[num % 23]

def dni(num: int) -> str:
    return f'{num}{nif_letter(num)}'

def random_dni() -> str:
    return dni(random.randint(10000000, 100000000))

def nie(num_first: int, num: int) -> str:
    return f'{"XYZ"[num_first]}{num}{nif_letter(int(str(num_first) + str(num)))}'

def random_nie() -> str:
    return nie(random.randint(0, 3), random.randint(1000000, 10000000))

def main() -> None:
    parser = argparse.ArgumentParser(
    prog='esdoc',
    description='dni/nie generator')
    parser.add_argument('-dni', '-d', metavar='N', type=int, nargs=1,
                       help='Generate DNI from number in range [10000000, 100000000)')
    parser.add_argument('-dni-rand', '-dr', action='store_true',
                       help='Generate random DNI')
    parser.add_argument('-nie', '-n', metavar='N', type=int, nargs=2,
                       help='Generate NIE from numbers where first: 0:X, '
                            '1:Y, 2:Z; second in range [1000000, 10000000)')
    parser.add_argument('-nie-rand', '-nr', action='store_true',
                       help='Generate random NIE')

    args = parser.parse_args()

    if args.dni:
        if 100000000 <= args.dni[0] or args.dni[0] < 10000000:
            print("Number should be in range [10000000, 100000000)")
        else:
            print(dni(args.dni[0]))
    if args.dni_rand:
        print(random_dni())
    if args.nie:
        if 2 < args.nie[0] or args.nie[0] < 0:
            print("First number should be: 0:X, '1:Y, 2:Z")
        elif 10000000 <= args.nie[1] or args.nie[1] < 1000000:
            print("Second number should be in range [1000000, 10000000)")
        else:
            print(nie(args.nie[0], args.nie[1]))
    if args.nie_rand:
        print(random_nie())

if __name__ == '__main__':
    main()

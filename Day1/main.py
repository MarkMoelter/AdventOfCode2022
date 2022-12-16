from Day1 import elf_with_most_calories, top_elves


def main():
    # part 1
    print(elf_with_most_calories()[1])
    # or
    print(*top_elves(1))

    # part 2
    print(sum(top_elves(3)))


if __name__ == '__main__':
    main()

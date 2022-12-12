import utils

from Day3.part1 import Part1


class Part2(Part1):
    def __init__(self, rucksack_list: list[str] = None):
        super().__init__(rucksack_list)
        self.rucksack_list = rucksack_list

    def split_into_groups(
            self,
            number_in_each_group: int = 3
    ) -> dict[int: list[tuple[str, str]]]:
        """
        Split the list into groups of the parameter's size.

        :param number_in_each_group: The number of groups to split the list into.
        Default value is 3 groups.
        :return: A dictionary containing the groups of rucksacks.
        """
        groups = {}
        group_id = 0
        for i in range(0, len(self.split_rucksack()), number_in_each_group):
            groups[group_id] = self.split_rucksack()[i:i+number_in_each_group]
            group_id += 1

        return groups


def main():
    rucksacks = utils.read_input_file()
    print(Part2(rucksacks).split_into_groups())


if __name__ == '__main__':
    main()

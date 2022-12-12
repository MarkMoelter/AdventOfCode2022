import utils


class Part1:
    def __init__(self, rucksack_list: list[str] = None):
        self.rucksack_list = rucksack_list

    def split_rucksack(self) -> list[tuple[str, str]]:
        """
        Split the list of rucksacks into pockets.

        :return: List of rucksacks split into separate pockets.
        """
        rucksack_pockets = []

        for rucksack in self.rucksack_list:
            # calculate the length of each rucksack
            pocket_len = len(rucksack) // 2

            # use string splicing to split the rucksack
            pocket_1 = rucksack[:pocket_len]
            pocket_2 = rucksack[pocket_len:]

            # append to the list
            rucksack_pockets.append((pocket_1, pocket_2))

        return rucksack_pockets

    @staticmethod
    def check_pockets(pocket_1, pocket_2) -> set[str]:
        """
        Check pockets for duplicate items.
        Should return one item for this problem.

        :return: Duplicate item in both pockets.
        """

        # make sure pockets are the same length
        if len(pocket_1) != len(pocket_2):
            raise ValueError('Pockets must have the same length.')

        duplicates = set()

        for char in pocket_1:
            if char in pocket_2:
                duplicates.add(char)

        return duplicates

    @staticmethod
    def priority_map() -> dict:
        """
        Create a dictionary to map alphabetical characters to a priority value.

        :return: A dictionary that maps a-z: 1-26 and A-Z: 27-52
        """
        priority = {}

        # lowercase characters
        unicode_a = 97
        unicode_z = 122
        lowercase_start_value = 1
        for i in range(unicode_a, unicode_z + 1):
            priority[chr(i)] = lowercase_start_value
            lowercase_start_value += 1

        # uppercase characters
        unicode_A = 65
        unicode_Z = 90
        uppercase_start_value = 27
        for i in range(unicode_A, unicode_Z + 1):
            priority[chr(i)] = uppercase_start_value
            uppercase_start_value += 1

        return priority

    def assign_priority(self, character: str) -> int:
        """
        Check the priority (score) of a given character.

        :return: Integer value of the priority.
        """

        # parameter not length 1
        if len(character) != 1:
            raise TypeError(
                f'assign_priority() expected a character, '
                f'but string of length {len(character)} was found.')

        # parameter not in dictionary
        if self.priority_map().get(character) is None:
            raise TypeError(
                f'assign_priority() expected an alphabetical character, '
                f'but character "{character}" was found.')

        return self.priority_map().get(character)

    def total_priority(self) -> int:
        """
        Calculate the total priority value of all rucksacks in the input file.

        :return: The total priority value as an integer.
        """
        score = 0

        for pocket_1, pocket_2 in self.split_rucksack():
            # collect the duplicate from each rucksack
            duplicate = self.check_pockets(pocket_1, pocket_2)

            # get the value of the duplicate and add it to the score
            for dup in duplicate:
                score += self.assign_priority(dup)

        return score

def main():
    part_obj = Part1(utils.read_input_file())
    print(part_obj.total_priority())

if __name__ == '__main__':
    main()

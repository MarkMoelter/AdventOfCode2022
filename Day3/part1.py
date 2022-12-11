class Part1:
    def __init__(self, rucksack_list:list[str] = None):
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
            pocket1 = rucksack[:pocket_len]
            pocket2 = rucksack[pocket_len:]

            # append to the list
            rucksack_pockets.append((pocket1, pocket2))

        return rucksack_pockets

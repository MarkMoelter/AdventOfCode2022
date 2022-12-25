class Visibility:
    def __init__(self, forest: list[str]):
        self.forest = forest

    def is_visible(self, tree: str) -> bool:
        """Check if a tree is visible from the outside of the forest."""

    def horizontal(self):
        """Check for visibility horizontally in the forest."""

    def vertical(self):
        """Check for visibility vertically in the forest."""

    def count_visible_trees(self) -> int:
        """Count the number of trees visible from the outside of the forest."""
        total = 0
        # iterate though all trees in the forest
        for idx, tree_row in enumerate(self.forest):
            for j_idx, tree in enumerate(tree_row):

                # return true if the index is 0 or the last index in the list.
                find_edges = lambda index, list_: index == 0 or index == (len(list_) - 1)

                # check for perimeter trees
                top_and_bottom = find_edges(idx, self.forest)
                left_and_right = find_edges(j_idx, tree_row)
                if top_and_bottom or left_and_right:
                    total += 1
                # check for visibility
                if self.is_visible(tree):
                    total += 1
        return total

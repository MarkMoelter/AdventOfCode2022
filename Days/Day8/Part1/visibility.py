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
        for tree_row in self.forest:
            for tree in tree_row:
                # check for visibility
                if self.is_visible(tree):
                    total += 1
        return total

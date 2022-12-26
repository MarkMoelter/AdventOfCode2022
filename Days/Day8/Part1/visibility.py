class Visibility:
    def __init__(self, forest: list[str]):
        self.forest = forest

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
                perimeter = top_and_bottom or left_and_right

                # check for row and column visibility
                find_rows_or_col = lambda index, list_: False  # fixme: not functional
                row_visibility = find_rows_or_col(idx, self.forest)
                col_visibility = find_rows_or_col(j_idx, tree_row)
                row_and_column = row_visibility or col_visibility

                is_visible = perimeter or row_and_column
                if is_visible:
                    total += 1

        return total

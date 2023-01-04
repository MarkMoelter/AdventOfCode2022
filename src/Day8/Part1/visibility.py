class Visibility:
    def __init__(self, forest: list[str]):
        self.forest = forest

    def count_visible_trees(self) -> int:
        """Count the number of trees visible from the outside of the forest."""
        total = 0
        # iterate though all trees in the forest
        for idx, tree_row in enumerate(self.forest):
            for j_idx, tree in enumerate(tree_row):

                def is_vert_edge() -> bool:
                    return j_idx == 0

                def is_hori_edge() -> bool:
                    return idx == (len(self.forest) - 1)


                def is_edge(index, list_):
                    return index == 0 or index == (len(list_) - 1)

                def is_visible_in_row(index, list_):
                    return False

                def is_visible_in_col(index, list_):
                    return False

                # remove below this ##################
                # check for perimeter trees
                top_and_bottom = is_edge(idx, self.forest)
                left_and_right = is_edge(j_idx, tree_row)
                perimeter = top_and_bottom or left_and_right

                # check for row and column visibility
                find_rows_or_col = lambda index, list_: False
                row_visibility = find_rows_or_col(idx, self.forest)
                col_visibility = find_rows_or_col(j_idx, tree_row)
                row_and_column = row_visibility or col_visibility

                is_visible = perimeter or row_and_column


                # remove above ##########
                if is_visible:
                    total += 1

        return total

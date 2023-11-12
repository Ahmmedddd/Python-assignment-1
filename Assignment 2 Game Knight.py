import unittest

class Board:
    def __init__(self):
        self.knights = {
            "RED": [[0, 0], "LIVE", None, 1, 1],
            "BLUE": [[7, 0], "LIVE", None, 1, 1],
            "GREEN": [[7, 7], "LIVE", None, 1, 1],
            "YELLOW": [[0, 7], "LIVE", None, 1, 1]
        }
        self.items = {
            "MAGIC_STAFF": [[5, 2], False],
            "HELMET": [[5, 5], False],
            "DAGGER": [[2, 5], False],
            "AXE": [[2, 2], False]
        }

    def move_knight(self, knight_color, direction):
        """Moves a knight in the specified direction.

        Args:
            knight_color: The color of the knight to move.
            direction: The direction to move the knight.

        Returns:
            None.
        """

        # Validate the knight color.
        if knight_color not in self.knights:
            raise ValueError("Invalid knight color: {}".format(knight_color))

        # Validate the direction.
        if direction not in ["N", "E", "S", "W"]:
            raise ValueError("Invalid direction: {}".format(direction))

        # Get the knight.
        knight = self.knights[knight_color]

        # Get the knight's current row and column.
        row, col = knight[0]

        # Calculate the new row and column.
        new_row = row - 1 if direction == "N" else row + 1 if direction == "S" else row
        new_col = col + 1 if direction == "E" else col - 1 if direction == "W" else col

        # Check if the new row and column are within the bounds of the board.
        if new_row < 0 or new_row > 7 or new_col < 0 or new_col > 7:
            knight[1] = "DROWNED"
            return

        # Get the item at the new row and column.
        item_row, item_col = self.items["MAGIC_STAFF"]
        if item_row == new_row and item_col == new_col:
            self.items["MAGIC_STAFF"][1] = True
            knight[3] += 1
            knight[4] += 1

        item_row, item_col = self.items["HELMET"]
        if item_row == new_row and item_col == new_col:
            self.items["HELMET"][1] = True
            knight[4] += 1

        item_row, item_col = self.items["DAGGER"]
        if item_row == new_row and item_col == new_col:
            self.items["DAGGER"][1] = True
            knight[3] += 1

        item_row, item_col = self.items["AXE"]
        if item_row == new_row and item_col == new_col:
            self.items["AXE"][1] = True
            knight[3] += 2

        # Update
        knight[0] = [new_row, new_col]

    def attack_knights(self):
        """Attacks all knights on the board.

        Returns:
            None.
        """

        for knight_color in ["RED", "BLUE", "GREEN", "YELLOW"]:
            knight = self.knights[knight_color]

            # Skip drowned or dead knights.
            if knight[1] == "DROWNED" or knight[1] == "DEAD":
                continue

            # Find the other knight.
            other_knight = None
            for other_knight_color in ["RED", "BLUE", "GREEN", "YELLOW"]:
                if other_knight_color != knight_color:
                    other_knight = self.knights[other_knight_color]
                    break

            # Skip if there is no other knight.
            if other_knight is None or other_knight[1] == "DROWNED" or other_knight[1] == "DEAD":
                continue

            # Calculate the attacker's attack power.
            attacker_attack = knight [3]

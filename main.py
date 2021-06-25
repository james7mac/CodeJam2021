# This is a sample Python script.
from typing import List, Any, Optional
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import platform
print(platform.python_version())

def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:
    table = []
    """
    :param rows: 2D list containing objects that have a single-line representation (via `str`).
    All rows must be of the same length.
    :param labels: List containing the column labels. If present, the length must equal to that of each row.
    :param centered: If the items should be aligned to the center, else they are left aligned.
    :return: A table representing the rows passed in.
    """
    return table



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    table = make_table(
        rows=[
            ["Lemon"],
            ["Sebastiaan"],
            ["KutieKatj9"],
            ["Jake"],
            ["Not Joe"]
        ]
    )
    print(table)

    table = make_table(
        rows=[
            ["Lemon", 18_3285, "Owner"],
            ["Sebastiaan", 18_3285.1, "Owner"],
            ["KutieKatj", 15_000, "Admin"],
            ["Jake", "MoreThanU", "Helper"],
            ["Joe", -12, "Idk Tbh"]
        ],
        labels=["User", "Messages", "Role"]
    )
    print(table)
    table = make_table(
        rows=[
            ["Ducky Yellow", 3],
            ["Ducky Dave", 12],
            ["Ducky Tube", 7],
            ["Ducky Lemon", 1]
        ],
        labels=["Name", "Duckiness"],
        centered=True
    )
    print(table)




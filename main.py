# This is a sample Python script.
from typing import List, Any, Optional
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import platform
tt =  {'ul':'┌','um':'┬','ur': '┐', 'ml': '├', 'mm': '┼', 'mr':'┤', 'll':'└', 'lm':'┴', 'lr':'┘', 'b':'│', 'd' :'─'}

def get_shape(rows):
    #find the size of each column
    cols = zip(*rows)
    shape = []
    for col in cols:
        shape.append(max([len(str(item)) for item in col])+1)
    return shape


def fix_row(row, shape, centered=False):
    #add padding to correctly justify each entry in row
    for i, item in enumerate(row):
        item = ' ' + str(item)
        if centered:
            item = item.center(shape[i]+1) + tt['b']
        else:
            item = item.ljust(shape[i]) + ' ' + tt['b']
        row[i] = item
    row[0] = tt['b'] + row [0]
    return row

def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:

    # find size of biggest entry in each column
    shape = get_shape(rows + [labels]) if labels else get_shape(rows)

    #build top of the table
    if labels:
        top = [tt['ul']]
        head = [tt['ml']]
        for i, label in enumerate(labels):
            top.append(tt['d']*(shape[i]+1))
            top.append(tt['um'])
            head.append(tt['d']*(shape[i]+1))
            head.append(tt['mm'])

        top[-1] = tt['ur']
        head[-1] = tt['mr']
        header = ''.join(top) + '\n'
        labs = fix_row(labels, shape)
        header = header + ''.join(labs) + '\n'
        header = header + ''.join(head) + '\n'
    else:
        header = tt['ul'] + tt['d'] * (sum(shape) + (len(shape) * 2) - 1) + tt['ur'] + '\n'

    # create and bottom top of table
    bottom = [tt['ll']]
    for i in shape:
        bottom.append(tt['d']*(i+1))
        bottom.append(tt['lm'])
    bottom[-1] = tt['lr']
    foot = ''.join(bottom)

    # middle of table
    for i, row in enumerate(rows):
        rows[i] = fix_row(row, shape, centered=centered)
    for i, row in enumerate(rows):
        rows[i] = ''.join(row)

    # join 3 sectioins together
    table = header + '\n'.join(rows) + '\n' + foot







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




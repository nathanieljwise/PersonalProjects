import random


def create_block(colors, fabrics):
    """
    Creates a block with a specified number of colors, chosen from the fabric stash.
    :param colors: Integer from user input. Corresponds to a fabric color.
    :param fabrics: Integer from user input. Total number of fabric colors.
    :return: A list of integers (corresponding to fabric colors.)
    """
    this_block = []
    while len(this_block) < colors:
        this_color = random.randint(1, fabrics)
        if this_color not in this_block:  # Don't duplicate colors in block
            this_block.append(this_color)
    return this_block


def check_block(quilt, this_block):
    """
    Verifies that no more than two colors match between any two blocks.
    :param quilt: 2D list of blocks made of colors.
    :param this_block: A newly created block, to be checked against existing (already verified) blocks.
    :return: False if 3 colors match; otherwise True.
    """
    for existing_block in quilt:
        matching_colors = 0
        for existing_color in existing_block:
            for new_color in this_block:
                if new_color == existing_color:
                    matching_colors += 1
                    if matching_colors > 2:
                        return False
    return True


if __name__ == '__main__':

    the_quilt = []

    number_of_fabrics = int(input("How many fabrics do you have? "))
    number_of_blocks = int(input("How many blocks do you need? "))
    number_of_colors = int(input("How many colors per block? "))

    for i in range(number_of_blocks):
        current_block = create_block(number_of_colors, number_of_fabrics)
        if check_block(the_quilt, current_block):
            the_quilt.append(current_block)

    for i in range(len(the_quilt)):
        print("Block %d: %s" % (i + 1, the_quilt[i]))

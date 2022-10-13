print(">> I'm here. At the start.")

def split(name):
    """Take a name string and split in first and last name."""
    print(">> I'm in the split function now.")
    # Do the split
    splitted = name.split(" ")
    # Output the result
    return {
        'first': splitted[0],
        'last': splitted[1]
    }


def capitalize(names):
    """Take first and last name and capitalize them."""
    print(">> I'm in capitalize")
    # Capitalize the two names
    # print(names)
    # Output the result
    return [names[0].capitalize(), names[1].capitalize()]


if __name__ == "__main__":
    print('>> I\'m in the "if __name__" thing')
    artist = "john lennon"
    first_last = split(artist)
    print(first_last)
    # print(capitalize(first_last))

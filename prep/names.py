print(">> I'm here. At the start.")

def split(name):
    """Take a name string and split in first and last name."""
    print(">> I'm in the split function now.")
    # Do the split
    first_last = name.split(" ")
    # Output the result
    print(first_last)


def capitalize(names):
    """Take first and last name and capitalize them."""
    print(">> I'm in capitalize")
    # Capitalize the two names
    # TO DO
    # Output the result
    print(first_cap, last_cap)


if __name__ == "__main__":
    print('>> I\'m in the "if __name__" thing')
    artist = "John Lennon"
    split(artist)
    # capitalize(artist)

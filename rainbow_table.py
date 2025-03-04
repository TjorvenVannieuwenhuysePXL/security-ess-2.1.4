def load_rainbow_table(filepath):
    rainbow_table = {}

    # Load rainbow table file. "with" will automatically
    # close the file once the block is exited.
    with open(filepath, "r") as f:
        for line in f:
            line_data = line.strip().split(maxsplit=1)
            if len(line_data) < 2:
                continue

            _hash, password = line_data
            rainbow_table[_hash] = password

    return rainbow_table
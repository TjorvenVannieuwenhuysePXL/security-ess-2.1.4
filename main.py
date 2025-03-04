from rainbow_table import load_rainbow_table

def main():
    rainbow_table = load_rainbow_table("md5woordenlijst.txt")

    with open("hashes.txt", "r") as f:
        hashes = f.read().splitlines()

    for _hash in hashes:
        print(f"{_hash}: {rainbow_table.get(_hash, 'Not found')}")

if __name__ == '__main__':
    main()
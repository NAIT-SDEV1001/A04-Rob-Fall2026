def read_journal(file_path):
    """Read the journal entries from a file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        # option 1: read all of the file at once
        entries = file.readlines()
    return entries

# ... read_journal function ...

def main():
    file_path = 'journal.txt'
    entries = read_journal(file_path)
    print(F"Journal Entries of {file_path}:\n")
    for index, entry in enumerate(entries):
        print(entry)

if __name__ == "__main__":
    main()


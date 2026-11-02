def write_to_file(filename, lines):
    """Creates or overwrites a file and writes each line from the list to it."""
    with open(filename, 'w') as f:
        # Basic approach: using a standard for loop with an index or simple iteration
        for line in lines:
            f.write(line + "\n")
            
        # Pythonic alternative using "line comprehension":
        # f.writelines([line + "\n" for line in lines])
        
    print(f"Successfully wrote {len(lines)} lines to {filename}.")

def append_to_file(filename, lines):
    """Appends each line from the list to the end of an existing file."""
    with open(filename, 'a') as f:
        # Basic approach: loop through each line and write with a newline
        for line in lines:
            f.write(line + "\n")
            
        # Pythonic alternative using "line comprehension":
        # f.writelines([line + "\n" for line in lines])
        
    print(f"Successfully appended {len(lines)} lines to {filename}.")
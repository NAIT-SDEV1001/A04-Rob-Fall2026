from file_writer import write_to_file, append_to_file

def main():
    filename = input("Enter filename: ")
    mode = input("Do you want to write or append? ").strip().lower()
    num_lines = int(input("How many lines? "))
    
    lines = [] 
    # Basic approach: standard counting loop
    for i in range(num_lines):
        line = input(f"Enter line {i + 1}: ")
        lines.append(line)
        
    # Pythonic alternative (replace lines 10-12 with single line below):
    # lines = [input(f"Enter line {i + 1}: ") for i in range(num_lines)]

    if mode == 'write':
        write_to_file(filename, lines)
    elif mode == 'append':
        append_to_file(filename, lines)
    else:
        print("Invalid choice! Please choose either 'write' or 'append'.")

if __name__ == "__main__":
    main()
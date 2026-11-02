from file_reader import read_file

def main():
    filename = input("Enter filename: ")
    
    # 1. Call the function to get the list of lines
    lines = read_file(filename)
    
    # 2. Process the list
    non_empty_count = 0

    for line in lines:
        cleaned_line = line.strip()
        
        # Check if the line is not empty
        if cleaned_line != "":  #vs if cleaned_line (shortcut relying on python truthiness)
            non_empty_count += 1
            print(f"Line {non_empty_count}: {cleaned_line}")
            
    # 3. Print the final total count
    print(f"Total non-empty lines: {non_empty_count}")

if __name__ == "__main__":
    main()
from file_writer import write_to_file, append_to_file

def main():
    while True:
        mode = input("Do you want to write, append, or quit? ").strip().lower()
        
        if mode == 'quit':
            print("Exiting program.")
            break
            
        if mode not in ['write', 'append']:
            print("Invalid choice! Please choose either 'write', 'append', or 'quit'.")
            continue

        filename = input("Enter filename: ")

        try:
            num_lines = int(input("How many lines? "))
            
            if num_lines <= 0:
                print("Please enter a number greater than 0.")
                continue
                
        except ValueError:
            print("Error: Invalid input. Please enter a valid whole number for the line count.")
            continue  

        lines = []
        
        # Basic approach: standard counting loop
        for i in range(num_lines):
            line = input(f"Enter line {i + 1}: ")
            lines.append(line)
            
        # Pythonic alternative (commented out list comprehension with input):
        # lines = [input(f"Enter line {i + 1}: ") for i in range(num_lines)]

        # Use try-except to handle potential file system errors (e.g., permission issues, invalid paths)
        try:
            if mode == 'write':
                write_to_file(filename, lines)
            elif mode == 'append':
                append_to_file(filename, lines)
        except Exception as e:
            print(f"An error occurred while saving to the file: {e}")

if __name__ == "__main__":
    main()
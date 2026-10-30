# Reading and Writing to Files

## Why is this important?

Files are a fundamental part of programming. They allow us to store data persistently, which means that the data will still be there even after the program has stopped running. This is important for many applications, such as web applications, games, and data analysis.

It doesn't matter if it's a text file, a csv file, or a json file, being able to read and write files is a fundamental skill that every programmer should have.

## What are we going to do?

We're going to create a journal application that will allow us to read and write entries to a file.

## Steps

### 1. Let's open our `journal.txt` file and read the contents.

First we need to know the path of the file we want to read.

In this case, we want to read the `journal.txt` file which is in the same directory as our script.

With files you need to use `open()` to open the file, and then you can read it using `read()`, `readline()`, or `readlines()`.

Let's create a `read_journal` function that will read the contents of the file and return the lines as a list.
```python
def read_journal(file_path):
    """Read the journal entries from a file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        # option 1: read all of the file at once
        entries = file.readlines()
    return entries
```
Let's break down the code:
- We define a function `read_journal` that takes a file path as an argument.
- We use the `with` statement to open the file in read mode (`'r'`). This ensures that the file is properly closed after we're done with it. The options for opening a file are:
  - `'r'`: read mode (default)
  - `'w'`: write mode (overwrites the file)
  - `'a'`: append mode (adds to the end of the file)
  - `'b'`: binary mode (for binary files)
- We pass `encoding='utf-8'` to ensure the file is read using the UTF-8 character encoding. UTF-8 is a standard encoding that supports virtually all characters from all languages. Without specifying it, Python uses your system's default — which varies by OS and can cause issues when sharing files across different computers.
- We use `file.readlines()` to read all the lines in the file and store them in the `entries` variable. This returns a list of lines.
  - The other options are:
    - `file.read()`: reads the entire file as a single string.
    - `file.readline()`: reads a single line from the file.
- Finally, we return the `entries` list.

Note: the `with` statement is a context manager that automatically closes the file when we're done with it, even if an error occurs.

### 2. Let's create the `main` function and module guard to read the journal entries and print them.

Let's use this read function to read the `journal.txt` file and print the entries.

```python
# ... read_journal function ...

def main():
    file_path = 'journal.txt'
    entries = read_journal(file_path)
    print(F"Journal Entries of {file_path}:\n")
    for index, entry in enumerate(entries):
        print(entry)

if __name__ == "__main__":
    main()

```

Now if you execute the script `python journal_app.py`, this will be the output.

```
Journal Entries of journal.txt:

I've been learning python and it's pretty fun so far!

I'm really excited to learn how to use pip and virtualenv, and learn more about the python ecosystem.
```

### 3. Let's see what happens when we try to read a file that doesn't exist.

Change the `file_path` to a file that doesn't exist, for example `non_existent_file.txt`.

Now run the script again `python journal_app.py` and you will see this error.
```
$ python journal_app.py
Traceback (most recent call last):
  File "C:\Users\dmouris\course_development\sdev1001_programming_fundamentals\sdev1001-master-course\files_reading_and_writing\read_and_write_fundamentals_end\journal_app.py", line 19, in <module>
    main()
  File "C:\path\to\journal_app.py", line 12, in main
    entries = read_journal(file_path)
              ^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\path\to\journal_app.py", line 5, in read_journal
    with open(file_path, 'r') as file:
         ^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'non_existent_file.txt'
```
When you try to read a file that doesn't exist, Python raises a `FileNotFoundError`. This is an exception that indicates that the file could not be found.

External files are something that can change, and aren't guaranteed to be there, so let's use a `try` and `except` block to handle this error gracefully.

### 4. Let's handle the `FileNotFoundError` exception.

Now we will modify the `read_journal` function to handle the `FileNotFoundError` exception. This way, if the file does not exist, we can return a friendly error message instead of crashing the program.

```python
def read_journal(file_path):
    """Read the journal entries from a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            # option 1: read all of the file at once
            entries = file.readlines()
        return [entry.strip() for entry in entries if entry.strip()]
    except FileNotFoundError:
        return ["Error: The file does not exist. Please check the file path."]

# ... main function ...
```

Let's run the script again with the `file_path` set to `non_existent_file.txt`.

```
$ python journal_app.py
Journal Entries of non_existent_file.txt:

Error: The file does not exist. Please check the file path.
```

Now, instead of crashing the program, we get a friendly error message that tells us the file does not exist.

### 5. Let's write to the journal file.

Now that we can read from the journal file, let's add a function to write entries to the journal file.

```python
def write_journal(file_path, entry):
    """Write a journal entry to a file."""
    with open(file_path, 'a', encoding='utf-8') as file:  # 'a' mode to append
        file.write(F"{entry}\n")
```
Let's break down the code:
- We define a function `write_journal` that takes a file path and an entry as arguments.
- We use the `with` statement to open the file in append mode (`'a'`). This means that if the file does not exist, it will be created, and if it does exist, the new entry will be added to the end of the file.
- We use `file.write()` to write the entry to the file, followed by a newline character (`\n`) to ensure that each entry is on a new line.

### 6. Let's modify our `main` function to prompt the user if they want to add a new entry or read the journal entries.

First change the `file_path` back to `journal.txt`.

```python
# ... read_journal and write_journal functions ...

def main():
    file_path = 'journal.txt'
    while True:
        action = input("Do you want to (r)ead the journal or (w)rite a new entry? (q to quit): ").strip().lower()
        if action == 'r':
            entries = read_journal(file_path)
            print(F"Journal Entries of {file_path}:\n")
            for index, entry in enumerate(entries):
                print(entry)
        elif action == 'w':
            new_entry = input("Enter your journal entry: ")
            write_journal(file_path, new_entry)
            print("Entry added to the journal.")
        elif action == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
```
You can see that we added a loop that will keep asking the user if they want to read or write to the journal until they choose to quit.

Here's a sample run of the program:
```
$ python journal_app.py
Do you want to (r)ead the journal or (w)rite a new entry? (q to quit): w
Enter your journal entry:  Here's my first entry from the journal app.
Entry added to the journal.
Do you want to (r)ead the journal or (w)rite a new entry? (q to quit): w
Enter your journal entry: Wow I can see the files being changed if I open it in vscode!
Entry added to the journal.
Do you want to (r)ead the journal or (w)rite a new entry? (q to quit): r
Journal Entries of journal.txt:

I've been learning python and it's pretty fun so far!
I'm really excited to learn how to use pip and virtualenv, and learn more about the python ecosystem.
Here's my first entry from the journal app.
Wow I can see the files being changed if I open it in vscode!
Do you want to (r)ead the journal or (w)rite a new entry? (q to quit): q
Goodbye!
```

Now if you open the `journal.txt` file in a text editor, you will see the new entries added to the file.

### 7. Let's make our file path more robust with `pathlib`.

Up to now we've used `file_path = 'journal.txt'` and run the script with `python journal_app.py` from inside the lesson folder. This works, but it's fragile. To see why, we first need to understand the **current working directory**.

#### What is the current working directory?

When you run a Python script, the program has a notion of the **current working directory** (often abbreviated **CWD**) — basically, "where you are" in the file system when you ran the command. By default, any relative path like `'journal.txt'` is resolved relative to the CWD, **not** relative to where the script file is located.

You can ask Python for the current working directory like this:

```python
from pathlib import Path
print(Path.cwd())
```

If you run `python journal_app.py` from inside `read_and_write_fundamentals_end/`, the CWD is that folder — and Python finds `journal.txt` right next to the script. But if you run the same script from a different folder:

```
$ cd ..
$ python read_and_write_fundamentals_end/journal_app.py
```

...the CWD is now the parent folder, Python looks for `journal.txt` there, doesn't find it, and our `FileNotFoundError` handler kicks in.

#### Building a path relative to the script

What we really want is a path that's relative to the **script file itself**, not the current working directory. Python's built-in `pathlib` module makes this easy.

```python
from pathlib import Path

script_dir = Path(__file__).parent
file_path = script_dir / 'journal.txt'
```

Let's break this down:
- `__file__` is a special variable Python sets to the path of the currently-running script file.
- `Path(__file__)` wraps it in a `Path` object so we can use path operations on it.
- `.parent` gives us the directory containing the script.
- The `/` operator joins paths — `pathlib` overloads it to act like a path separator. `script_dir / 'journal.txt'` builds the full path to the journal file regardless of whether you're on Windows (`\`) or macOS/Linux (`/`).

Update `main()` to use this:

```python
from pathlib import Path

# ... other imports and functions ...

def main():
    file_path = Path(__file__).parent / 'journal.txt'
    while True:
        action = input("Do you want to (r)ead the journal or (w)rite a new entry? (q to quit): ").strip().lower()
        # ... rest unchanged
```

Notice that `read_journal` and `write_journal` don't need any changes — `open()` accepts both strings and `Path` objects.

One small tweak: now that `file_path` is a full path, printing it directly would show the whole thing (e.g., `C:\...\read_and_write_fundamentals_end\journal.txt`). Use `file_path.name` instead to keep the header showing just the filename:

```python
print(F"Journal Entries of {file_path.name}:\n")
```

Now you can run the script from any directory and it will still find the journal file next to itself.

#### A few other things `pathlib` gives you

Once you have a `Path` object, you get a lot of useful methods for free:
- `path.exists()` — check whether the file or folder actually exists
- `path.is_file()` / `path.is_dir()` — check whether the path points to a file or a directory
- `path.suffix` — get the file extension (e.g., `.txt`)
- `path.name` — get just the filename without the rest of the path

For modern Python code, `pathlib` is the recommended way to work with file paths — you no longer need to worry about whether to use `/` or `\\` as a separator, and your code reads more clearly.

## Best Practices

- **Always close your files.** Using the `with` statement (as we did throughout this lesson) handles this automatically — the file closes as soon as the block exits, even if an error occurs.
- **Handle exceptions for missing or inaccessible files.** Files can disappear, be moved, or be locked by another process. Using `try`/`except FileNotFoundError` (as in our `read_journal` function) prevents your program from crashing unexpectedly.
- **Use clear file paths and verify they exist when needed.** Relative paths like `'journal.txt'` work fine when your script and file are in the same directory, but can cause confusion otherwise. If your program depends on a file being present, consider checking or communicating the path clearly to the user.
- **Use `pathlib` for path handling.** Building file paths with `Path(__file__).parent / 'filename'` makes your script work no matter where it's run from, and the `Path` object's methods (`.exists()`, `.is_file()`, etc.) are far cleaner than manipulating strings.

## Conclusion

In this lesson, we learned how to read and write files in Python. We created a simple journal application that allows us to read and write entries to a file. We also learned how to handle exceptions when reading files that do not exist.

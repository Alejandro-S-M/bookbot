from pathlib import Path

# This gets the directory where your script (the .py file) lives
current_dir = Path(__file__).parent

# Now build the path to 'frankenstein.txt' inside the 'books' folder
book_path = current_dir / 'books' / 'frankenstein.txt'

print(book_path)
# This will print the absolute path to 'frankenstein.txt'
# Desktop File Organizer

## Description
An automation script that cleans up a messy desktop by scanning files and moving them into specific folders based on their file extensions (e.g., images, pdfs, text files). Files with unknown extensions are moved to an "others" folder.

## Features
- Uses dictionaries to map file extensions to folder names.
- Automatically creates destination folders if they do not exist.
- Safely moves files using `pathlib.Path.replace()`.

## Technologies Used
- Python 3
- `pathlib` module

## How to Run
1. Run the script:
   `python3 organize.py`
2. The script will automatically scan your Desktop and organize the files.

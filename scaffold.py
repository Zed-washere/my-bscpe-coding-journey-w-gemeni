#The "Safety Check": Before creating anything, check if the folder already exists.
#If it does, print a warning message: "Warning: Directory already exists. Skipping creation." and stop the script using sys.exit().
#The Nested README: Ensure the README.md is created inside the new project folder, not outside of it. (Hint: Use base_dir / "README.md")

import sys
from pathlib import Path
from datetime import date

# 1. Get the name from the user via terminal
# If the user didn't provide a name, use a default
project_name = sys.argv[1] if len(sys.argv) > 1 else "New-Project"

# 2. Convert string to a Path object
base_dir = Path(project_name)

# 3. Create the main folder
base_dir.mkdir(exist_ok=True)

# 4. Loop to create subdirectories
subfolders = ["src", "docs", "tests"]
for folder in subfolders:
    target = base_dir / folder  # This works now because base_dir is a Path!
    target.mkdir(exist_ok=True) # Creates a folder, not a file
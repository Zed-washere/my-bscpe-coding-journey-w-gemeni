
import sys
from pathlib import Path
from datetime import date

current_date = date.today()

# 1. Get the name from the user via terminal
# If the user didn't provide a name, use a default
project_name = sys.argv[1] if len(sys.argv) > 1 else "New-Project"

print(f"the name you chose is {project_name}")

# 2. Convert string to a Path object
folder_name = Path(project_name)

# 3. Create the main folder
if folder_name.exists():
    print("Stopped creating folder, folder already exists")
    sys.exit()
else:
    folder_name.mkdir(exist_ok=True)

# 4. Loop to create subdirectories
subfolders = ["src", "docs", "tests"]
for folder in subfolders:
    target = folder_name / folder  # This works now because base_dir is a Path!
    target.mkdir(exist_ok=True) # Creates a folder, not a file


with open(folder_name/"README.md","w") as readme:
    readme.write(f"# {project_name}\n initiated on {current_date}")



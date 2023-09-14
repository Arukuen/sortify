from pathlib import Path
import shutil
from datetime import datetime

# CONSTANTS
SUBFOLDERS = ['math', 'bio', 'sci']
START_WEEK = datetime(2023, 9, 11)

source = Path('source')
destination = Path('destination')

destination_folders = {}

# Create subfolders inside the destination
for subfolder in SUBFOLDERS:
    destination.joinpath(subfolder.lower()).mkdir(parents=True, exist_ok=True)

# Move files from SOURCE to DESTINATION in appropriate subfolders
for file in source.iterdir():
    for sub in SUBFOLDERS:
        if sub in file.name: 
            shutil.move(file, destination.joinpath(sub).joinpath(file.name))

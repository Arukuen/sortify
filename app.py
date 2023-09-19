from pathlib import Path
import shutil
from datetime import datetime

# CONSTANTS
SUBFOLDERS = [
    'CS 198',
    'CS 196',
    'CS 133',
    'Engg 150',
    'Persyan 10',
    'Eng 30',
    'MBB 1',
]
START_WEEK = datetime(2023, 9, 11)

source = Path(r'C:\Users\adsar\Downloads\source')
destination = Path(r'C:\Users\adsar\Documents\UP Files\Year 4 First Sem - BSCS')

def get_current_week():
    return (datetime.now() - START_WEEK).days // 7 + 1

# Create subfolders inside the destination
def create_subfolders():
    for subfolder in SUBFOLDERS:
        current_week = get_current_week()
        for week in range(1, current_week + 1):
            path = destination.joinpath(subfolder).joinpath(f'Week {week}')
            path.mkdir(parents=True, exist_ok=True)
        

# Move files from SOURCE to DESTINATION in appropriate subfolders
def move_files():
    current_week = get_current_week()
    for file in source.iterdir():
        for sub in SUBFOLDERS:
            if sub in file.name: 
                shutil.move(file, destination.joinpath(sub).joinpath(f'Week {current_week}').joinpath(file.name))

create_subfolders()
move_files()
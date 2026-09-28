import os
import shutil
from datetime import datetime

# Source folder
source_folder = "StudentProjects"

# Check whether the source folder exists
if not os.path.exists(source_folder):
    print("Error: StudentProjects folder does not exist.")
else:
    # Create backup folder with the current date
    current_date = datetime.now().strftime("%Y-%m-%d")
    backup_folder = "Backup_" + current_date

    os.makedirs(backup_folder, exist_ok=True)

    # Copy files from source folder to backup folder
    file_count = 0

    for file_name in os.listdir(source_folder):
        source_path = os.path.join(source_folder, file_name)
        backup_path = os.path.join(backup_folder, file_name)

        if os.path.isfile(source_path):
            shutil.copy2(source_path, backup_path)
            file_count += 1

    # Display number of files backed up
    print("Backup completed successfully.")
    print("Number of files backed up:", file_count)

import os
from datetime import datetime

# Database connection information
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "Secret5555"
DB_NAME = "test_db"
BACKUP_DIR = "./backups"

# Check and create backup folder if it doesn't exist
os.makedirs(BACKUP_DIR, exist_ok=True)

# Create a unique filename using current date and time
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
backup_filename = f"{DB_NAME}_backup_{timestamp}.sql"
backup_path = os.path.join(BACKUP_DIR, backup_filename)

# Command to run mysqldump with TCP connection
command = f"mysqldump --protocol=TCP -h {DB_HOST} -u {DB_USER} -p{DB_PASSWORD} {DB_NAME} > {backup_path}"

# Run the backup command
exit_code = os.system(command)

# Check if backup was successful
if exit_code == 0:
    print(f"Backup successful! File saved at: {backup_path}")
else:
    print("Backup failed. Please check your connection or credentials.")

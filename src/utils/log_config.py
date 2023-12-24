import os
import logging

LOG_DIR = "logs"
LOG_FILE = f"{LOG_DIR}/prime_calculations.log"

def setup_logging():
    """
    Set up logging configuration.
    """
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    console = logging.StreamHandler()
    console.setLevel(logging.WARNING)
    logging.getLogger("").addHandler(console)

def logrotate(max_size=5, backup_count=3):
    """
    Rotate the log file if it exceeds the specified size.

    Args:
        max_size (int, optional): Maximum size of the log file in MB. Defaults to 5MB.
        backup_count (int, optional): Number of backup files to keep. Defaults to 3.
    """
    if not os.path.exists(LOG_FILE):
        return

    file_size = os.path.getsize(LOG_FILE) / (1024 * 1024)  # Convert size to MB

    if file_size < max_size:
        return

    for i in range(backup_count - 1, 0, -1):
        src = f"{LOG_FILE}.{i}"
        dst = f"{LOG_FILE}.{i+1}"
        if os.path.exists(src):
            os.rename(src, dst)

    os.rename(LOG_FILE, f"{LOG_FILE}.1")

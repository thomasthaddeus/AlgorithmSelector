import os

def logrotate(logfile, max_size=5, backup_count=3):
    """
    Rotate the log file if it exceeds the specified size.

    Args:
        logfile (str): Path to the log file to be rotated.
        max_size (int, optional): Maximum size of the log file in MB. Defaults to 5MB.
        backup_count (int, optional): Number of backup files to keep. Defaults to 3.
    """
    if not os.path.exists(logfile):
        return

    file_size = os.path.getsize(logfile) / (1024 * 1024)  # Convert size to MB

    if file_size < max_size:
        return

    for i in range(backup_count - 1, 0, -1):
        src = f"{logfile}.{i}"
        dst = f"{logfile}.{i+1}"
        if os.path.exists(src):
            os.rename(src, dst)

    os.rename(logfile, f"{logfile}.1")

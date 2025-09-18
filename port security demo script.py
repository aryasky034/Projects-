import os
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import pyclamd

# Initialize ClamAV
clamd = pyclamd.ClamdUnixSocket()  # Use ClamdNetworkSocket() for network socket

# Directory to monitor for external drives
MONITOR_DIR = '/media'  # Change this to your external drive mount point

class DriveEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        # Check if the created event is a directory (external drive)
        if event.is_directory:
            print(f"Drive inserted: {event.src_path}")
            self.scan_drive(event.src_path)

    def scan_drive(self, drive_path):
        print(f"Scanning drive: {drive_path}")
        for root, dirs, files in os.walk(drive_path):
            for file in files:
                file_path = os.path.join(root, file)
                self.scan_file(file_path)

    def scan_file(self, file_path):
        print(f"Scanning file: {file_path}")
        result = clamd.scan(file_path)
        if result is not None:
            log_message = f"Virus detected in {file_path}: {result}\n"
            print(log_message)
            with open('scan_results.txt', 'a') as log_file:
                log_file.write(log_message)
        else:
            log_message = f"No virus found in {file_path}\n"
            print(log_message)
            with open('scan_results.txt', 'a') as log_file:
                log_file.write(log_message)

def monitor_drives():
    event_handler = DriveEventHandler()
    observer = Observer()
    observer.schedule(event_handler, MONITOR_DIR, recursive=True)
    observer.start()
    print("Monitoring for external drives...")

    # Open a log file
    with open('scan_results.txt', 'a') as log_file:
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()

if __name__ == "__main__":
    monitor_drives()
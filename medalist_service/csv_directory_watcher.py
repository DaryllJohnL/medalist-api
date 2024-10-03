import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from mongo_csv_handler import parse_and_store_csv  # Import the CSV parsing function

# Event handler to detect new CSV files
class CSVHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return None
        
        # Check if the file is a CSV
        if event.src_path.endswith('.csv'):
            print(f"New CSV file detected: {event.src_path}")
            # Add a delay to ensure file is ful ly uploaded
            time.sleep(2)
            parse_and_store_csv(event.src_path)

# Function to start the observer
def start_watching(directory_to_watch):
    event_handler = CSVHandler()
    observer = Observer()
    observer.schedule(event_handler, directory_to_watch, recursive=False)
    
    print(f"Started watching directory: {directory_to_watch}")
    observer.start()

    try:
        while True:
            time.sleep(1)  # Keep the observer running
    except KeyboardInterrupt:
        observer.stop()
    
    observer.join()

# If run directly, start watching the specified folder
if __name__ == "__main__":
    directory_to_watch = "../storage/app/medalists"  # Replace with the directory you want to monitor
    start_watching(directory_to_watch)

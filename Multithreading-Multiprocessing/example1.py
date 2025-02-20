import threading
import time

def download_file(file_name):
    print(f"Starting download: {file_name}")
    time.sleep(2)  # Simulate download time
    print(f"Download completed: {file_name}")

# Creating multiple threads
threads = []
file_names = ["file1.zip", "file2.zip", "file3.zip"]

for file in file_names:
    t = threading.Thread(target=download_file, args=(file,))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

print("All downloads completed!")

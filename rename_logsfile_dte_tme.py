import os
from datetime import datetime

def append_timestamp_to_log(log_file_path):
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(log_file_path, 'a') as log_file:
        log_file.write(f"\nTimestamp: {timestamp}\n")
        
    print(f"Timestamp '{timestamp}' added to the log file.")

def backup_log_file(log_file_path):
    
    current_date = datetime.now().strftime("%Y-%m-%d")
    log_file_dir = os.path.dirname(log_file_path)
    log_file_name = os.path.basename(log_file_path)
    new_file_name = f"{current_date}_{log_file_name}"
    new_log_file_path = os.path.join(log_file_dir, new_file_name)

    os.rename(log_file_path, new_log_file_path)
    print(f"Log file renamed to {new_file_name} for backup.")

def main():
 
    log_file_path = '/home/ubuntu/log.txt'
    
    append_timestamp_to_log(log_file_path)
    
    backup_log_file(log_file_path)

if _name_ == "_main_":
    main()

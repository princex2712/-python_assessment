# Importing Module Which Are Necessary
import os

# Funtion to create log file and store logs
def save_logs(log):
    log_file_path = os.path.join(os.path.dirname(__file__),'..','logs','logs.txt')
    with open(log_file_path,'a') as file:
        file.write(str(log)+',\n')

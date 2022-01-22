# Native
import os


# Locals
from custombkup.utils import in_format_file, fix_file_path


class Custombkup():

    def __init__(self, from_path: str, to_path: str, log_path: str) -> None:

        if not in_format_file(from_path):
            from_path = fix_file_path(from_path)
        
        if not in_format_file(to_path):
            to_path = fix_file_path(to_path)
        
        if not in_format_file(log_path):
            log_path = fix_file_path(log_path)

        self.__from = from_path
        self.__to = to_path
        self.__logpath = log_path   

        print(f'  [start]  >  Custombkup is is initialized')

    def generate(self) -> None:
        
        bkup_template: str = f'''
#!/bin/sh

##########################################################################################
#
# .Description
#   Script used to List all files where it was called, remove files with a creation date 
#   greater than 3 (three) days and complete the backup of files.
#
##########################################################################################
# .Author:  Matheus Silva
# .Github:    https://github.com/silvamva
# .Version:    0.0.1
####################################################################

# List directory and save the output in /tmp/backupsFrom.log
ls -ls -I bkup.sh -I backupsFrom.log >> /tmp/backupsFrom.log

# Move with secure the file backupsFrom.log to {self.__logpath}
mv --backup=numbered /tmp/backupsFrom.log {self.__logpath}

# Search for files with a creation date greater than 3 days, if found, delete. 
# Then list the directory and save the output to ./files.txt
find . -mtime +3 -type f -delete
ls -I bkup.sh -I files.txt >> ./files.txt

# Copy each remaining file in ./ to {self.__to}
for i in `cat files.txt`
do
    cp $i {self.__to}
done

# Delete files.txt
rm files.txt

# List directory, save the output in /tmp/backupsFrom.log and move with secure to {self.__logpath}
ls -ls -I bkup.sh -I backupsTo.log >> /tmp/backupsTo.log
mv --backup=numbered /tmp/backupsTo.log {self.__logpath}
'''
        
        with open(self.__from + 'bkup.sh', 'w') as f:
            f.write(bkup_template)
        
        print(f'  [generate]  >  Custombkup create bkup.sh file in the path: {self.__from}') 

    def execute(self) -> None:
        os.chdir(self.__from)
        os.system('bash bkup.sh')
        print(f'  [execute]  >  Custombkup run bkup.sh file in the path: {self.__from}')

    def cleanup(self) -> None:
        print(f'  [backup]  >  Custombkup copy files to the path: {self.__to}')
        print(f'  [log]  >  Custombkup create log files in the path: {self.__logpath}')

        os.chdir(self.__from)
        os.system('rm bkup.sh')

        print(f'  [cleanup]  >  Custombkup remove bkup.sh file in the path: {self.__from}')
        print(f'  [complete]  >  Custombkup complete the task\n')

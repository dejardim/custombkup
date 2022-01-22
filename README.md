# Custombkup
Custombkup is a super easy CLI built in Python for simple backup. Its purpose is to make the execution of the bkup.sh script more practical and customizable.

```
$ bkup --help
usage: bkup [-h] [-fp FROMPATH] [-tp TOPATH] [-lp LOGPATH]

optional arguments:
  -h, --help            show this help message and exit
  -fp FROMPATH, --frompath FROMPATH
  -tp TOPATH, --topath TOPATH
  -lp LOGPATH, --logpath LOGPATH
```


## Installing
Install and update using python venv and pip (or Makefile):

```bash
# Clone the repository
❯ git clone git@github.com:silvamva/custombkup.git

# Enter project directory
❯ cd custombkup

# Create a python venv
❯ python3 -m venv venv # Ubuntu 20.04

# Install custombkup inside python venv
❯ source venv/bin/activate
❯ pip install -e .

# Alternative use make command
❯ source venv/bin/activate
❯ make install
```



## A Simple Example

How run custombkup:

```bash
# Run custombkup inserting args
# WARNING: bkup.sh excludes files older than 3 days of creation
❯ custombkup

# Alternative 
❯ bkup -fp /home/testFolder/from -tp /home/testFolder/to -lp /home/testFolder
```
```

  Stages Status | Custombkup                                                          v0.0.1
----------------------------------------------------------------------------------------------    
    
  [start]  >  Custombkup is is initialized
  [generate]  >  Custombkup create bkup.sh file in the path: /home/testFolder/from/
  [execute]  >  Custombkup run bkup.sh file in the path: /home/testFolder/from/
  [backup]  >  Custombkup copy files to the path: /home/testFolder/to/
  [log]  >  Custombkup create log files in the path: /home/testFolder/
  [cleanup]  >  Custombkup remove bkup.sh file in the path: /home/testFolder/from/
  [complete]  >  Custombkup complete the task

```

## Uninstalling

Uninstall using pip:

```bash
❯ pip uninstall custombkup                                       
```

Uninstall using Makefile:

```bash
# Enter project directory
❯ cd custombkup

# Uninstall via Makefile
❯ make uninstall
```

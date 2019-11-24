# intro / how to run
There are three folders in the project submission. Phase1, phase2, phase3. The appropriate files for each file must exist in each folder. A given phase will only write files inside the current working directory. 

To run phase 1, cd into phase1 dir, NEXT, run the command ‘make’ this will make the executable ‘parse’. The contents of the xml file must be piped into the parse executable as such:
```
Cat example.xml | ./parse
```
The outputted .txt files will be created in the directory after about 4.5 minutes if there are 1million lines. 

To run phase 2, move the .txt files from phase1 folder into the phase2 folder. Cd into phase2. Run the command
```
./phase2.sh
```
Which does 4 parallel pipes, sorts, perl scrubbing, db_loads to create the idx files in the phase2 directory. This should take at most 30 seconds.

To run phase3, move the idx files from phase2 directory into the phase3 directory and then run the command 
```
Python3 phase3.py
```
Which will start the CLI to the database. To exit the database type in the command exit() or hit Ctrl+C/ 


# The layout

there are some testing files still present in this project... ignore them. For the most part each phase directory is self sufficnet. 
.
├── README.md
├── deprecated
│   ├── dragonshell.cc
│   └── phase2.py
├── phase1
│   ├── 1k.xml
│   ├── 1m-helper
│   │   ├── 1k-body.txt
│   │   └── generate_1m.sh
│   ├── fast_enough.png
│   ├── makefile
│   └── parse.cpp
├── phase2
│   ├── 1k-tests
│   │   ├── dates.txt
│   │   ├── emails.txt
│   │   ├── recs.txt
│   │   └── terms.txt
│   ├── break.pl
│   └── phase2.sh
└── phase3
    ├── bdb_helper.py
    ├── dates.py
    ├── emails.py
    ├── helper.py
    ├── phase3.py
    └── terms.py


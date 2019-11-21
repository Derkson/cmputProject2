# The plan
.
├── dates.py
├── emails.py
├── phase3.py
└── terms.py

phase3 will be the main python file which will make calls to the other modules. Each of the modules has a process_type_q() function which is expected to return the string it was passed, MINUS the command it just parsed out. 

In the future these process_type_q might also return a class with all the logic that was parsed out of the statements.

Handle_command essentially pops valid commands off the original input until there is nothing left to parse 

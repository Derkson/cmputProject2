#!/bin/bash 

sort terms.txt | perl break.pl | python3 phase2.py --prefix=terms --db_type=btree &
sort emails.txt | perl break.pl | python3 phase2.py --prefix=emails --db_type=btree &
sort dates.txt | perl break.pl | python3 phase2.py --prefix=dates --db_type=btree &
sort recs.txt | perl break.pl | python3 phase2.py --prefix=recs --db_type=hash

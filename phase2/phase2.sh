#!/bin/bash 

sort terms.txt  | perl break.pl  | db_load -T -t btree te.idx &
sort emails.txt | perl break.pl  | db_load -T -t btree em.idx &
sort dates.txt  | perl break.pl  | db_load -T -t btree da.idx &
sort recs.txt   | perl break.pl  | db_load -T -t hash  re.idx &
wait

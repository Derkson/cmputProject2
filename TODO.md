# Phase 3 (query languages)

## examples
 - subj:gas
 - subj:gas body:earning
 - confidential%
 - from:phillip.allen@enron.com
 - to:phillip.allen@enron.com
 - to:kenneth.shulklapper@enron.com  to:keith.holst@enron.com
 - date:2001/03/15
 - date>2001/03/10
 - bcc:derryl.cleaveland@enron.com  cc:jennifer.medcalf@enron.com
 - body:stock  confidential  shares  date<2001/04/12

## grammar

```
alphanumeric    ::= [0-9a-zA-Z_-]
numeric		::= [0-9]
date            ::= numeric numeric numeric numeric '/' numeric numeric '/' numeric numeric
datePrefix      ::= 'date' whitespace* (':' | '>' | '<' | '>=' | '<=')
dateQuery       ::= datePrefix whitespace* date
emailterm	::= alphanumeric+ | alphanumeric+ '.' emailterm
email		::= emailterm '@' emailterm
emailPrefix	::= (from | to | cc | bcc) whitespace* ':'
emailQuery	::= emailPrefix whitespace* email
term            ::= alphanumeric+
termPrefix	::= (subj | body) whitespace* ':'
termSuffix      ::= '%' 
termQuery       ::= termPrefix? whitespace* term termSuffix?

expression      ::= dateQuery | emailQuery | termQuery 
query           ::= expression (whitespace expression)*

modeChange	::= 'output=full' | 'output=brief'

command		::= query | modeChange
```




# Phase 2 (TODO indicies)


## create the following four indexes:

(1) a hash index on recs.txt with row ids as keys and the full email record as data,
	- rowID
	- full record
 
(2) a B+-tree index on terms.txt with terms as keys and row ids as data, 
	- K: terms
	- V: row ID

(3) a B+-tree index on emails.txt with emails as keys and row ids as data, and
	- K: emails
	- V: row ID
 
(4) a B+-tree index on dates.txt with dates as keys and row ids as data.
	- K: dates
	- V: row ID	 


## Help

You should note that the keys in all four cases are the character strings before colon ':' and the data is everything that comes after the colon.

Use the db_load command to build your indexes. db_load by default expects keys in one line and data in the next line. Also db_load treats backslash as a special character and you want to avoid backslash in your input. Here is a simple Perl script that converts input records into what db_load expects and also removes backslashes.

Your program for Phase 2 would produce four indexes which should be named re.idx, te.idx, em.idx,  and da.idx respectively corresponding to indexes 1, 2, 3, and 4, as discussed above. It can be noted that the keys in re.idx are unique but the keys in all indexes can have duplicates.

In addition to db_load, you may also find db_dump with option p useful as you are building and testing the correctness of your indexes.

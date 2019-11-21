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

## in general...
A command is either a mode change or a query. A query consists of any number of sub queries separated by whitespace. Sub queries are made of 3 types, email, date, or term queries. Each sub query is relativily simple. 

## Pseudo code
```python
# process_X_q appends to some list of queries 
# with the search properties parsed out

while remaining != "":
	str = remaining.strip()
	if start(str) is "date":
		remaining = process_date_q(str)
	elif start(str) in ['to', 'from', 'cc', 'bcc']:
		remaining = process_email_q(str):
	else:
		remaining = process_term_q(str)
```



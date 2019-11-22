import re

def process_term_q(cmd):
	#print("Processing terms.....")

	regex = "((subj|body)?(\s)*:)?(\s)*[0-9a-zA-Z_-]+[%]?"
	matcher = re.search(regex, cmd)
	term_q = matcher.group(0)
	
	prefix = ""
	if ":" in term_q:
		# ASSUMPTION: only one semi colon in term_q
		prefix, term_q = term_q.split(":")
		prefix = prefix.strip()
		term_q = term_q.strip()

	wildcard = term_q.strip()[-1] == '%'	
	term = ""
	if wildcard:
		term = term_q[:-1]
	else:
		term = term_q
	obj = (prefix, term, wildcard, )		
		
	# return everything that isnt the term query
	return cmd[matcher.span()[1]:], obj


if __name__ == "__main__":
	
	print("term tests")
	assert( process_term_q("body:termm_-90    ")[0] =="    ") 
	assert( process_term_q("subj:termm_-123   ")[0] =="   ") 
	assert( process_term_q("body:  termm_-23  ")[0] =="  ") 
	assert( process_term_q("subj  : termm-_90 ")[0] ==" ") 
	assert( process_term_q("termmmm-_90 ")[0] ==" ") 
	assert( process_term_q("termm-_90   ")[0] =="   ") 
	
	print("suffix tests")
	assert( process_term_q("subj  : termm-_90% ")[0] ==" ") 
	assert( process_term_q("body:  termm_-23%  ")[0] =="  ") 
	assert( process_term_q("body:termm_-90%    ")[0] =="    ") 
	assert( process_term_q("subj:termm_-123%   ")[0] =="   ")
	assert( process_term_q("termmmm-_90% ")[0] ==" ") 
	assert( process_term_q("termm-_90%   ")[0] =="   ") 

	
	print("Just the word body or subj")
	assert( process_term_q("body%   ")[0] =="   ") 
	assert( process_term_q("subj%   ")[0] =="   ") 
	assert( process_term_q("subj %   ")[0] ==" %   ")
	 
	# TODO: invalid tests 
	# "body    :    " 


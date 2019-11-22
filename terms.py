import re

def process_term_q(cmd):
	#print("Processing terms.....")

	regex = "((subj|body)?(\s)*:)?(\s)*[0-9a-zA-Z_-]+[%]?"
	matcher = re.search(regex, cmd)
	#print("Term q: {}".format(matcher.group(0)))

	
	# return everything that isnt the term query
	return cmd[matcher.span()[1]:]


if __name__ == "__main__":
	
	print("term tests")
	assert( process_term_q("body:termm_-90    ") =="    ") 
	assert( process_term_q("subj:termm_-123   ") =="   ") 
	assert( process_term_q("body:  termm_-23  ") =="  ") 
	assert( process_term_q("subj  : termm-_90 ") ==" ") 
	assert( process_term_q("termmmm-_90 ") ==" ") 
	assert( process_term_q("termm-_90   ") =="   ") 
	
	print("suffix tests")
	assert( process_term_q("subj  : termm-_90% ") ==" ") 
	assert( process_term_q("body:  termm_-23%  ") =="  ") 
	assert( process_term_q("body:termm_-90%    ") =="    ") 
	assert( process_term_q("subj:termm_-123%   ") =="   ")
	assert( process_term_q("termmmm-_90% ") ==" ") 
	assert( process_term_q("termm-_90%   ") =="   ") 

	
	print("Just the word body or subj")
	assert( process_term_q("body%   ") =="   ") 
	assert( process_term_q("subj%   ") =="   ") 
	assert( process_term_q("subj %   ") ==" %   ")
	 
	# TODO: invalid tests 
	# "body    :    " 


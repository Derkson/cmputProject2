import re

def process_term_q(cmd):
	regex = "((subj|body)?(\s)*:)?(\s)*[0-9a-zA-Z_-]+[%]?"
	matcher = re.search(regex, cmd)
	if matcher == None:
		raise Exception("Error: parsing term query: {}".format(cmd))
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
	def test_proc(cmd, e_rem, e_obj):
		rem, obj = process_term_q(cmd)
		assert(rem == e_rem)
		assert( obj == e_obj) 
			
	print("running tests...")
	test_proc("body:tm_-90    ","    ",('body', 'tm_-90', False)) 
	test_proc("subj:tem_-123   ","   ",('subj', 'tem_-123', False) ) 
	test_proc("body:  m_-23  ","  ", ('body','m_-23',False)) 
	test_proc("subj  : term-_90 "," ",('subj','term-_90',False) ) 
	test_proc("termmmm-_90 "," ",("",'termmmm-_90',False) ) 
	test_proc("termm-_90   ","   ",("",'termm-_90',False) ) 
	
	test_proc("subj  : termm-_90% "," ",('subj','termm-_90',True) ) 
	test_proc("body:  termm_-23%  ","  ",('body','termm_-23',True) ) 
	test_proc("body:termm_-90%    ","    ",('body','termm_-90',True) ) 
	test_proc("subj:termm_-123%   ","   ",('subj','termm_-123',True) )
	test_proc("termmmm-_90% "," ",("",'termmmm-_90',True) ) 
	test_proc("termm-_90%   ","   ",("",'termm-_90',True) ) 

	test_proc("body%   ","   ",("",'body',True) ) 
	test_proc("subj%   ","   ",("",'subj',True) ) 
	test_proc("subj %   "," %   ",("",'subj',False) )
	 
	# TODO: invalid tests 
	# "body    :    " 


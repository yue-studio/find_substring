# find_substring

Trying to build a regular expression engine doing:

For your programming challenge, we'd like you to implement a simple string search application. The user inputs a regular expression (e.g. A.*32b+Y), an input file name to parse, and will output all indices with the matching regular expression (e.g. Found AJT32bbY at index 45, line 235).  Implement the regular expression parser from scratch and as a Python/Golang package that's called by the app.  The regular expression grammar is limited to just the elements below, and you can assume either a 'greedy' or 'lazy' match policy -- be sure to specify which.  You may use existing libraries in the wild except for the regular expression parser which must be your implementation.

Regular expression grammar:
	.					#match any 1 character
	*					#wildcard, match the previous letter or '.' 0 or more times
	+					#wildcard, match the previous letter 1 or more times
	Any letter or number	#[a-zA-Z0-9]

Application command line:
	find_substring <input file>  '<regular_expression>'
	Example:  find_substring  dna_sequence.txt  'AT+CG.*'
 



The code should be correct and the regular expression parser implemented from scratch.  Show that the application correctly matches all substrings according to your stated lazy or greedy match policy and passes your provided test examples. 

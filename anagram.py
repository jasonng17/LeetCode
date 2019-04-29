'''
Problem
Given two strings, check to see if they are anagrams. An anagram is when the two strings
can be written using the exact same letters (so you can just rearrange the letters to get
a different phrase or word).

For example:
"public relations" is an anagram of "crap built on lies."
"clint eastwood" is an anagram of "old west action"
Note: Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" and "o d g".
'''

from nose.tools import assert_equal

# Approach 1: using python default functions
def anagram_1(s1, s2):
	s1 = s1.replace(' ', '').lower()
	s2 = s2.replace(' ', '').lower()
	return sorted(s1) == sorted(s2)

# Approach 2: using hashmaps
def anagram_2(s1, s2):
	s1 = s1.strip().lower()
	s2 = s2.strip().lower()
	print(s1)
	smap1 = {}
	for s in s1:
		if s in smap1.keys():
			smap1[s] += 1
		else:
			smap1[s] = 1
	for s in s2:
		if s in smap1.keys():
			smap1[s] -= 1
	for k in smap1:
		if smap1[k] != 0:
			return False
	return True

class AnagramTest(object):
    
    def test(self,sol):
        assert_equal(sol('go go go','gggooo'),True)
        assert_equal(sol('abc','cba'),True)
        assert_equal(sol('hi man','hi     man'),True)
        assert_equal(sol('aabbcc','aabbc'),False)
        assert_equal(sol('123','1 2'),False)
        print ("ALL TEST CASES PASSED")

if __name__ == '__main__':
	if anagram_2('go go go','gggooo'):
		print('True')
	else:
		print('False')
	
	# Run Tests
	t = AnagramTest()
	t.test(anagram_1)
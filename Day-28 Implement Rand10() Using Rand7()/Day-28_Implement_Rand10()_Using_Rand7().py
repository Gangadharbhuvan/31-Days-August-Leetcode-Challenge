'''
	Given a function rand7 which generates a uniform random integer in the range 1 to 7, write a function rand10 which generates a uniform random integer in the range 1 to 10.

Do NOT use system's Math.random().

 

Example 1:

Input: 1
Output: [7]
Example 2:

Input: 2
Output: [8,4]
Example 3:

Input: 3
Output: [8,1,10]
 

Note:

rand7 is predefined.
Each testcase has one argument: n, the number of times that rand10 is called.
 

Follow up:

What is the expected value for the number of calls to rand7() function?
Could you minimize the number of calls to rand7()?


'''

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        
        
        while True:
		
			# generate a random number from 1 ~ 49 with uniform distribution
            random_num = ( rand7() - 1 ) * 7 + rand7()
            
            if random_num <= 40:
			
			    # map 1 ~ 40 to 1 ~ 10 by modulo operation with offset
                return random_num % 10 + 1
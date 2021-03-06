'''
	Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?

'''

class Solution:
    def isPowerOfFour(self, num):
        s = bin(num)[3:]
        return num!=0 and ('1' not in s) and len(s)%2 == 0

        
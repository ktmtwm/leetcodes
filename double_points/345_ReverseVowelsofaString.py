"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
"""
class Solution(object):
    def __init__(self):
        self.vowels = ['a', 'e', 'i', 'o', 'u',
        			   'A', 'E', 'I', 'O', 'U']

    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str

        PS: s = ""
        """
        # turn string s to list
        list_s = []
        for i in s:
            list_s.append(i)

        start_i = 0
        end_j = len(list_s) - 1

        while start_i < end_j:
            while list_s[start_i] not in self.vowels and start_i < end_j:
                start_i = start_i + 1

            while list_s[end_j] not in self.vowels and start_i < end_j:
                end_j = end_j - 1
            
            # exchange
            tmp = list_s[start_i]
            list_s[start_i] = list_s[end_j]
            list_s[end_j] = tmp
            
            # continue
            start_i = start_i + 1
            end_j = end_j - 1
        return ''.join(list_s)

if __name__ == "__main__":
    solut = Solution()
    s = "leetcode"
    print solut.reverseVowels(s)
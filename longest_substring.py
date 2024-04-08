"""Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces."""

from collections import Counter

def longest_substring(string: str):
    result = 0
    saved_words = []
    counter = 0
    word = Counter(string)

    for i in range(len(string)):
        
        if len(word.most_common()) <= 1:
            result = 1
            break

        counter = len(saved_words)

        if string[i] in saved_words[0: -1]:
            
            if counter > result:
                result = counter

            saved_words = []

        saved_words.append(string[i])



    return result


print(longest_substring('werwwwertuiwwwwww'))



# code provided by copilot #

def longest_substringv2(s: str) -> int:
    start = 0
    max_length = 0
    used_char = {}

    for i in range(len(s)):
        if s[i] in used_char and start <= used_char[s[i]]:
            start = used_char[s[i]] + 1
        else:
            max_length = max(max_length, i - start + 1)

        used_char[s[i]] = i

    return max_length


print(longest_substringv2('werwwwertuiwwwwww'))


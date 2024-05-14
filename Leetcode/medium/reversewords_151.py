import collections
class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        i = 0
        next_word = True
        for character in s:
            if character.isalnum() and next_word:
                next_word = False
                words.append(character)

            elif character.isalnum() and not next_word:
                words[i] += character

            elif character == ' ' and not next_word:
                next_word = True
                i += 1

            elif character == ' ' and next_word:
                continue

        revers = ''
        for i in range(len(words) - 1):
            revers += words.pop() + ' '
        return revers + words.pop()
    
    def reverseWords_better(self, s: str) -> str:
        string_builder = collections.deque() # double-ended queue
        start = -1
        i =0 
        while i < len(s):
            if s[i] != ' ':
                start = i

                while i < len(s) and s[i] != " ":
                    i += 1
                
                string_builder.appendleft(s[start: i])

                i -= 1
            i += 1
        return " ".join(string_builder)
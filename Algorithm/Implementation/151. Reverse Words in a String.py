class Solution(object):
    def reverseWords(self, s):
        arr = s.split()
        arr.reverse()
        return " ".join(arr)

# class Solution(object):
#     def reverseWords(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         result = ""
#         word = ""
#         for i in range(len(s)):
#             print(s[i], word)
#             if s[i] == " ":
#                 if word != " ":
#                     result = word + result
#                     word = " "
#             else:
#                 if word == " ":
#                     result = word + result
#                     word = ""
#                 word += s[i]
#         result = word + result
#         return result.strip()
            
        

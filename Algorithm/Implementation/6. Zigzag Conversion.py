class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        result = [[] for _ in range(numRows)]
        cycle = (numRows*2 - 2)
        if cycle == 0:
            return s
        for i in range(len(s)):
            #print(i%cycle, s[i], result)
            if i % cycle < numRows:
                result[i % cycle].append(s[i])
            else:   # nR =4, 4-2 5-1 / 10-2, 11-1
                result[cycle - i % cycle ].append(s[i])
        answer = "" 
        for r in result:
            answer += "".join(r)
        return answer

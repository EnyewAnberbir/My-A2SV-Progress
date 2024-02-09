class Solution:
    def maxScore(self, s: str) -> int:
        prefix_sum = [0]
        for i in range(len(s)):
            if s[i] == "0":
                prefix_sum.append(prefix_sum[-1]+1)
            else:
                prefix_sum.append(prefix_sum[-1]+0)
        suffix_sum = [0]
        for i in range(len(s)-1,-1,-1):
            if s[i] == "1":
                suffix_sum.append(suffix_sum[-1]+1)
            else:
                suffix_sum.append(suffix_sum[-1]+0)
        i = 1
        j = len(prefix_sum)-2
        ans = []
        maxi = 0
        while i < len(prefix_sum)-1 and j > 0:
            temp = prefix_sum[i] + suffix_sum[j]
            maxi = max(maxi, temp)
            ans.append(temp)
            i+=1
            j-=1

        return maxi

        




        
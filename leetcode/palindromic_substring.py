

class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = [0, 0]
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if answer[1] - answer[0] < r - l:
                    answer[0], answer[1] = [l, r]

                l -= 1
                r += 1

        for i in range(len(s)):
            l, r = i, i + 1
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if answer[1] - answer[0] < r - l:
                    answer[0], answer[1] = [l, r]

                l -= 1
                r += 1

        return s[answer[0]:answer[1]+1]            



strings = "cbbd"

sol = Solution()
answer = sol.longestPalindrome(strings)
print(f"answer : {answer}")

class Solution:
    def lengthOfLongestSubstring(self, s: str) ->int:
        answer, left, check = 0, 0, set()

        for right, ch in enumerate(s):
            if ch not in check:
                check.add(ch)
                answer = max(answer, (right - left) + 1)
            else:
                while left <= right and ch in check:
                    if s[left] in check:
                        check.remove(s[left])
                    left += 1
                    print(ch)
                check.add(ch)       

        return answer


sol = Solution()             
print(sol.lengthOfLongestSubstring("abcdac"))


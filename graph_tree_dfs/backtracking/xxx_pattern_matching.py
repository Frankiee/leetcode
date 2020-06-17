# [Backtracking, Classic]
# https://leetcode.com/discuss/interview-question/124709/pattern-matching
# Pattern Matching

# History:
# Dropbox
# 1.
# Feb 27, 2020

# Given a pattern and a string input - find if the string follows the same pattern and return
# true or false.
#
# Examples:
#
# Pattern : "abab", input: "redblueredblue" should return true.
# Pattern: "aaaa", input: "asdasdasdasd" should return true.
# Pattern: "aabb", input: "xyzabcxzyabc" should return false.
from collections import defaultdict


class Solution(object):
    def dfs(self, pattern_idx, pattern, curr_text_start_idx, text_idx, text, mapping):
        if text_idx >= len(text):
            return curr_text_start_idx == len(text) and pattern_idx == len(pattern)

        if pattern[pattern_idx] in mapping:
            pattern_end = curr_text_start_idx + len(mapping[pattern[pattern_idx]])
            if pattern_end <= len(text) and mapping[pattern[pattern_idx]] == text[curr_text_start_idx:pattern_end]:
                return self.dfs(pattern_idx+1, pattern, pattern_end, pattern_end+1, text, mapping)
            else:
                return False
        else:
            if self.dfs(pattern_idx, pattern, curr_text_start_idx, text_idx+1, text, mapping):
                return True
            else:
                mapping[pattern[pattern_idx]] = text[curr_text_start_idx:text_idx]
                if self.dfs(pattern_idx+1, pattern, text_idx, text_idx+1, text, mapping):
                    return True
                del mapping[pattern[pattern_idx]]

        return False

    def match_pattern(self, pattern, text):
        mapping = defaultdict(str)
        return self.dfs(0, pattern, 0, 1, text, mapping)


s = Solution()

print s.match_pattern("abab", "redblueredblue")
print s.match_pattern("aaaa", "asdasdasdasd")
print s.match_pattern("aabb", "xyzabcxzyabc")

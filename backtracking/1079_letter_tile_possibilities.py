# https://leetcode.com/problems/letter-tile-possibilities/
# 1079. Letter Tile Possibilities

# You have a set of tiles, where each tile has one letter tiles[i] printed
# on it.  Return the number of possible non-empty sequences of letters you
# can make.
#
#
#
# Example 1:
#
# Input: "AAB"
# Output: 8
# Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB",
# "ABA", "BAA".
#
# Example 2:
#
# Input: "AAABBC"
# Output: 188
#
#
# Note:
#
# 1 <= tiles.length <= 7
# tiles consists of uppercase English letters.


class Solution(object):
    def dfs(self, ret, tiles, used, prefix):
        ret.append(prefix)

        for i in range(len(tiles)):
            if used[i]:
                continue

            if i > 0 and tiles[i] == tiles[i - 1] and not used[i - 1]:
                continue

            used[i] = True
            self.dfs(ret, tiles, used, copy.copy(prefix) + tiles[i])
            used[i] = False

    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        tiles = sorted(tiles)
        ret = []
        used = [False] * len(tiles)

        self.dfs(ret, tiles, used, "")

        # Remove the empty string
        return len(ret) - 1

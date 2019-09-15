# [DP-Sequence-Action]
# https://leetcode.com/problems/zuma-game/
# 488. Zuma Game

# Think about Zuma Game. You have a row of balls on the table, colored red(
# R), yellow(Y), blue(B), green(G), and white(W). You also have several
# balls in your hand.
#
# Each time, you may choose a ball in your hand, and insert it into the row
# (including the leftmost place and rightmost place). Then, if there is a
# group of 3 or more balls in the same color touching, remove these balls.
# Keep doing this until no more balls can be removed.
#
# Find the minimal balls you have to insert to remove all the balls on the
# table. If you cannot remove all the balls, output -1.
#
# Examples:
#
# Input: "WRRBBW", "RB"
# Output: -1
# Explanation: WRRBBW -> WRR[R]BBW -> WBBW -> WBB[B]W -> WW
#
# Input: "WWRRBBWW", "WRBRW"
# Output: 2
# Explanation: WWRRBBWW -> WWRR[R]BBWW -> WWBBWW -> WWBB[B]WW -> WWWW -> empty
#
# Input:"G", "GGGGG"
# Output: 2
# Explanation: G -> G[G] -> GG[G] -> empty
#
# Input: "RBYYBBRRB", "YRBGB"
# Output: 3
# Explanation: RBYYBBRRB -> RBYY[Y]BBRRB -> RBBBRRB -> RRRB -> B -> B[B] ->
# BB[B] -> empty
#
# Note:
# 1. You may assume that the initial row of balls on the table won’t have any 3
# or more consecutive balls with the same color.
# 2. The number of balls on the table won't exceed 20, and the string
# represents these balls is called "board" in the input.
# 3. The number of balls in your hand won't exceed 5, and the string represents
# these balls is called "hand" in the input.
# 4. Both input strings will be non-empty and only contain characters 'R','Y',
# 'B','G','W'.


from collections import Counter
import copy


class Solution(object):
    def dfs(self, board_seq_counter, hand_counter, current_balls_count):
        if not board_seq_counter:
            return current_balls_count
        if not hand_counter:
            return -1

        possible_ways = -1
        for idx in range(len(board_seq_counter)):
            char, count = board_seq_counter[idx]

            if count + hand_counter[char] < 3:
                continue

            insertion_count = 3 - count

            hand_counter[char] -= insertion_count
            if hand_counter[char] == 0:
                del hand_counter[char]

            board_seq_counter_copy = copy.deepcopy(board_seq_counter)
            board_seq_counter_copy.pop(idx)
            while 0 < idx < len(board_seq_counter_copy):
                if (board_seq_counter_copy[idx][0] ==
                        board_seq_counter_copy[idx - 1][0]):
                    board_seq_counter_copy[idx - 1][1] += (
                        board_seq_counter_copy[idx][1])
                    board_seq_counter_copy.pop(idx)

                    if board_seq_counter_copy[idx - 1][1] > 2:
                        board_seq_counter_copy.pop(idx - 1)
                        idx = idx - 1
                    else:
                        break
                else:
                    break

            current_way = self.dfs(
                board_seq_counter_copy,
                hand_counter,
                current_balls_count + insertion_count,
            )

            if char not in hand_counter:
                hand_counter[char] = insertion_count
            else:
                hand_counter[char] += insertion_count

            if current_way != -1:
                if possible_ways == -1:
                    possible_ways = current_way
                else:
                    possible_ways = min(possible_ways, current_way)

        return possible_ways

    def _to_sequence_counter(self, string):
        str_c = []

        current_char = None
        current_char_count = None
        for c in string:
            if not current_char:
                current_char = c
                current_char_count = 1
            elif current_char != c:
                str_c.append([current_char, current_char_count])
                current_char = c
                current_char_count = 1
            else:
                current_char_count += 1

        if current_char:
            str_c.append([current_char, current_char_count])

        return str_c

    def findMinStep(self, board, hand):
        """
        :type board: str
        :type hand: str
        :rtype: int
        """
        board_seq_counter = self._to_sequence_counter(board)
        hand_counter = Counter(hand)

        return self.dfs(board_seq_counter, hand_counter, 0)

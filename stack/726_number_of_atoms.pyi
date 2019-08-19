# [Important]
# https://leetcode.com/problems/number-of-atoms/
# 726. Number of Atoms

# Given a chemical formula (given as a string), return the count of each atom.
#
# An atomic element always starts with an uppercase character, then zero or
# more lowercase letters, representing the name.
#
# 1 or more digits representing the count of that element may follow if the
# count is greater than 1. If the count is 1, no digits will follow. For
# example, H2O and H2O2 are possible, but H1O2 is impossible.
#
# Two formulas concatenated together produce another formula. For example,
# H2O2He3Mg4 is also a formula.
#
# A formula placed in parentheses, and a count (optionally added) is also a
# formula. For example, (H2O2) and (H2O2)3 are formulas.
#
# Given a formula, output the count of all elements as a string in the
# following form: the first name (in sorted order), followed by its count (
# if that count is more than 1), followed by the second name (in sorted
# order), followed by its count (if that count is more than 1), and so on.
#
# Example 1:
# Input:
# formula = "H2O"
# Output: "H2O"
# Explanation:
# The count of elements are {'H': 2, 'O': 1}.
#
# Example 2:
# Input:
# formula = "Mg(OH)2"
# Output: "H2MgO2"
# Explanation:
# The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
#
# Example 3:
# Input:
# formula = "K4(ON(SO3)2)2"
# Output: "K4N2O14S4"
# Explanation:
# The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
#
# Note:
#
# All atom names consist of lowercase letters, except for the first
# character which is uppercase.
# The length of formula will be in the range [1, 1000].
# formula will only consist of letters, digits, and round parentheses,
# and is a valid formula as defined in the problem.


from collections import defaultdict


class Solution(object):
    def add_num(self):
        if self.num or not self.explicit_num or self.is_close_parentheses:
            num = self.num or 1
            if self.is_close_parentheses:
                last_dict = self.stack.pop()
                second_last_dict = self.stack[-1]

                for element, count in last_dict.iteritems():
                    second_last_dict[element] += count * num
                self.current_element = None
            else:
                self.stack[-1][self.current_element] += num
                self.explicit_num = True

            self.current_element = None
            self.is_close_parentheses = False
            self.num = None

    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        self.stack = [defaultdict(int)]

        self.num = None
        self.is_close_parentheses = False
        self.current_element = None
        self.explicit_num = True
        for c in formula:
            if c.islower():
                self.current_element += c
            elif c.isupper():
                self.add_num()

                self.current_element = c
                self.explicit_num = False
            elif c == '(':
                self.add_num()

                self.current_element = None
                self.stack.append(defaultdict(int))
            elif c == ')':
                self.add_num()
                self.is_close_parentheses = True
            else:
                if not self.num:
                    self.explicit_num = True
                    self.num = int(c)
                else:
                    self.num = self.num * 10 + int(c)

        self.add_num()

        elements = sorted(self.stack[-1].items())
        ret = ""
        for element, count in elements:
            ret += str(element)
            if count > 1:
                ret += str(count)
        return ret

# [Archived]
# https://leetcode.com/problems/defanging-an-ip-address/
# 1108. Defanging an IP Address

# History:
# Facebook
# 1.
# Mar 8, 2020
# 2.
# May 10, 2020

# Given a valid (IPv4) IP address, return a defanged version of that IP address.
#
# A defanged IP address replaces every period "." with "[.]".
#
#
#
# Example 1:
#
# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"
# Example 2:
#
# Input: address = "255.100.50.0"
# Output: "255[.]100[.]50[.]0"
#
#
# Constraints:
#
# The given address is a valid IPv4 address.


class SolutionReplace(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return address.replace(".", "[.]")


class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return '[.]'.join(address.split('.'))

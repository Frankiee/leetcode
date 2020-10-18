# https://leetcode.com/problems/smallest-common-region/
# 1257. Smallest Common Region

# history
# Airbnb
# 1.
# Oct 17, 2020

# You are given some lists of regions where the first region of each list includes all other regions in that list.
#
# Naturally, if a region X contains another region Y then X is bigger than Y.
# Also by definition a region X contains itself.
#
# Given two regions region1, region2, find out the smallest region that contains both of them.
#
# If you are given regions r1, r2 and r3 such that r1 includes r3,
# it is guaranteed there is no r2 such that r2 includes r3.
#
# It's guaranteed the smallest region exists.
#
#
#
# Example 1:
#
# Input:
# regions = [["Earth","North America","South America"],
# ["North America","United States","Canada"],
# ["United States","New York","Boston"],
# ["Canada","Ontario","Quebec"],
# ["South America","Brazil"]],
# region1 = "Quebec",
# region2 = "New York"
# Output: "North America"
#
#
# Constraints:
#
# 2 <= regions.length <= 10^4
# region1 != region2
# All strings consist of English letters and spaces with at most 20 letters.

# Bottom-Up
class SolutionBottomUp(object):
    def findSmallestRegion(self, regions, region1, region2):
        """
        :type regions: List[List[str]]
        :type region1: str
        :type region2: str
        :rtype: str
        """
        parent = {
            c: region[0]
            for region in regions
            for c in region[1:]
        }

        region1_ancestors = set()

        while region1 in parent:
            region1_ancestors.add(region1)
            region1 = parent[region1]
        region1_ancestors.add(region1)

        while region2 not in region1_ancestors:
            region2 = parent[region2]

        return region2

# Top-Down
class SolutionTopDown(object):
    def _dfs(self, curr_node, tree, region1, region2):
        all_regions = []
        if curr_node in tree:
            for child in tree[curr_node]:
                ret, included_regions = self._dfs(child, tree, region1, region2)
                if ret:
                    return ret, included_regions
                all_regions.extend(included_regions)

        if curr_node == region1 or curr_node == region2:
            all_regions.append(curr_node)

        if len(all_regions) == 2:
            return curr_node, all_regions

        return None, all_regions

    def findSmallestRegion(self, regions, region1, region2):
        """
        :type regions: List[List[str]]
        :type region1: str
        :type region2: str
        :rtype: str
        """
        children = set()

        tree = {
            region[0]: region[1:]
            for region in regions
        }

        for values in tree.values():
            children |= set(values)
        root = None
        for key in tree.keys():
            if key not in children:
                root = key
                break

        ret, _ = self._dfs(root, tree, region1, region2)

        return ret

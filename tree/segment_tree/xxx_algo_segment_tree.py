# [Algorithm, Segment-Tree]
# https://www.youtube.com/watch?v=rYBtViWXYeI&list=PLLuMmzMTgVK5Hy1qcWYZcd7wVQQ1v0AjX&index=7&t=735s


class SegmentTreeNode(object):
    def __init__(self, start, end, sum, left, right):
        self.start = start
        self.end = end
        self.sum = sum           # can be max/min etc.
        self.left = left
        self.right = right


# Time complexity O(n)
def build_tree(start, end, vals):
    if start == end:
        return SegmentTreeNode(start, end, vals[start])

    mid = (start + end) / 2

    left = build_tree(start, mid, vals)
    right = build_tree(mid+1, end, vals)

    return SegmentTreeNode(
        start,
        end,
        left.sum + right.sum,
        left,
        right,
    )


# Time complexity O(log(n))
def update_tree(root, index, val):
    if root.start == root.right == index:
        root.sum = val
        return

    mid = (root.start + root.end) / 2

    if index <= mid:
        update_tree(root.left, index, val)
    else:
        update_tree(root.right, index, val)

    root.sum = root.left.sum + root.right.sum


def query_sum(root, l, r):
    if root.left == l and root.right == r:
        return root.sum

    mid = (root.start + root.end) / 2

    if r <= mid:
        return query_sum(root.left, l, r)
    elif l > mid:
        return query_sum(root.right, l, r)
    else:
        return query_sum(root.left, l, mid) + query_sum(root.right, mid+1, r)

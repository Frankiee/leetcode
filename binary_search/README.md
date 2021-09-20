## Why Binary Search
* Fast
* T(n) = T(n/2) + O(eval)
* O(log(range)) * O(eval)

| Range | Binary | Linear | Speed Up (x) |
| --- | --- | --- | --- |
| 100 | 7 | 100 | 14.29 |
| 10,000 | 14 | 10,000 | 714.29 |
| 1,000,000 | 20 | 1,000,000 | 500,000 |
| 1,000,000,000 | 30 | TLE | N/A |

## Template:
[l, r)

```python
def binary_search(l, r):
    while l < r:
        m = l + (r - l) / 2
        if f(m): return m  # optional
        if g(m):
            r = m          # new range [l, m)
        else:
            l = m + 1      # new range [m+1, r)
    return l   # or not found
```

## Example 
### Example 1:
LC 704: Return the index of an element in a sorted array. Elements are unique. If not found return -1.
A = [1, 2, 5, 7, 8, 12]
search(8) = 4, search(6) = -1

```python
def binary_search(A, val, l, r):
    while l < r:
        m = l + (r - l) / 2
        if A[m] == val:
            return m
        if A[m] > val:
            r = m
        else:
            l = m + 1
    # Not found
    return -1

binary_search(A, 8, 0, len(A))
```

### Example 2:
Return the lower_bound / upper_bound of a val in a sorted array.

lower_bound(x): first index of i, such that A[i] >= x
upper_bound(x): first index of i, such that A[i] > x

A = [1, 2, 2, 2, 4, 4, 5]
lower_bound(A, 2) = 1, lower_bound(A, 3) = 4 (does not exist)
upper_bound(A, 2) = 4, upper_bound(A, 5) = 7 (does not exist)

```python
# tips: m >= r m
def lower_bound(A, val, l, r):
    while l < r:
        m = l + (r - l) / 2
        if A[m] >= val:     # g(m)
            r = m
        else:
            l = m + 1
    return l
```

```python
# tips: m > r m
def upper_bound(A, val, l, r):
    while l < r:
        m = l + (r - l) / 2
        if A[m] > val:     # g(m)
            r = m
        else:
            l = m + 1
    return l
```

### Example 3:
LC 69: sqrt(x)
sqrt(4) = 2
sqrt(8) = 2

```python
# Same as the upper_bound query
def sqrt(x):
    l = 0
    r = x + 1
    
    while l < r:
        m = l + (r - l) / 2
        
        m_square = m ** 2
        
        if m_square == x:
            return m
        if m_square > x:
            r = m
        else:
            l = m + 1
    
    return l - 1
```

### Example 4:
LC 278: First Bad Version

```python
def firstBadVersion(n):
    l = 1
    r = n + 1
    
    while l < r:
        m = l + (r - l) / 2
        
        if isBadVersion(m):
            r = m
        else:
            l = m + 1
    
    return l
```

### Example 5:
LC 875: KoJo Eating Bananas
Find minimum K such that she can eat all the bananas within H hours.

```python
def minEatingSpeed(piles, H):
    """
    :type piles: List[int]
    :type H: int
    :rtype: int
    """
    l = 1
    r = max(piles) + 1

    while l < r:
        m = l + (r - l) / 2

        min_hours = sum([math.ceil(p / float(k)) for p in piles])

        if min_hours <= H:
            r = m
        else:
            l = m + 1

    return l
```


### Example 6:
LC 378: Kth Smallest Element in a Sorted Matrix
Each row and column are sorted.

```python
def kthSmallest(self, matrix, k):
    l = matrix[0][0]
    r = matrix[-1][-1] + 1

    while l < r:
        m = l + (r - l) / 2

        total = 0  # total # of elements <= m
        for row in matrix:
            total += bisect.bisect_right(row, m)

        # Minimal m so that total >= k
        if total >= k:
            r = m
        else:
            l = m + 1

    return l
```

## Reference
* Binary Search
https://www.youtube.com/watch?v=v57lNF2mb_s&t=205s

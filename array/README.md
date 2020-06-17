## Check if two integer ranges for overlap
https://stackoverflow.com/questions/3269434/whats-the-most-efficient-way-to-test-two-integer-ranges-for-overlap/25369187

What does it mean for the ranges to overlap? It means there exists some number C which is in both ranges, i.e.

```
x1 <= C <= x2
```

and

```
y1 <= C <= y2
```

Now, if we are allowed to assume that the ranges are well-formed (so that x1 <= x2 and y1 <= y2) then it is sufficient to test

```
x1 <= y2 && y1 <= x2
```
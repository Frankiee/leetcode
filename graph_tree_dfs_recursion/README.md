https://leetcode.com/explore/learn/card/queue-stack/232/practical-application-stack/1384/

There are two ways to implement DFS. The first one is to do recursion which you might already be familiar with. Here we provide a template as reference:

/*
 * Return true if there is a path from cur to target.
 */
```java
boolean DFS(Node cur, Node target, Set<Node> visited) {
    return true if cur is target;
    for (next : each neighbor of cur) {
        if (next is not in visited) {
            add next to visted;
            return true if DFS(next, target, visited) == true;
        }
    }
    return false;
}
```

## Tree DFS Graph
![Tree DFS Graph](https://github.com/Frankiee/leetcode/blob/master/graph_tree_dfs_recursion/tree_traversal_graph.png)
Credit: [LeetCode 889. Construct Binary Tree from Preorder and Postorder Traversal](https://www.youtube.com/watch?v=53aOi0Drp9I&t=323s)

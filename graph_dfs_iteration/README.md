https://leetcode.com/explore/learn/card/queue-stack/232/practical-application-stack/1385/

The advantage of the recursion solution is that it is easier to implement. However, there is a huge disadvantage: if the depth of recursion is too high, you will suffer from stack overflow. In that case, you might want to use BFS instead or implement DFS using an explicit stack.

Here we provide a template using an explicit stack:

/*
 * Return true if there is a path from cur to target.
 */
```java
boolean DFS(int root, int target) {
    Set<Node> visited;
    Stack<Node> stack;
    add root to stack;
    while (s is not empty) {
        Node cur = the top element in stack;
        remove the cur from the stack;
        return true if cur is target;
        for (Node next : the neighbors of cur) {
            if (next is not in visited) {
                add next to visited;
                add next to stack;
            }
        }
    }
    return false;
}
```

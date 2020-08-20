# 232. 用栈实现队列 python3
# 使用栈实现队列的下列操作：
#
# push(x) – 将一个元素放入队列的尾部。
# pop() – 从队列首部移除元素。
# peek() – 返回队列首部的元素。
# empty() – 返回队列是否为空。
#
# 示例:
# MyQueue queue = new MyQueue();
#
# queue.push(1);
# queue.push(2);
# queue.peek(); // 返回 1
# queue.pop(); // 返回 1
# queue.empty(); // 返回 false
#
# 说明:
#
# 你只能使用标准的栈操作 – 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
#
# 你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
#
# 假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）。

# 98.8%
# 执行用时：28 ms
# 内存消耗：13.6 MB
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.push_stack = []
        self.pop_stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.push_stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.pop_stack:
            return self.pop_stack.pop()
        else:
            while self.push_stack:
                self.pop_stack.append(self.push_stack.pop())
            return self.pop_stack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.pop_stack:
            return self.pop_stack[-1]
        else:
            return self.push_stack[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.push_stack or self.pop_stack:
            return False
        else:
            return True


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
param_3 = obj.peek()
param_2 = obj.pop()
param_4 = obj.empty()
print(param_2)
print(param_3)
print(param_4)
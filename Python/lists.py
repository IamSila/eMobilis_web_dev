from collections import deque

q = deque()
q.append('a')
q.append('b')
q.append('c')
print("Initial queue")
print(q)
print("Elements dequed from the queue")
print(q.popleft())
print(q.popleft())
print(q.popleft())





print(q)
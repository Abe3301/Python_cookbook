#STAR SYNTAX-------------------------------------------------------------------------------------
#any iterable can be unpacked into variables 
p = (4,5)
x, y = p
print(x,y)
data = ['ACME', 50,91.1, (2012, 12,21)]
name, shares, price, date=data
print(name,shares,price, date)
name, shares, prices, (year, mon, day) = data
print(year)
#unpacking strings
s = 'Hello'
a,b,c,d,e = s
print(a,b,c,d,e)
#unpack and discard 
_,shares, price, _ = data
print(data)

#unpack n elements, iterable larger then n solution is star expressions
from statistics import *
def drop_first_last(grades):
    first,  middle, *last = grades
    return mean(middle)

record = ('dave', 'email@email.com', '093248239', '9021812')
name, email, *IDs = record
print(IDs)

#suppose we want how  most recent  quarter stacks up agains average of first 7 
#*trailing_qtrs, current_qtr = sales_record 
#trailing_avg = sum(trailing_qtrs) / len(trailing_qtrs)
*trailing, current = [10,8,7,1,9,5,10,3]
print(trailing)
print(current)

#star syntax best when iterating over a sequence of tuples of varying length 
records = [
        ('foo',1,2),
        ('bar','hello'),
        ('foo',3,4),
        ]
def do_foo(x,y):
    print('foo',x,y)

def do_bar(s):
    print('bar',s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)
#can also be used for splitting
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname, homedir, sh)
#split list to head and tail
items = [1,10,7,4,5,9]
head, *tail = items
print(head)
print(tail)
*head2, tail2 = items
print(head2)
print(tail2)

#heres a clever treat, 
def sum(items):
    head, *tail = items
    ans = head +sum(tail) if tail else head
    print(ans)
    return ans
sum(items)

#collection deque 
from collections import deque
def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in lines:
            yield line, previous_lines
        previous_lines.append(line)

with open('test.txt') as f:
    for line, prevlines in search(f,'test',5):
        for pline in prevlines:
            print(pline, end='')
            print(line, end='')
            print('-'*20)
q = deque(maxlen = 3)
q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)
q = deque()
q.appendleft(5)
q.append(1)
q.append(2)
q.append(3)
print(q)
q.popleft()
print(q)
#heapq smallest and largest
import heapq
nums = [1,3,54,56,324,-2930,-3.0983,32,9834,9,-1,34,564,0.3,-0.4]
print(heapq.nlargest(4, nums))
print(heapq.nsmallest(4,nums))

portfolio = [
        {'name':'IBM','shares':100,'price':91.11},
        {'name':'AAPL','shares':72,'price':981.14},
        {'name':'FB','shares':193,'price':41.71},
        {'name':'HPQ','shares':23,'price':51.31},
        {'name':'YHOO','shares':59,'price':9.5},
        {'name':'ACME','shares':99,'price':243.8}
        ]
cheap = heapq.nsmallest(3,portfolio,key=lambda s: s['price'])
expensive = heapq.nlargest(3,portfolio,key=lambda s: s['price'])
print(cheap)
print(expensive)

heap=list(nums)
heapq.heapify(heap)
print(heap)
heapq.heappop(heap)
heapq.heappop(heap)
print(heap)

#QUEUE
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
    def pop(self):
        return heapq.heappop(self._queue)[-1]
class Item:
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q = PriorityQueue()
q.push(Item('foo'),1)
q.push(Item('bar'),5)
q.push(Item('spam'),4)
q.push(Item('grok'),1)
q.pop()
#this pops bar first with highest priority
a = (1,0,Item('foo'))
b = (5,1,Item('bar'))
c = (1,2,Item('grok'))
print(a)
print(b)
print(c)
x = a < b
y = b > c
z = a < c
print (x,y,z)




























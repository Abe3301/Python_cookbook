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

#Mapping multiple keys to  multi vlaues in a dictionary
d = {
        'a':[1,2,3],
        'b':[4,5]
    }
e = {
        'a':[1,2,3],
        'b':[4,5]
    }
from collections import defaultdict 
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d)
d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
print(d)
#to prevent auto creating entries for keys accessed later 
d = {}
d.setdefault('a',[]).append(1)
#inializing can be simple like
#d = defaultdict(list)
#for key, value in pairs:
#    d[key].append(values)
# order of items in a dict
from collections import OrderedDict
d = OrderedDict()
d['foo'] = 1
d['bar'] = 3
d['spam'] = 4
d['grok'] = 2
for key in d:
    print(key, d[key])
#heres a good use
import json
json.dumps(d)
print(d)

#calculating with dictionaries
prices = {
        'ACME':45.23,
        'AAPL':983.93,
        'IBM':234.99,
        'HPQ':93.4,
        'FB':32.33
        }
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(min_price)
print(max_price)
print(prices_sorted)
#note:zip creates an iterator that can only be used once
print(min(prices, key=lambda k: prices[k]))
print(max(prices,key=lambda k: prices[k]))
min_value = prices[min(prices,key=lambda k: prices[k])]
print(min_value)

#finding commonalities in dicts
a = {
        'x':1,
        'y':2,
        'z':3
        }
b = {
        'w':10,
        'x':11,
        'y':2
        }
common = a.keys() & b.keys()
print(common)
a_notIn_b = a.keys() - b.keys()
common_pairs = a.items() & b.items() 
print(a_notIn_b)
print(common_pairs)
c = {key:a[key] for key in a.keys() - {'z','w'}}
print(c)

#remove duplicates while mainting order
#if items hashable we can do 
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item 
            seen.add(item)
a = [1,4,5,6,6,7,8,8,8,6,5,4,2,4,567,54,90,0,90]
print(list(dedupe(a)))
#for unshashable items such as dicts
def dup_unhashable(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item 
            seen.add(val)
a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
print(list(dup_unhashable(a, key=lambda d: (d['x'],d['y']))))
print(list(dup_unhashable(a, key=lambda d: d['x'])))

#most frequent items in a sequence 
words = [
        'look', 'into' , 'my','eyes', 'look', 'into' , 'my','eyes',
        'the', 'eyes', 'the', 'eyes', 'eyes', 'the', 'not', 'around' 'the',
        'eyes', 'just', 'some', 'more', 'eyes'
        ]
from collections import Counter
word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)
print(word_counts['the'])
more_words = ['even', 'more', 'eyes']
for word in more_words:
    word_counts[word] += 1
word_counts.update(more_words)
a = Counter(words)
b = Counter(more_words)
c = a + b
print(c)

#sorting list of dictionaries by a common key
sql_rows = [
        {'fname':'Brian', 'lname':'Oconner','uid':378924},
        {'fname':'Abraham', 'lname':'Al','uid': 893211},
        {'fname':'Micheal', 'lname':'Scott','uid':90823},
        {'fname':'Alexander', 'lname':'Kirk','uid':834924}
        ]
from operator import itemgetter
rows_by_name = sorted(sql_rows, key=itemgetter('fname'))
rows_by_uid = sorted(sql_rows, key=itemgetter('uid'))
print(rows_by_name)
print(rows_by_uid)
#multiple keys
rows_by_lfname = sorted(sql_rows, key=itemgetter('lname','fname'))
print(rows_by_lfname)
#can use lambda
rows_by_flname = sorted(sql_rows, key=lambda r: (r['lname'],r['fname']))
print(rows_by_lfname)
#can apply min and mix 
mx = max(sql_rows, key=itemgetter('uid'))
print(mx)
# sorting objects without native comparision support
class User:
    def __init__(self,user_id):
        self.user_id = user_id
    def __repr__(self):
        return 'User({})'.format(self.user_id)
users = [User(23), User(3), User(99)]
print(users)
print(sorted(users, key=lambda u: u.user_id))
#alternative to lambda
from operator import attrgetter
print(sorted(users, key=attrgetter('user_id')))
print(max(users, key=attrgetter('user_id')))
#group tecords together based on a field
rows = [
        {'address':'342 N CLARK', 'date': '07/06/2012'},
        {'address':'teN CLARy', 'date': '07/07/2012'},
        {'address':'993 Ute', 'date': '07/09/2012'},
        {'address':'12 millrace', 'date': '07/08/2012'},
        {'address':'9 moon ave', 'date': '07/04/2012'},
        {'address':'1 bloomfield', 'date': '07/03/2012'},
        {'address':'9382 rchale', 'date': '07/05/2012'},
        {'address':'7 crt dr', 'date': '07/09/2012'}
        ]
from itertools import groupby
#have to sort items first
rows.sort(key=itemgetter('date'))
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ', i)
#if we want to group data together into large data structure that allows random acccess
from collections import defaultdict
rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)
    for r in rows_by_date['07/09/2012']:
        print(r)
#using generator expressions to filter sequence elemetns 
mylist = [1,5,3,7,-6,-42,-5,-9,89,-1,83,-91]
#simple way only good for small set
print([n for n in mylist if n > 0])
#better way
pos = (n for n in mylist if n < 0)
for x in pos:
    print(x)
#if we need exc handling and/or list is complex not just nums 
values = ['1','2','-3','-','4','N/A','5']
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False
ivals = list(filter(is_int, values))
print(ivals)
import math
print([math.sqrt(n) for n in mylist if n >= 0])
#instead of just finding we want to replace values
clip_neg = [n if n > 0 else 0 for n in mylist]
print(clip_neg)
#apply results of one filtering to another
addresses = [
        '324 clark',
        '389 nwod',
        '938 mill',
        '930 race',
        '126 arc',
        '9 miller',
        '8 crt',
        '1 moon'
        ]
counts = [0,3,10,4,1,7,6,1]
#make addresses where coresponding count values > 5 
from itertools import compress 
more5 = [n > 5 for n in counts]
print(more5)
print(list(compress(addresses, more5)))

#extracting a subset of a dictionary
#make a dict that is a subset of another dict
prices = {
        'ACME':45.21,
        'AAPL':987.99,
        'GOOG':536.23,
        'HPQ':152.32,
        'FB':23.32
        }
#dict for all prices over 200 
p1 = {key:value for key, value in prices.items() if value > 200}
print(p1)
#make a dict of tech stocks
tech_names = {'AAPL', 'GOOG', 'HPQ', 'MsFT'}
p2 = {key:value for key, value in prices.items() if key in tech_names}
print(p2)

#mapping names to sequence elements
from collections import namedtuple
Subscriber = namedtuple('Subscriber',['addr','joined'])
sub = Subscriber('john@example.com','2020-10-19')
sub
Subscriber(addr='john@example.com', joined='2020-10-19')
print(sub.addr + ' ' + sub.joined)
#we can use a namedtuple instead of dict but its not mutable, cant change values
# to do so we use replace 
Stock = namedtuple('Stock',['name','shares','price'])
s = Stock('ALBA', 9283, 9826.93)
print(s)
# s.shares = 100 will throw error, we use
s = s._replace(shares=10000)
print(s)
#populate named tuples
Stock = namedtuple('Stock',['name', 'shares', 'price', 'date', 'time'])
stock_prototype = Stock('', 0,0.0, None, None)
#convert dict to stack
def dict_to_stack(s):
    return stock_prototype._replace(**s)
a = {'name': 'ALBA', 'shares':'8912', 'price':30789.92}
print(dict_to_stack(a))

#transforming and reducing data at the same time
import os 
files = os.listdir('/var/www/html/')
if any(name.endswith('.py') for name in files):
    print('there is python')
else:
    print('no python here')
#output tuple to csv
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))
#data reduction across fields of a data structure
portfolio = [
        {'name':'GOOG', 'shares':50},
        {'name':'AAPL', 'shares':82},
        {'name':'AOL',  'shares':81},
        {'name':'Tesla','shares':78912}
        ]
min_shares = min(s['shares'] for s in portfolio)
print(min_shares)
print(min(portfolio,key=lambda s: s['shares']))

#combining multiple mappings.dictionaries into a single mapping
a = {'x':1, 'z':3}
b = {'y':2, 'z':4}

from collections import ChainMap
c = ChainMap(a,b)
print(c['x'])
print(c['y'])
print(c['z'])

values = ChainMap()
values['x'] = 1
#add new mapping
values = values.new_child()
values['x'] = 2

values = values.new_child()
values['x'] = 3
print(values)
#discard last mapping
values = values.parents
print(values['x'])

values  = values.parents
print(values['x'])
#alternative to chainmaps 
a = {'x':1, 'z':3}
b = {'y':2, 'z':4}

merged = dict(b)
merged.update(a)
print(merged['x'])
print(merged['y'])
print(merged['z'])

a['x'] = 13 
print(merged['x'])

merged = ChainMap(a,b)
print(merged['x'])
a['x'] = 42
print(merged['x'])













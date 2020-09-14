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


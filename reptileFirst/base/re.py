#coding=utf-8
import re

'''
返回pattern对象
re.compile(string[,flag])
#以下为匹配所用函数
re.match(pattern, string[, flags])
re.search(pattern, string[, flags])
re.split(pattern, string[, maxsplit])
re.findall(pattern, string[, flags])
re.finditer(pattern, string[, flags])
re.sub(pattern, repl, string[, count])
re.subn(pattern, repl, string[, count])
'''

# pattern可以理解为一个匹配模式，那么我们怎么获得这个匹配模式呢？很简单，我们需要利用re.compile方法就可以
pattern = re.compile('hello')

'''
另外大家可能注意到了另一个参数 flags，在这里解释一下这个参数的含义：
参数flag是匹配模式，取值可以使用按位或运算符’|’表示同时生效，比如re.I | re.M。

 • re.I(全拼：IGNORECASE): 忽略大小写（括号内是完整写法，下同）
 • re.M(全拼：MULTILINE): 多行模式，改变'^'和'$'的行为（参见上图）
 • re.S(全拼：DOTALL): 点任意匹配模式，改变'.'的行为
 • re.L(全拼：LOCALE): 使预定字符类 \w \W \b \B \s \S 取决于当前区域设定
 • re.U(全拼：UNICODE): 使预定字符类 \w \W \b \B \s \S \d \D 取决于unicode定义的字符属性
 • re.X(全拼：VERBOSE): 详细模式。这个模式下正则表达式可以是多行，忽略空白字符，并可以加入注释。

'''

# 使用re.match匹配文本，获得匹配结果，无法匹配时将返回None
result1 = re.match(pattern, 'hello')
result2 = re.match(pattern, 'helloo CQC!')
result3 = re.match(pattern, 'helo CQC!')
result4 = re.match(pattern, 'hello CQC!')

# 如果1匹配成功
if result1:
    # 使用Match获取分组信息
    print result1.group()
else:
    print '1匹配失败!'

# 如果2匹配成功
if result2:
    # 使用Match获取分组信息
    print result2.group()
else:
    print '2匹配失败!'

# 如果3匹配成功
if result3:
    # 使用Match获取分组信息
    print result3.group()
else:
    print '3匹配失败!'

# 如果4匹配成功
if result4:
    # 使用Match获取分组信息
    print result4.group()
else:
    print '4匹配失败!'

'''
属性：
1.string: 匹配时使用的文本。
2.re: 匹配时使用的Pattern对象。
3.pos: 文本中正则表达式开始搜索的索引。值与Pattern.match()和Pattern.seach()方法的同名参数相同。
4.endpos: 文本中正则表达式结束搜索的索引。值与Pattern.match()和Pattern.seach()方法的同名参数相同。
5.lastindex: 最后一个被捕获的分组在文本中的索引。如果没有被捕获的分组，将为None。
6.lastgroup: 最后一个被捕获的分组的别名。如果这个分组没有别名或者没有被捕获的分组，将为None。


方法：
1.group([group1, …]):
获得一个或多个分组截获的字符串；指定多个参数时将以元组形式返回。group1可以使用编号也可以使用别名；编号0代表整个匹配的子串；不填写参数时，返回group(0)；没有截获字符串的组返回None；截获了多次的组返回最后一次截获的子串。
2.groups([default]):
以元组形式返回全部分组截获的字符串。相当于调用group(1,2,…last)。default表示没有截获字符串的组以这个值替代，默认为None。
3.groupdict([default]):
返回以有别名的组的别名为键、以该组截获的子串为值的字典，没有别名的组不包含在内。default含义同上。
4.start([group]):
返回指定的组截获的子串在string中的起始索引（子串第一个字符的索引）。group默认值为0。
5.end([group]):
返回指定的组截获的子串在string中的结束索引（子串最后一个字符的索引+1）。group默认值为0。
6.span([group]):
返回(start(group), end(group))。
7.expand(template):
将匹配到的分组代入template中然后返回。template中可以使用\id或\g、\g引用分组，但不能使用编号0。\id与\g是等价的；但\10将被认为是第10个分组，如果你想表达\1之后是字符’0’，只能使用\g0。
'''
print '----------------------'
# 匹配如下内容：单词+空格+单词+任意字符
m = re.match('(\w+) (\w+)(?P<sign>.*)', 'hello world!')

print "m.string:", m.string
print "m.re:", m.re
print "m.pos:", m.pos
print "m.endpos:", m.endpos
print "m.lastindex:", m.lastindex
print "m.lastgroup:", m.lastgroup
print "m.group():", m.group()
print "m.group(1,2):", m.group(1, 2)
print "m.groups():", m.groups()
print "m.groupdict():", m.groupdict()
print "m.start(2):", m.start(2)
print "m.end(2):", m.end(2)
print "m.span(2):", m.span(2)
print r"m.expand(r'\g \g\g'):", m.expand(r'\2 \1\3')

print '----------------------'
'''
re.search(pattern, string[, flags])

search方法与match方法极其类似，区别在于match()函数只检测re是不是在string的开始位置匹配，
search()会扫描整个string查找匹配，match（）只有在0位置匹配成功的话才有返回，
如果不是开始位置匹配成功的话，match()就返回None。
同样，search方法的返回对象同样match()返回对象的方法和属性。
'''
# 将正则表达式编译成Pattern对象
pattern = re.compile(r'world')
# 使用search()查找匹配的子串，不存在能匹配的子串时将返回None
# 这个例子中使用match()无法成功匹配
match = re.search(pattern, 'hello world!')
if match:
    # 使用Match获得分组信息
    print match.group()


print '----------------------'
'''
re.split(pattern, string[, maxsplit])

按照能够匹配的子串将string分割后返回列表。
maxsplit用于指定最大分割次数，不指定将全部分割。
'''
pattern = re.compile('\d+')
print re.split(pattern, 'one1two2three3four4')

print '----------------------'
'''
re.findall(pattern, string[, flags])
搜索string，以列表形式返回全部能匹配的子串。
'''
pattern = re.compile(r'\d+')
print re.findall(pattern,'one1two2three3four4')

print '----------------------'
'''
e.finditer(pattern, string[, flags])

搜索string，返回一个顺序访问每一个匹配结果（Match对象）的迭代器。
'''

pattern = re.compile(r'\d+')
for m in re.finditer(pattern,'one1two2three3four4'):
    print m.group()

print '----------------------'
'''
re.sub(pattern, repl, string[, count])

使用repl替换string中每一个匹配的子串后返回替换后的字符串。
当repl是一个字符串时，可以使用\id或\g、\g引用分组，但不能使用编号0。
当repl是一个方法时，这个方法应当只接受一个参数（Match对象），
并返回一个字符串用于替换（返回的字符串中不能再引用分组）。
count用于指定最多替换次数，不指定时全部替换。
'''
pattern = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!'

print re.sub(pattern, r'\2 \1', s)

def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()

print re.sub(pattern, func, s)

print '----------------------'
'''
re.subn(pattern, repl, string[, count])

返回 (sub(repl, string[, count]), 替换次数)

'''
pattern = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!'

print re.subn(pattern,r'\2 \1', s)

def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()

print re.subn(pattern,func, s)
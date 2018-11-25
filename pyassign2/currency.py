def a(i):
    #对于一个字符串，首先根据','进行分割，得到一个列表。取这个列表中的[1]位字符串，再根据':'进行分割，得到一个列表。
    #取这个列表中的[1]位字符串，把其中的'"'替换成''，然后去掉''。
    z=i.split(',')[1].split(':')[1].replace('"','').strip()
    return z



def test_a():
    #测试a函数是否正确
    assert('2.24075 Euros' == a('{ "from" : "2.5 United States Dollars", "to" : "2.24075 Euros", "success" : true, "error" : "" }'))
    assert('' == a('{ "from" : "", "to" : "", "success" : false, "error" : "Source currency code is invalid." }'))

    
    
def b(i):
    #对于一个字符串，去掉''，得到一个列表。取这个列表的[0]位字符串。
    y=i.split()[0]
    return y



def test_b():
    #测试b函数是否正确
    assert('2.1589225' == b('2.1589225 Euros'))           

    
    
def exchange(currency_from,currency_to,amount_from):
    #实参有三个：currency_from,currency_to,amount_from。
    #该函数可以根据amount_from的数值实现由currency_from向currency_to的转换计算，并得到计算值（浮点数类型）。
    #当输入的三个参数不正确时，会输出相应指示。
    url='http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=' + currency_from + '&to=' + currency_to + '&amt=' + str(amount_from)    
    from urllib.request import urlopen
    doc = urlopen(url)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')    
    if a(jstr) == '':
        error_name=jstr.split(':')[-1].split()[0].replace('"','')
        if error_name == 'Source':
            return '请输入正确的初始货币符号'
        elif error_name == 'Exchange':
            return '请输入正确的目标货币符号'
        elif error_name == 'Currency':
            return '请输入正确的数值'
    else:
        x = float(b(a(jstr)))
        return x   

    
    
def test_exchange():
    #测试exchange函数是否正确
    assert(2.1589225 == exchange('USD','EUR',2.5))
    assert('请输入正确的初始货币符号' == exchange('XXX','EUR',2.5))
    assert('请输入正确的目标货币符号' == exchange('USD','XXX',2.5))
    assert('请输入正确的数值' == exchange('USD','EUR','XXX'))

    
    
def testAll():
    #如果a函数,b函数和exchange函数都正确，则输出All tests passed
    test_a()
    test_b()
    test_exchange()
    print('All tests passed')
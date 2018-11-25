def a(i):
    #����һ���ַ��������ȸ���','���зָ�õ�һ���б�ȡ����б��е�[1]λ�ַ������ٸ���':'���зָ�õ�һ���б�
    #ȡ����б��е�[1]λ�ַ����������е�'"'�滻��''��Ȼ��ȥ��''��
    z=i.split(',')[1].split(':')[1].replace('"','').strip()
    return z



def test_a():
    #����a�����Ƿ���ȷ
    assert('2.24075 Euros' == a('{ "from" : "2.5 United States Dollars", "to" : "2.24075 Euros", "success" : true, "error" : "" }'))
    assert('' == a('{ "from" : "", "to" : "", "success" : false, "error" : "Source currency code is invalid." }'))

    
    
def b(i):
    #����һ���ַ�����ȥ��''���õ�һ���б�ȡ����б��[0]λ�ַ�����
    y=i.split()[0]
    return y



def test_b():
    #����b�����Ƿ���ȷ
    assert('2.1589225' == b('2.1589225 Euros'))           

    
    
def exchange(currency_from,currency_to,amount_from):
    #ʵ����������currency_from,currency_to,amount_from��
    #�ú������Ը���amount_from����ֵʵ����currency_from��currency_to��ת�����㣬���õ�����ֵ�����������ͣ���
    #�������������������ȷʱ���������Ӧָʾ��
    url='http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=' + currency_from + '&to=' + currency_to + '&amt=' + str(amount_from)    
    from urllib.request import urlopen
    doc = urlopen(url)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')    
    if a(jstr) == '':
        error_name=jstr.split(':')[-1].split()[0].replace('"','')
        if error_name == 'Source':
            return '��������ȷ�ĳ�ʼ���ҷ���'
        elif error_name == 'Exchange':
            return '��������ȷ��Ŀ����ҷ���'
        elif error_name == 'Currency':
            return '��������ȷ����ֵ'
    else:
        x = float(b(a(jstr)))
        return x   

    
    
def test_exchange():
    #����exchange�����Ƿ���ȷ
    assert(2.1589225 == exchange('USD','EUR',2.5))
    assert('��������ȷ�ĳ�ʼ���ҷ���' == exchange('XXX','EUR',2.5))
    assert('��������ȷ��Ŀ����ҷ���' == exchange('USD','XXX',2.5))
    assert('��������ȷ����ֵ' == exchange('USD','EUR','XXX'))

    
    
def testAll():
    #���a����,b������exchange��������ȷ�������All tests passed
    test_a()
    test_b()
    test_exchange()
    print('All tests passed')
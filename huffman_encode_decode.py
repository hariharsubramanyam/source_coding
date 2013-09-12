def encode(codeBook, msg):
    """
    arguments:
    codeBook -- list of 0/1 strings (e.g. the output of PS11mycode.huffman)
    msg      -- list of integers between 0 and len(codeBook)
    
    returns: 0/1 string
    """
    res = ""
    for i in msg:
        res += codeBook[i]
    return res

def decode(codeBook, msg):
    """
    arguments:
    codeBook -- list of 0/1 strings, prefix-free (e.g. from PS11mycode.huffman)
    msg      -- encoded message (a 0/1 string)
    
    returns: list of integers between 0 and len(codeBook)
    """
    tmp = msg[:]
    res = []
    while len(tmp) > 0:
        for i in xrange(0,len(codeBook)):
            if tmp.find(codeBook[i]) == 0:
                tmp = tmp[len(codeBook[i]):]
                res.append(i)
    return res

def compress(msg_in, maxInput, tableSize):
    """
    arguments:
    maxInput       -- a positive integer
    msg_i          -- a list of integers from range(maxInput)
    tableSize      -- an integer greater than maxInput
    
    outputs: a list of integers from range(tableSize)
    """
    def resetTable(maxInput):
        tbl = {}
        for i in xrange(0,maxInput):
            tbl[(i,)] = i
        return tbl
    msg = msg_in[:]
    output = []
    table = resetTable(maxInput)
    string = [msg.pop(0)]
    while len(msg) > 0:
        symbol = msg.pop(0)
        if tuple(string + [symbol]) in table.keys():
            string += [symbol]
        else:
            output += (table[tuple(string)],)
            if len(table) >= tableSize:
                table = resetTable(maxInput)
            table[tuple(string + [symbol])] = len(table)
            string = [symbol]
    output += (table[tuple(string)],)
    return output


def uncompress(compressed_msg_in, maxInput, tableSize):
    """
    arguments:
    maxInput       -- a positive integer
    tableSize      -- an integer greater than maxInput
    compressed_msg_in        -- a list of integers from range(tableSize)

    outputs: a list of integers from range(maxInput)
    """
    compressed_msg = compressed_msg_in[:]
    def resetTable(maxInput):
        tbl = {}
        for i in xrange(0,maxInput):
            tbl[i] = (i,)
        return tbl
    table = resetTable(maxInput)
    code = compressed_msg.pop(0)
    string = list(table[code])
    output = string[:]
    while len(compressed_msg) > 0:
        code = compressed_msg.pop(0)
        if len(table) >= tableSize:
            table = resetTable(maxInput)
        if not(code in table.keys()):
            entry = string[:] + [string[0]]
        else:
            entry = table[code]
        output += entry
        table[len(table)] = tuple(string + [entry[0]])
        string = list(entry)
    return output
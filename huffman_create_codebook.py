
def huffman(pList):
    """
    argument: pList -- numpy.array of probabilities
    return: (codeBook, codeLength)
       codeBook   -- a Huffman code: codeBook[k] encodes the symbol
                     with probability pList[k]
    codeLength -- code length for the codeBook
    """
    codeBook = []
    class Node:
        def __init__(self, prob, left=None, right=None, code=None, index=None):
            self.prob = prob
            self.left = left
            self.right = right
            self.code = code
            self.index = index
        def __str__(self):
            res = ""
            for prop, val in vars(self).iteritems():
                res += prop + ": " + str(val) + ", "
            return res
        def __eq__(self, other):
            if other == None:
                return False 
            return self.__dict__ == other.__dict__
    def aggregate(nodes):
        a = Node(1)
        b = Node(1)
        aInd = -1
        bInd = -1
        for x in xrange(0,len(nodes)):
            node = nodes[x]
            if node.prob <= a.prob:
                b = Node(prob=a.prob, left=a.left, right=a.right, code=a.code,
                        index=a.index)
                bInd = aInd
                a = Node(prob=node.prob, left=node.left, right=node.right,
                        code=node.code, index=node.index)
                aInd = x
            elif node.prob <= b.prob:
                b = Node(prob=node.prob, left=node.left, right=node.right,
                        code=node.code, index=node.index)
                bInd = x
        nodes = [nodes[x] for x in xrange(0,len(nodes)) if not(x == aInd or x ==
            bInd)]
        print len(nodes)
        combinedNode = Node(prob=a.prob+b.prob, left=a, right=b)
        nodes.append(combinedNode) 
        return nodes
    def buildCodebook(node, currentCode):
        if node.left == None or node.right == None:
            codeBook.append(Node(prob=node.prob, code=currentCode,
                index=node.index))
        else:
            buildCodebook(node.left, currentCode + "1")
            buildCodebook(node.right, currentCode + "0")
    def findCodeLength(nodes):
        codeLength = 0.0
        for node in nodes:
            codeLength += len(node.code)*node.prob
        return codeLength
    remainingElements = [Node(prob=pList[x],index=x) for x in
            xrange(0,len(pList))]
    
    while len(remainingElements) > 1:
        remainingElements = aggregate(remainingElements)

    buildCodebook(remainingElements[0], "")
    codeBook.sort(key=lambda x: x.index)
    return ([x.code for x in codeBook], findCodeLength(codeBook))

if __name__ == "__main__":
    import sys
    import numpy
    import PS1bin
    if len(sys.argv)>1:
        pList = numpy.array(eval(sys.argv[1]))
    else:
        pList = PS1bin.get_dist(5)
    print 'pList = ', pList
    (codeBook, codeLength) = huffman(pList)
    print 'codeLength = ', codeLength
    print 'codeBook:'
    for x in codeBook:
        print x

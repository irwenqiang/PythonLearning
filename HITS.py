# ref:http://en.wikipedia.org/wiki/HITS_algorithm
def genTranspose(linkmatrix=[[]]):
    size=len(linkmatrix)
    TransposeMatrix=[[][:] for i in xrange(size)]
    
    rowid=0
    while rowid<size :
        for col in linkmatrix[rowid]:
            TransposeMatrix[col].append(rowid)
        rowid+=1
    return TransposeMatrix
            
def HITS(linkmatrix=[[]],iterstep=8):
    """linkmatrix must in dense representation like: [[0,1],[],[1,2]]."""
    size=len(linkmatrix)
    result=[[1]*2 for i in range(size)]#auth and hub

    TransposeMatrix=genTranspose(linkmatrix)

    for x in xrange(iterstep):
        tempau=[ah[0] for ah in result]
        i=0
        while i<size:   #each page update all authority
            for incomingNeighbour in TransposeMatrix[i]:
                result[i][0]+=result[incomingNeighbour][1]
            i+=1
            
        i=0
        while i<size:
            for outgoingNeighbour in linkmatrix[i]:
                result[i][1]+=result[outgoingNeighbour][0]
            i+=1
        i=0
        hubsum=sum([ah[1] for ah in result])
        authsum=sum([ah[0] for ah in result])
        while i<size:
            result[i][0]=float(result[i][0])/authsum
            result[i][1]=float(result[i][1])/hubsum
            i+=1
        for i in result:
            print i
    return result
if __name__ == "__main__":

    r=HITS(linkmatrix=[[1,2,4,6],[0],[0,1],[],[0,2,5],[0,4],[4]])
    for i in r:
        print i

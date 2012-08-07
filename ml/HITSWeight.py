def transpose(network):
    Size=len(network)
    
    TransposeMatrix=[[][:] for i in xrange(Size)]
    
    ii=0
    while ii<Size:
        for outlink in network[ii]:
            TransposeMatrix[outlink[0]].append((ii,outlink[1]))
        ii+=1
    
    return TransposeMatrix
def HITS(linkmatrix=[[]],iterstep=8):
    
    size=len(linkmatrix)
    result=[[1]*2 for i in range(size)]#init auth and hub to 1
    
    TransposeMatrix=transpose(linkmatrix)#generate transpose matrix
    
    for x in xrange(iterstep):
    
        i=0
        while i<size:   #each page update all authority
            for incomingNeighbour in TransposeMatrix[i]:
                result[i][0]+=result[incomingNeighbour[0]][1]*incomingNeighbour[1]
            i+=1
            
        i=0
        while i<size:
            for outgoingNeighbour in linkmatrix[i]:
                result[i][1]+=result[outgoingNeighbour[0]][0]*outgoingNeighbour[1]
            i+=1
        i=0
        hubsum=sum([ah[1] for ah in result])
        authsum=sum([ah[0] for ah in result])
        while i<size:
            result[i][0]=float(result[i][0])/authsum
            result[i][1]=float(result[i][1])/hubsum
            i+=1
    
    return result
    
if __name__ == "__main__":
    r=HITS(linkmatrix=[[(1,0.7),(2,0.7),(4,0.9),(6,1)],[(0,1)],[(0,0.8),(3,1)],[],[(0,0.5),(2,1),(5,1)],[(0,1),(4,1)],[(4,1)]])
    for i in r:
        print i

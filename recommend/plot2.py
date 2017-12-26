#!/usr/bin/python
#
# Created by Albert Au Yeung (2010)
#
# An implementation of matrix factorization
#
try:
    import numpy
except:
    print ("This implementation requires the numpy module.")
    exit(0)

###############################################################################

"""
@INPUT:
    R     : a matrix to be factorized, dimension N x M
    P     : an initial matrix of dimension N x K
    Q     : an initial matrix of dimension M x K
    K     : the number of latent features
    steps : the maximum number of steps to perform the optimisation
    alpha : the learning rate
    beta  : the regularization parameter
@OUTPUT:
    the final matrices P and Q
"""
def matrix_factorization(R, P, Q, K, steps=5000, alpha=0.02, beta=0.02):
    Q = Q.T
    for step in range(steps):
        for i in range(len(R)):
            for j in range(len(R[i])):
                if R[i][j] > 0:
                    eij = R[i][j] - numpy.dot(P[i,:],Q[:,j])
                    for k in range(K):
                        P[i][k] = P[i][k] + alpha * (2 * eij * Q[k][j] - beta * P[i][k])
                        Q[k][j] = Q[k][j] + alpha * (2 * eij * P[i][k] - beta * Q[k][j])
                        #P[i][k] = (P[i][k] + alpha * (2 * eij * Q[k][j]))
                        #Q[k][j] = (Q[k][j] + alpha * (2 * eij * P[i][k]))
        eR = numpy.dot(P,Q)
        e = 0
        for i in range(len(R)):
            for j in range(len(R[i])):
                if R[i][j] > 0:
                    e = e + (pow(R[i][j] - numpy.dot(P[i,:],Q[:,j]), 2))
                    for k in range(K):
                        e = e + (beta/2) * ( pow(P[i][k],2) + pow(Q[k][j],2) )
        print(e)
        if e < 0.001:
            break
        f = open('result.txt', 'w')
        a=numpy.dot(P, Q)
        for i in range(0,20):
            for j in range(0,1682):
                f.write(str(a[i][j])+'\t')
            f.write('\n')
        #f.write(str(numpy.dot(P, Q)))  # python will convert \n to os.linesep
        f.close()
        print(1)


    return P, Q.T

###############################################################################

if __name__ == "__main__":
    """R = [
         [5,3,0,1],
         [4,0,0,1],
         [1,1,0,5],
         [1,0,0,4],
         [0,1,5,4],
        ]"""

    R = []
    for i in range(0, 20):
        R.append([])
        for j in range(0, 1682):
            R[i].append(0)

    file = open("C:/Users/hp/Desktop/ItemRecommender/train1.txt", "r")

    for line in file:
        x = line.split('\t')
        if int(x[0]) - 1==20:
            break
        R[int(x[0]) - 1][int(x[1]) - 1] = int(x[2])

    """f = open('d.txt', 'w')
    for i in range(0, 943):
        for j in range(0, 1682):
            f.write(str(R[i][j]) + '\t')
        f.write("\n")
    f.close()"""

    R = numpy.array(R)

    N = len(R)
    M = len(R[0])
    K = 10

    P = numpy.random.rand(N,K)
    #P = numpy.array(P, dtype='int64')
    Q = numpy.random.rand(M,K)
    #Q = numpy.array(Q, dtype='int64')
    #print(P)
    #print(Q)
    nP, nQ = matrix_factorization(R, P, Q, K)
    #print(nP)
    #print(nQ)

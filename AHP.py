class AHP:
    def __init__(self, criFile, degFile):
        self.compMat = [[(0, 0, 0) for i in range(7)] for j in range(7)]
        for i in range(7):
            for j in range(7):
                if i == j:
                    self.compMat[i][j] = (1, 1, 1)

        with open(inputf, 'r') as f:
            self.criList = f.readlines()
        self.criCount = len(self.criList)
        
        with open(degFile, 'r') as f:
            self.degList = f.readlines()
        self.degCount = len(self.degList)
    
    def getTFN(n):
        if (n == 1):
            return (1, 1, 1)
        elif (n == self.degCount):
            return (self.degCount, self.degCount, self.degCount)
        else:
            return (n - 1, n, n + 1)

    def invTFN(n):
        if n == 1:
            return (1, 1, 1)
        elif n == self.degCount:
            return (1/self.degCount, 1/self.degCount, 1/self.degCount)
        else:
            return (1/(n + 1), 1/n, 1/(n - 1))

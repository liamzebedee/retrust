class ListToMatrixIndexMapper:
    def __init__(self, l):
        self.l = l
        self.idxs = list(map(lambda x: x[0], l))
    
    def __call__(self, id):
        # remap user id's to indices for use in matrix
        return self.idxs.index(id)
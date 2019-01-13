import itertools

def id_generator():
    id = 0
    while(True):
        yield str(id)
        id += 1

class NodeIdGenerator():
	def __init__(self):
		self.gen = id_generator()
	
	def __call__(self, amt):
		if amt == 1:
			return next(self.gen)
		else:
			return list(itertools.islice(self.gen, 10))
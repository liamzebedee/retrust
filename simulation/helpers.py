def id_generator():
    id = 0
    while(True):
        yield str(id)
        id += 1


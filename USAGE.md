Usage
=====

Trust networks are stored in networks/*.dot in the Graphdot format.

python gen.py:
    serve a webserver on localhost:3000
    watch for changes to networks/*.dot
    for f of networks/*.dot:
        parse dot into (nodes,edges)
        render_dot(f) -> networks/{id}/structure.jpg
        build trust graph
        render_trust(f) -> networks/{id}/trust.jpg
    


```
```
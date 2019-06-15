C: constant(decimal) = 2.

b: constant(int128) = 0
d: constant(int128) = 1
u: constant(int128) = 2


@public
def opinion_add(x: decimal[3], y: decimal[3]) -> decimal[3]:
    z: decimal[3]
    divisor: decimal = (x[u] + y[u]) - (x[u] * y[u])
    z[b] = ( x[u] * y[b]  +  y[u] * x[b] ) / divisor
    z[d] = ( x[u] * y[d]  +  y[u] * x[d] ) / divisor
    z[u] = x[u] * y[u] / divisor
    return z

@public
def opinion_scalar_mult(a: decimal, x: decimal[3]) -> decimal[3]:
    # z: decimal[3]
    divisor: decimal = a * (x[b] + x[d]) + x[u]
    return [x[b]*a / divisor, x[d]*a / divisor, x[u] / divisor]

# g(x) in paper
@public
def evidence_transfer_scalar(x: decimal[3]) -> decimal:
    return sqrt(x[b])

@public 
def opinion_generic_discount(x: decimal[3], y: decimal[3]) -> decimal[3]:
    return self.opinion_scalar_mult(
        self.evidence_transfer_scalar(x), 
        y
    )

@public
def to_opinion(x: int128) -> decimal[3]:
    x_: decimal = convert(x, decimal)
    if x >= 0:
        return [ 
            x_ / (x_ + C),
            0., 
            C / (x_ + C),
        ]
    else:
        return [ 
            0., 
            x_ / (x_ + C),
            C / (x_ + C),
        ]


xtol: constant(decimal) = 0.001

# Checks whether two decimal values differ by less than xtol
# (the x tolerance)
@public
def check_xtol(a1: decimal, a2: decimal) -> bool:
    z: decimal = a1 / a2
    if z < 1.:
        return (1. - z) < xtol
    else:
        return (z - 1.) < xtol

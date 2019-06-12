pragma solidity ^0.5.6;

pragma experimental ABIEncoderV2;

import "ds-math/math.sol";

contract EBSL is DSMath {

    // using DSMath for uint64;
    // using DSMath for uint256;

    uint64 constant C = 2;
    uint constant b = 0;
    uint constant d = 1;
    uint constant u = 2;
    
    function to_evidence(
        uint64[3] memory x
    )
        public pure
        returns (uint64 pos, uint64 neg)
    {
        pos = C * (x[0] / x[2]);
        neg = C * (x[1] / x[2]);
        return (pos, neg);
    }

    function to_opinion(
        uint64[2] memory e
    )
        public pure
        returns (uint[3] memory x)
    {
        uint sum = e[0] + e[1] + C;

        x[0] = wdiv(e[0], sum);
        x[1] = wdiv(e[1], sum);
        x[2] = wdiv(C, sum);
    
        return x;
    }

    function opinion_add(
        uint[3] memory x,
        uint[3] memory y
    )
        public pure
        returns (uint[3] memory z)
    {
        //     divisor =       (x_u + y_u)  -  (x_u * y_u)
        uint divisor = sub(add(x[u], y[u]), wmul(x[u], y[u]));

        //     (x_b, x_d, x_u) = x
        //     (y_b, y_d, y_u) = y
        
        //     b = ( x_u * y_b  +  y_u * x_b ) / divisor
        z[b] = wdiv( 
            add( 
                wmul(x[u], y[b]),  
                wmul(y[u], x[b]) 
            ),
            divisor
        ); 
        //     d = ( x_u * y_d  +  y_u * x_d ) / divisor
        z[d] = wdiv( 
            add( 
                wmul(x[u], y[d]),  
                wmul(y[u], x[d]) 
            ),
            divisor
        ); 
        //     u = x_u * y_u / divisor
        z[u] = wdiv(
            wmul(x[u], y[u]),
            divisor
        );

        return z;
    }

    function opinion_scalar_mult(uint a, uint[3] memory x) public pure returns (uint[3] memory z) {
        // # Scalar mult basically multiplies against (b,d)
        // # And then normalises.
        // (b, d, u) = x
        // divisor = a * (b + d) + u
        uint divisor = add(
            wmul(
                a,
                add(x[b], x[d])
            ),
            x[u]
        );
        // return opinion(b*a / divisor, d*a / divisor, u / divisor)
        z[b] = wdiv(wmul(x[b], a), divisor);
        z[d] = wdiv(wmul(x[d], a), divisor);
        z[u] = wdiv(x[u], divisor);
        return z;
    }

    function ebsl_F(
        uint64[][][] memory m
    ) public {
        for(uint i = 0; i < m.length; i++) {
            for(uint j = 0; j < m[0].length; j++) {

            }
        }
    }

    function ebslConverge(
        uint64[][][] memory m
    )
        public
    {
        // find the fixed point of the matrix
        // or prove it?
        
        // 1e-3
        uint xtol = 1 * 10^3;
    }
}

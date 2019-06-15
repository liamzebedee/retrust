pragma solidity ^0.5.6;

pragma experimental ABIEncoderV2;


import "./EBSLCore.sol";
import "./TrustToken.sol";

contract EBSL {

    uint64 constant C = 2;
    uint constant b = 0;
    uint constant d = 1;
    uint constant u = 2;

    uint constant xtol = 1 * 10^3;

    TrustToken trust;

    uint168[3][][] opinionsMatrix;

    using EBSLCore for uint168;

    constructor(
        address _trustToken
    ) public {
        trust = TrustToken(_trustToken);
    }

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

    function buildMatrix() internal returns (uint168[3][][] memory matrix) {
        // go through every account in the system
        // set their address?
        // or maybe we can just store the matrix here

        // for all users
        // convert their tokens into evidence
        // build matrix


        // First get users
        address[] memory users = new address[](trust.getUserCount());

        for(uint i = 0; i < users.length; i++) {
            users[i] = (trust.getUser(i));
        }

        matrix = new uint168[3][][](3);

        // Now fill matrix
        for(uint i = 0; i < users.length; i++) {
            for(uint j = 0; j < users.length; j++) {
                matrix[i][j] = EBSLCore.to_opinion(
                    trust.getTrust(users[i], users[j])
                );
            }
        }

        return matrix;
    }


    function ebsl_F(
        uint168[3][][] memory m
    )
        public
        returns (uint168[3][][] memory)
    {
        uint n = m.length;

        for(uint i = 0; i < n; i++) {
            for(uint j = 0; j < n; j++) {
                uint168[3] memory opinion = m[i][j];

                for(uint k = 0; k < n; k++) {
                    opinion = EBSLCore.opinion_add(
                        opinion,
                        EBSLCore.opinion_generic_discount(
                            m[i][k],
                            m[k][j]
                        )
                    );
                }

                m[i][j] = opinion;
            }
        }

        return m;
    }

    function verifyEbslProof(
        uint168[3][][] memory m
    )
        public
        returns (uint168[3][][] memory)
    {
        uint168[3][][] memory m_prime = ebsl_F(buildMatrix());
        
        // now compare difference
        uint n = m.length;
        for(uint i = 0; i < n; i++) {
            for(uint j = 0; j < n; j++) {
                for(uint k = 0; k < 3; k++) {
                    require(
                        EBSLCore.check_xtol(m[i][j][k], m_prime[i][j][k]),
                        "xtol not valid"
                    );
                }
            }
        }
    }

    function ebslConverge()
        public
        returns (uint168[3][][] memory)
    {
        uint168[3][][] memory m = buildMatrix();
        uint n = m.length;

        while(true) {
            uint168[3][][] memory m_prime = ebsl_F(m);

            bool converged = true;
            for(uint i = 0; i < n; i++) {
                for(uint j = 0; j < n; j++) {
                    for(uint k = 0; k < 3; k++) {
                        converged = converged && EBSLCore.check_xtol(m[i][j][k], m_prime[i][j][k]);
                    }
                }
            }

            if(converged) break;
            else {
                m = m_prime;
            }
        }

        return m;
    }

    function ebslConverge2(
    )
        public
    {
        opinionsMatrix = ebslConverge();
    }

    function getOpinion(address from, address of_) external view returns (uint168[3] memory) {
        return opinionsMatrix[trust.getUserIdx(from)][trust.getUserIdx(of_)];
    }
}

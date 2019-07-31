pragma solidity ^0.5.6;

import "ds-test/test.sol";

import "./GUACToken.sol";
import "./MemberNFT.sol";

contract TestMemberNFT is DSTest {
    GUACToken guac;

    function setUp() public {
        guac = new GUACToken();
    }
    
    function testJoin() public {
        MemberNFT members = new MemberNFT(address(guac));
        guac.setup(address(members));
        uint memberId = members.join.value(members.getMinimumDeposit())("camus");
        
        assert(guac.balanceOf(address(memberId)) == members.getInitialReputation());
        assert(members.ownerOf(memberId) == address(this));
    }
}
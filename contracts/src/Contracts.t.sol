pragma solidity ^0.5.6;

import "ds-test/test.sol";

import "./Contracts.sol";

contract ContractsTest is DSTest {
    Contracts contracts;

    function setUp() public {
        contracts = new Contracts();
    }

    function testFail_basic_sanity() public {
        assertTrue(false);
    }

    function test_basic_sanity() public {
        assertTrue(true);
    }
}

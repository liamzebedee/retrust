// import "./lib/ERC20.sol";
import "./GUACToken.sol";
import "./lib/SafeMath.sol";

// A TCR-style entry and exit system
// uses ETH, but can easily use DAI 
contract EntryExit {
    using SafeMath for uint256;

    uint coopReserve = 0;

    uint depositAmt = 0.05 ether;

    // 3%
    uint coopFee = 30;
    uint coopFeeDivisor = 1000;

    constructor() public {

    }

    function enter() internal returns (bool) {
        require(msg.value == depositAmt, "exact deposit not received");
        uint feeAmt = msg.value.mul(coopFee).div(coopFeeDivisor);
        coopReserve += feeAmt;
        return true;
    }

    function exit(address payable account, uint share) internal returns (bool) {
        // based on the total supply
        // gives you a share of the funds here
        uint refundAmt = address(this).balance.mul(share);
        account.transfer(refundAmt);
        return true;
    }
}
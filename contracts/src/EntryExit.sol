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

    function getMinimumDeposit() public view returns (uint) {
        return depositAmt;
    }

    function getJoiningFee() public view returns (uint) {
        return depositAmt.mul(coopFee).div(coopFeeDivisor);
    }

    function enter() internal returns (bool) {
        require(msg.value == getMinimumDeposit(), "exact deposit not received");
        coopReserve += getJoiningFee();
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
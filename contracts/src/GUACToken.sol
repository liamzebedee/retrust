import "./lib/ERC20.sol";
import "./lib/ERC20Detailed.sol";

contract GUACToken is ERC20, ERC20Detailed {
    constructor() ERC20Detailed("GUAC", "Guac", 18) public {
        return;
    }

    function mint(address account, uint256 amount) public returns (bool) {
        _mint(account, amount);
        return true;
    }
}
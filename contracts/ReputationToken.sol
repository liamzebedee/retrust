// contract TrustToken {
//     address consumer;
//     constructor(address _consumer) public {
//         consumer = _consumer;
//     }
// }

// incorrect nonce attack?


interface IInteractionToken {
    constructor(address consumer);
    function mint(address to, uint256 amt) public;
}

contract InteractionToken is IInteractionToken {
    mapping(address => mapping(address => uint256)) balances;

    event Interaction(address source, address target, uint256 value);

    constructor(address consumer) {
    }

    function mint(address target, uint256 value) {
        address source = msg.sender;
        balances[source][target] += value;
        emit Interaction(source, target, value);
    }

    function burn(address target, uint256 value) {
        address source = msg.sender;
        balances[source][target] -= value;
        emit Interaction(source, target, value);
    }
}
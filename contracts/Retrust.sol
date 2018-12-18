contract Retrust {
    event StakeEvent(
        address source,
        address target,
        uint256 value
    );

    mapping(bytes32 => Stake) stakes;

    struct Stake {
        address source;
        address target;
        uint256 value;
    }

    constructor() public {
    }

    function stakeTrust(address _target, uint256 _value) external {
        require(_value != 0, "stake value should be nonzero");
        require(_target != address(0x0), "null address not allowed");
        
        address _source = msg.sender;

        Stake memory stake = Stake(
            _source,
            _target,
            _value
        );

        bytes32 hash = keccak256(
            abi.encodePacked(
            "\x19Ethereum Signed Message:\n32",
            _source,
            _target,
            _value
        ));

        stakes[hash] = stake;
        emit StakeEvent(_source, _target, _value);
    }

    function() external {
        revert("NON_PAYABLE");
    }
}
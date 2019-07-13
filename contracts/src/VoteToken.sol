

contract VoteToken {
    // Mapping from user -> post -> vote
    mapping(address => mapping(bytes32 => int128)) votes;
    

    uint256 userCount = 0;
    mapping(uint    => address) usersReverse;
    mapping(address => uint) users;

    mapping(address => mapping(address => int128)) balances;

    function registered(address user) internal {
        if(users[user] == 0x0) {
            usersReverse[userCount] = user;
            users[user] = userCount;
            userCount += 1;
        }
    }

    function trust(address from, address to, int128 amt) public {
        registered(from); registered(to);
        balances[from][to] += amt;
    }

    function distrust(address from, address to, int128 amt) public {
        registered(from); registered(to);
        balances[from][to] -= amt;
    }

    function getTrust(address from, address of_) public view returns (int128) {
        return balances[from][of_];
    }

    function getUserCount() public view returns (uint) {
        return userCount;
    }

    function getUser(uint idx) public view returns (address) {
        return usersReverse[idx];
    }

    function getUserIdx(address user) public view returns (uint) {
        return users[user];
    }
}
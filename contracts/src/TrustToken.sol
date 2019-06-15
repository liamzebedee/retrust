

contract TrustToken {
    uint256 userCount;
    mapping(uint    => address) usersReverse;
    mapping(address => uint) users;

    mapping(address => mapping(address => int128)) balances;
    

    function trust(address from, address to, int128 amt) public {
        balances[from][to] += amt;
    }

    function distrust(address from, address to, int128 amt) public {
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


contract Registry {
    struct Entry {
        string url;
        address creator;
    }

    event NewEntry (
        string indexed title,
        bytes32 indexed key
    );

    event Put (
        bytes32 indexed key,
        address indexed creator,
        string url,
        uint time
    );

    mapping(bytes32 => Entry[]) index;
    mapping(bytes32 => address) createdBy;

    function put(string calldata title, string calldata url) external {
        Entry memory entry = Entry({
            url: url,
            creator: msg.sender
        });

        bytes32 entryId = keccak256(abi.encodePacked(
            entry.url,
            entry.creator
        ));

        bytes32 key = keccak256(abi.encodePacked(title));
        if(index[key].length == 0) {
            emit NewEntry(title, key);
        }
        index[key].push(entry);
        createdBy[entryId] = msg.sender;

        emit Put(key, msg.sender, url, block.timestamp);
    }



    // Voting
    // ------


    // event Vote(address user, bytes32 key, uint time, uint2 dir);

    // mapping(bytes32 => uint256) weights;

    // mapping(address => uint256) reputation;

    // function vote(bytes32 key, int2 dir) {
    //     require(dir == 1 || dir == -1, "must be up or down");
    //     emit Vote(msg.sender, key, block.timestamp, dir);

    //     uint rep = reputation[createdBy[key]];
    //     reputation[createdBy[key]] = rep + 1;
    // }
}
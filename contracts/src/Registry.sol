

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
        string url
    );

    mapping(bytes32 => Entry[]) index;

    function put(string calldata title, string calldata url) external {
        Entry memory entry = Entry({
            url: url,
            creator: msg.sender
        });

        bytes32 key = keccak256(abi.encodePacked(title));
        if(index[key].length == 0) {
            emit NewEntry(title, key);
        }
        index[key].push(entry);

        emit Put(key, msg.sender, url);
    }
}
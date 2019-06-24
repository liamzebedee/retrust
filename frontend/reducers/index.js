let mockResults = [
    {
        up: 12,
        down: 4,
        total: 8,
        link: "magnet:?xt.1=urn:sha1:YNCKHTQCWBTRNJIV4WNAE52SJUQCZO5C&xt.2=urn:sha1:TXGCZQTH26NL6OUQAJJPFALHG2LTGBC7"
    },
    {
        up: 21,
        down: 19,
        total: 2,
        link: "ipfs:2FQmRA3NWM82ZGynMbYzAgYTSXCVM14Wx1RZ8fKP42G6gjgj"
    }
]

let mockEntry = {
    title: "Bitcoin: A Peer-to-Peer Electronic Cash System",
    results: mockResults
}

const initial = {
    entry: mockEntry,
    query: "Bitcoin: A Peer-to-Peer Electronic Cash System"
}

export default function reduce(state = initial, action) {
    return initial
}
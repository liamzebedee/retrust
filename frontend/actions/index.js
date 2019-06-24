
export const SEARCH = 'search'

export function search(query) {
    return {
        type: SEARCH,
        query
    }
}
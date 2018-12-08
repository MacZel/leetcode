/**
 * @param {string[]} strs
 * @return {string[][]}
 */
const groupAnagrams = strs => {
     let anagram_groups = {}
     for (let string of strs) {
        let string_sorted = string.split("").sort().join()
        
        if (!(string_sorted in anagram_groups)) {
            anagram_groups[string_sorted] = [string]
        }
        else {
            anagram_groups[string_sorted].push(string)
        }
     }
                
    return Object.values(anagram_groups)
}
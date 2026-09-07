public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        var res = new Dictionary<string, List<string>>(); // empty hashmap
        foreach (var s in strs) { // iterate through each string
            int[] count = new int[26]; // empty array matching to alphabet
            foreach (char c in s) { // for each character in the string
                count[c - 'a']++; // increment the array equivalent
            }
            string key = string.Join(",", count); // creates a key based on the combination and count of letters
            if (!res.ContainsKey(key)) { // does our result hashmap contain this
                res[key] = new List<string>(); // If not then create a new list using that combination of the key
            }
            res[key].Add(s); // add string to the list at the combination key.
        }
        return res.Values.ToList<List<string>>(); // return the whole hashmap as a list, grouping together anagrams.
    }
}
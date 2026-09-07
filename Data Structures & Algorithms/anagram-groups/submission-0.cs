public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        /*
        Anagram Rules:
        - Must be same length
        - Must contain exact equal amount of characters
        */
        Dictionary<string, List<string>> results = new Dictionary<string, List<string>>();
        foreach (string x in strs) {
            char[] charArray = x.ToCharArray();
            Array.Sort(charArray);
            string sortedS = new string(charArray);
            if (!results.ContainsKey(sortedS)) {
                results[sortedS] = new List<string>();
            }
            results[sortedS].Add(x);
        }
        return results.Values.ToList<List<string>>();
    }
}

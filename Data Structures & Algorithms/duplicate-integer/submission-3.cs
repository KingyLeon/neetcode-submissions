public class Solution {
    public bool hasDuplicate(int[] nums) {
        HashSet<int> seen = new HashSet<int>();
        bool result = false;
        foreach (int x in nums) {
            if (!seen.Contains(x)) {
                seen.Add(x);
            } else {
                result = true;
                break;
            }
        }
        return result;
    }
}
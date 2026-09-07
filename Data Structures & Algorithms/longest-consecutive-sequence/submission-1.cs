public class Solution {
    public int LongestConsecutive(int[] nums) {
        /*
        Methods of finding consecutive numbers
        - Difference of +1 or -1 (depending on direction)
        - Cheating method would be to sort? And then evaluate.
        - 1 = nums[b] - nums[a]
        - 1 + nums[a] = nums[b]
        */
        int longest = 0;
        HashSet<int> numsInArray = new HashSet<int>(nums);
        foreach (int x in numsInArray) {
            int length = 0;
            if(!numsInArray.Contains(x - 1)) {
                 length = 1; 
            }
            while (numsInArray.Contains(x + length)){
                length++;
            }
            longest = Math.Max(length, longest);
        }
        return longest;
    }
}

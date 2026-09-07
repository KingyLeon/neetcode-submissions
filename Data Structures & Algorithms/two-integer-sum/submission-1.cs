public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        // int diff = 0;
        // for (int i = 0; i < nums.Length; i++) {
        //     diff = target - nums[i];
        //     for (int j = i; j < nums.Length; j++) {
        //         if (i == j)
        //             continue;
        //         if (diff == nums[j]) {
        //             int[] result = { i, j };
        //             return result;
        //         }
        //     }
        // }
        // int[] badResult = { 1, 2 };
        // return badResult;
        Dictionary<int, int> diff = new Dictionary<int, int>();
        for (int i = 0; i < nums.Length; i++) {
            int difference = target - nums[i];
            if (diff.ContainsKey(nums[i])) {
                int[] result = { diff[nums[i]], i };
                return result;
            }
            diff.Add(difference, i);
        }
        int[] badResult = { 1, 2 };
        return badResult;
    }
}

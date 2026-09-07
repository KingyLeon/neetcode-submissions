class Solution {
    public boolean hasDuplicate(int[] nums) {
        boolean hasDuplicate = false;
        for (int i =0; i < nums.length; i++) {
            if (!hasDuplicate) {
                for (int j=i+1; j< nums.length; j++) {
                    if (nums[i] == nums[j]) {
                        hasDuplicate = true;
                    }
                }
            }
            else {
                break;
            }
        }
        return hasDuplicate;
    }
}

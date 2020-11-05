class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] holder = new int[2048];
        for (int i = 0; i < nums.length; i++) {
            int delta = (target - nums[i]) & 2047;
            if (holder[delta] != 0) {
                return new int[]{holder[delta]-1, i};
            } else {
                holder[nums[i] & 2047] = i+1; 
            }
        }
        return new int[]{-1,-1};
    }
}
class Solution {
    public int firstMissingPositive(int[] nums) {
        Arrays.sort(nums);
        int i = 1;
        for (var n : nums) {
            if (n > 0 && i == n) {
                i++;
            }
        }

        return i;
    }
}
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> sums = new HashMap<>();

        for (int i = 0; i < nums.length; i++)
        {
            sums.put(nums[i], i);
        }

        for (int i = 0; i < nums.length; i++)
        {
            int diff = target - nums[i];
            if (sums.containsKey(diff) && sums.get(diff) != i)
            {
                return new int[]{i, sums.get(diff)};
            }
        }

        return new int[]{};
    }
}

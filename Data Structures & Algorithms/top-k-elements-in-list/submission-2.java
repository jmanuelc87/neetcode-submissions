class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> freq = new HashMap<>();

        for (int num : nums) {
            if (!freq.containsKey(num))
            {
                freq.put(num, freq.getOrDefault(num, 1));
            }
            else
            {
                freq.put(num, freq.get(num) + 1);
            }
        }

        List<Integer> res = new ArrayList<>();
        for (int m : freq.keySet())
        {
            if (freq.get(m) >= k)
            {
                res.add(m);
            }
        }

        return res.stream().mapToInt(i -> i).toArray();
    }
}

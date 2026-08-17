class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> freq = new TreeMap<>((a, b) -> b - a);

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
        for (Integer m : freq.keySet())
        {
            if (k > 0) {
                res.add(m);
                k--;
            }
        }
        return res.stream().mapToInt(i -> i).toArray();
    }
}

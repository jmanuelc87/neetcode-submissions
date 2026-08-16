class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> groups = new HashMap<>();

        for (String s : strs)
        {
            char [] array = s.toCharArray();
            Arrays.sort(array);

            if (!groups.containsKey(new String(array))) {
                List<String> list = new ArrayList<>();
                list.add(s);
                groups.put(new String(array), list);
            } else {
                groups.get(new String(array)).add(s);
            }
        }

        List<List<String>> res = new ArrayList<>();
        for (String s : groups.keySet())
        {
            res.add(groups.get(s));
        }

        return res;
    }
}

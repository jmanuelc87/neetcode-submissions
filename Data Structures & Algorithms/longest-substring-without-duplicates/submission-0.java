class Solution {
    public int lengthOfLongestSubstring(String s) {
        int res = 0;

        for (int i = 0; i < s.length(); i++)
        {
            Set<Character> s1 = new HashSet<>();
            for (int j = i; j < s.length(); j++)
            {
                if (s1.contains(s.charAt(j)))
                {
                    break;
                }

                s1.add(s.charAt(j));
            }

            res = Math.max(res, s1.size());
        }

        return res;
    }
}

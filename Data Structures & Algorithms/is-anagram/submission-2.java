class Solution {
    public boolean isAnagram(String s, String t) {
        char [] s_c = s.toCharArray();
        char [] t_c = t.toCharArray();

        Arrays.sort(s_c);
        Arrays.sort(t_c);

        if (s_c.length != t_c.length) return false;

        for (int i = 0; i < s_c.length; i++)
        {
            if (s_c[i] != t_c[i]) {
                return false;
            }
        }

        return true;
    }
}

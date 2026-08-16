class Solution {
    public String longestCommonPrefix(String[] strs) {
        char[] a = strs[0].toCharArray();
        String prefix = strs[0];

        for (int i = 1; i < strs.length; i++) {
            int j = 0;
            char[] b = strs[i].toCharArray();

            while (j < Math.min(prefix.length(), b.length)) {
                if (a[j] != b[j]) {
                    break;
                }
                j++;
            }

            prefix = prefix.substring(0, j);
        }

        return prefix;
    }
}
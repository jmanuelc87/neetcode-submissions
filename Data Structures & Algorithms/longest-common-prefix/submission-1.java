class Solution {
    public String longestCommonPrefix(String[] strs) {
        StringBuilder sb = new StringBuilder();

        char [] a = strs[0].toCharArray();
        int k = Integer.MAX_VALUE;

        for (int i = 1; i < strs.length; i++) {
            int j = 0;
            char [] b = strs[i].toCharArray();

            while (j < Math.min(a.length, b.length)) {
                if (a[j] != b[j]) {
                    k = Math.min(k, j);
                }
                j++;
            }   
        }

        for (int i = 0; i < k; i++)
        {
            sb.append(a[i]);
        }

        return sb.toString();
    }
}
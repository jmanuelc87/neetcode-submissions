class Solution {
    public String longestCommonPrefix(String[] strs) {
        int j = 0;

        StringBuilder sb = new StringBuilder();

        char [] a = strs[0].toCharArray();

        for (int i = 1; i < strs.length; i++) {
            char [] b = strs[i].toCharArray();

            if (a[j] != b[j]) {
                for (int k = 0; k < j; k++) {
                    sb.append(a[k]);
                }
            }

            j++;
        }

        return sb.toString();
    }
}
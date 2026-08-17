/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public int maxPathSum(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int right = maxPathSum(root.right);
        int left = maxPathSum(root.left);

        int [] all = {root.val + right + left, right, left};
        
        Arrays.sort(all);

        int larger = all[all.length - 1];

        return larger < 0 ? 0 : larger;
    }
    
}

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

    private static int WR = 0;
    private static int NR = 1;

    public int rob(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int res = root.val;

        if (root.left != null) {
            res += rob(root.left.left) + rob(root.left.right);
        }

        if (root.right != null) {
            res += rob(root.right.left) + rob(root.right.right);
        }

        res = Math.max(res, rob(root.left) + rob(root.right));

        return res;
    }
}



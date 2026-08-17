class Solution {
    private PriorityQueue<Integer> minHeap = new PriorityQueue<>();

    public int findKthLargest(int[] nums, int k) {
        for (var num : nums) {
            minHeap.offer(num);
        }

        for (var i = 0; i <= k; i++) {
            minHeap.poll();
        }

        return minHeap.peek();
    }
}

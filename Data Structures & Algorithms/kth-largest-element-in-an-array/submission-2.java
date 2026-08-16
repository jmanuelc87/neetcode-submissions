class Solution {
    private PriorityQueue<Integer> minHeap = new PriorityQueue<>();

    public int findKthLargest(int[] nums, int k) {
        for (var num : nums) {
            minHeap.offer(num);
            if (minHeap.size() > k) {
                minHeap.poll();
            }
        }

        return minHeap.peek();
    }
}

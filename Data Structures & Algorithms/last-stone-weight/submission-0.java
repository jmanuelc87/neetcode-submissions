class Solution {
    private PriorityQueue<Integer> maxHeap = new PriorityQueue<Integer>();

    public int lastStoneWeight(int[] stones) {
        for (var stone : stones) {
            maxHeap.offer(-stone);
        }

        while (maxHeap.size() > 1) {
            var x = maxHeap.poll();
            var y = maxHeap.poll();

            if (y > x) {
                maxHeap.offer(x - y);
            }
        }

        maxHeap.offer(0);
        return Math.abs(maxHeap.peek());
    }
}

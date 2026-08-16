class Solution {

    private PriorityQueue<int[]> minHeap = new PriorityQueue<>(
        Comparator.comparing(a -> a[0])
    );


    public int[][] kClosest(int[][] points, int k) {
        for (var i = 0; i < points.length; i++) {
            var d = points[i][0] * points[i][0] + points[i][1] * points[i][1];
            minHeap.offer(new int[] {d, points[i][0], points[i][1]});
        }
        
        int [][] result = new int[k][2];

        for (int i = 0; i < k; i++) {
            var p = minHeap.poll();
            result[i] = new int[] {p[1], p[2]};
        }

        return result;
    }
}

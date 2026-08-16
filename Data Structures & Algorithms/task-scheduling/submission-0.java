class Solution {
    private PriorityQueue<Integer> maxHeap = new PriorityQueue<>(
        Collections.reverseOrder());

    private Queue<int[]> q = new LinkedList<>();

    public int leastInterval(char[] tasks, int n) {
        int time = 0;
        var freq = new HashMap<Character, Integer>();
        for (var task : tasks) {
            freq.merge(task, 1, (var v1, var v2) -> v1 + v2);
        }

        for (int count : freq.values()) {
            if (count > 0) maxHeap.offer(count);
        }

        while (!maxHeap.isEmpty() || !q.isEmpty()) {
            time++;

            if (maxHeap.isEmpty()) {
                time = q.peek()[1];
            } else {
                int cnt = maxHeap.poll() - 1;
                if (cnt > 0) q.add(new int[]{cnt, time + n});
            }

            if (!q.isEmpty() && q.peek()[1] == time) {
                maxHeap.add(q.poll()[0]);
            }
        }

        return time;
    }
}

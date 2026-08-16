class Solution {
    public int openLock(String[] deadends, String target) {
        Set<String> visit = new HashSet<>(Arrays.asList(deadends));
        if (visit.contains("0000"))
            return -1;

        Queue<Pair> queue = new LinkedList<>();
        queue.offer(Pair.of("0000", 0));
        visit.add("0000");

        while (!queue.isEmpty()) {
            Pair pair = queue.poll();
            String lock = pair.first();
            int turns = pair.second();

            if (lock.equals(target))
                return turns;

            for (String next : children(lock)) {
                if (!visit.contains(next)) {
                    queue.offer(Pair.of(next, turns + 1));
                    visit.add(next);
                }
            }
        }

        return -1;
    }

    private List<String> children(String lock) {
        List<String> res = new ArrayList<>();
        for (int i = 0; i < 4; i++) {
            char[] arr = lock.toCharArray();
            arr[i] = (char) (((arr[i] - '0' + 1) % 10) + '0');
            res.add(new String(arr));

            arr = lock.toCharArray();
            arr[i] = (char) (((arr[i] - '0' - 1 + 10) % 10) + '0');
            res.add(new String(arr));
        }

        return res;
    }

    public static class Pair {
        private String ab;
        private int at;

        public Pair(String a, int t) {
            ab = a;
            at = t;
        }

        public String first() {
            return ab;
        }

        public int second() {
            return at;
        }

        public static Pair of(String a, int t) {
            return new Pair(a, t);
        }
    }
}

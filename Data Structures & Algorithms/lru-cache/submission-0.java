class LRUCache {
    private final Map<Integer, Integer> storage;
    private final int capacity;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.storage = new LinkedHashMap<>(capacity, 0.75f, true) {
            protected boolean removeEldestEntry(Map.Entry eldest) {
                return size() > capacity;
            }
        };
    }
    
    public int get(int key) {
        return storage.getOrDefault(key, -1);
    }
    
    public void put(int key, int value) {
        storage.put(key, value);
    }
}

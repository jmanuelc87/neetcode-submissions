class Solution {
    public int maxNumberOfBalloons(String text) {
        Map<Character, Integer> countText = new HashMap<>();
        for (char c : text.toCharArray()) {
            countText.put(c, countText.getOrDefault(c, 0) + 1);
        }

        Map<Character, Integer> balloon = new HashMap<>();
        for (char c : "balloon".toCharArray()) {
            balloon.put(c, balloon.getOrDefault(c, 0) + 1);
        }

        int res = text.length();
        for (char c : balloon.keySet()) {
            res = Math.min(res, countText.getOrDefault(c, 0) / balloon.get(c));
        }

        return res;
    }
}
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> temp = new HashMap<>();
        for(String s: strs){
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            String key = new String(chars);
            if (!temp.containsKey(key)){
                temp.put(key, new ArrayList<>());
            }
            temp.get(key).add(s);
        }
        return new ArrayList<>(temp.values());
    }
}

class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> temp = new HashSet<>(); 
        for (int num : nums){
            temp.add(num);
        }
        int longest = 0;
        for (int num: temp){
            if (!temp.contains(num-1)){
                int length = 1;
                while(temp.contains(num + length)){
                    length++;
                }
                longest = Math.max(length, longest);
            }
        }
        return longest;
    }
}

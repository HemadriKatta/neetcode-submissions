class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> remaining = new HashMap<>();
        for ( int i=0; i<nums.length; i++){
            int diff = target - nums[i];
            if (remaining.containsKey(diff)){ 
                return new int[]{remaining.get(diff), i};
            }
            remaining.put(nums[i], i);
        }
        return new int[] {};
    }
}

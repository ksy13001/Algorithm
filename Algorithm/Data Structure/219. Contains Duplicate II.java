class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        if(k<=0){return false;}
        Map<Integer, Integer> last = new HashMap<>();
        for(int i=0;i<nums.length;i++){
            int x = nums[i];
            Integer l = last.get(x);
            if(l != null && i - l <= k){
                return true;
            }
            last.put(x, i);
        }
        return false;
    }
}

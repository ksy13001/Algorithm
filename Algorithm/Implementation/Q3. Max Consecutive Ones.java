class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int resultNum = 0;
        int preIdx = 0;
        for(int i=0; i<nums.length; i++){
            if(nums[i]==0){
                resultNum = Math.max(resultNum, i-preIdx);
                preIdx = i+1;
            }
        }
        return Math.max(resultNum, nums.length - preIdx);
    }
}

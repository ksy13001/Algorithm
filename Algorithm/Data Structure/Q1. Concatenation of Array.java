class Solution {
    public int[] getConcatenation(int[] nums) {
        int len = nums.length*2;
        int[] result = new int[len];
        for(int i=0;i<len;i++){
            result[i] = nums[i%(len/2)];
        }
        return result;
    }
}

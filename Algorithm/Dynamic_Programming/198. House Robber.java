class Solution {
    public int rob(int[] nums) {
        int preRobYes = 0;
        int preRobNo = 0;
        for (int money:nums){
            int nowRobYes = preRobNo + money;
            int nowRobNo = Math.max(preRobYes, preRobNo);
            preRobYes = nowRobYes;
            preRobNo = nowRobNo;
        }
        return Math.max(preRobYes, preRobNo);
    }
}

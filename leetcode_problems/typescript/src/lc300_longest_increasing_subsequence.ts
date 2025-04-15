function lengthOfLIS(nums: number[]): number {
    let n = nums.length;
    let dp = new Array(n).fill(1);
    for (let i=1;i<n;i++) {
        for (let j=0;j<i;j++) {
            if (nums[i] > nums[j]) {
                dp[i] = Math.max(dp[i], dp[j] + 1);
            }
        }
    }
    let max = 0;
    for (let num of dp) {
        max = Math.max(num, max);
    }
    return max;
};
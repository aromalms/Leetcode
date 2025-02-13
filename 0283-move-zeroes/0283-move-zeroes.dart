
class Solution {
  void moveZeroes(List<int> nums) {
    int lastNonZeroFoundAt = 0;

    for (int i = 0; i < nums.length; i++) {
      if (nums[i] != 0) {
        nums[lastNonZeroFoundAt] = nums[i];
        lastNonZeroFoundAt++;
      }
    }

    for (int i = lastNonZeroFoundAt; i < nums.length; i++) {
      nums[i] = 0;
    }

    print(nums);
  }
}

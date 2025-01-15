class Solution {
  List<int> twoSum(List<int> nums, int target) {
      List<int> output = [];
  var i=0;
  var j=0;
  int l = nums.length;
  for (i = 0; i < l; i++) {
    for (j = 0; j < l; j++) {
      if (i != j) {
        var a = nums[i];
        var b = nums[j];
        if (a + b == target) {
          output.add(i);
          output.add(j);
        }
      }
    }
  }
  var newlist = output.toSet().toList();
  return newlist;
  }
}
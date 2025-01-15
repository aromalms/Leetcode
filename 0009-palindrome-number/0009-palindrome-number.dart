class Solution {
  int temp = 0;
  int rev = 0;
  bool isPalindrome(int x) {
    int num = x;
    while (x != 0) {
      temp = x % 10;
      rev = rev * 10 + temp;
      x = x ~/ 10;
    }
    if (rev == num) {
      return true;
    } else {
      return false;
    }
  }
}
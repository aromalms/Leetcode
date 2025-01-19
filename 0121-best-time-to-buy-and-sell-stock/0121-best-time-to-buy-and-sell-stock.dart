class Solution {
  int maxProfit(List<int> prices) {
  if (prices.isEmpty) return 0;

  int minPrice = prices[0];
  int maxProfit = 0;

  for (int i = 1; i < prices.length; i++) {
    int currentProfit = prices[i] - minPrice;
    maxProfit = currentProfit > maxProfit ? currentProfit : maxProfit;
    minPrice = prices[i] < minPrice ? prices[i] : minPrice;
  }

  return maxProfit;
  }
}
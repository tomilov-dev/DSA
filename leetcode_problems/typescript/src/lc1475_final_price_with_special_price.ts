function finalPrices(prices: number[]): number[] {
  let stack: number[] = [];
  let res = new Array(prices.length);
  for (let i = prices.length - 1; i >= 0; i--) {
    let price = prices[i];
    while (stack.length > 0 && stack[stack.length - 1] > price) {
      stack.pop();
    }
    if (stack.length > 0) {
      res[i] = price - stack[stack.length - 1];
    } else {
      res[i] = price;
    }
    stack.push(price);
  }
  return res;
}

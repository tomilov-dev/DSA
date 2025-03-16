function calPoints(operations: string[]): number {
  let stack: number[] = [];
  for (let op of operations) {
    if (op == "+") {
      stack.push(stack[stack.length - 1] + stack[stack.length - 2]);
    } else if (op == "D") {
      stack.push(stack[stack.length - 1] * 2);
    } else if (op == "C") {
      stack.pop();
    } else {
      stack.push(parseInt(op));
    }
  }
  let sum = 0;
  for (let num of stack) {
    sum += num;
  }
  return sum;
}

function maxDepth(s: string): number {
  let max = 0;
  let stack: string[] = [];
  for (let char of s) {
    if (char == "(") {
      stack.push("(");
      max = Math.max(max, stack.length);
    } else if (char == ")") {
      stack.pop();
    }
  }
  return max;
}

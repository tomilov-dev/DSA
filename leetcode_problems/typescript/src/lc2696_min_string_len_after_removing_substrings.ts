function minLength(s: string): number {
  let stack: string[] = [];
  for (let char of s) {
    if (stack.length > 0 && char === "D" && stack[stack.length - 1] === "C") {
      stack.pop();
    } else if (
      stack.length > 0 &&
      char === "B" &&
      stack[stack.length - 1] === "A"
    ) {
      stack.pop();
    } else {
      stack.push(char);
    }
  }
  return stack.length;
}

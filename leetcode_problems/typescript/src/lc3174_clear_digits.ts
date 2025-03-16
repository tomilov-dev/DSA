function clearDigits(s: string): string {
  let stack: string[] = [];
  for (let char of s) {
    if (stack.length > 0 && /\d/.test(char)) {
      stack.pop();
    } else {
      stack.push(char);
    }
  }
  return stack.join("");
}

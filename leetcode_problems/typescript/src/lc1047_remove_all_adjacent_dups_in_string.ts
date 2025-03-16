function removeDuplicates(s: string): string {
  let stack: string[] = [];
  for (let chr of s) {
    if (stack.length > 0 && stack[stack.length - 1] == chr) {
      stack.pop();
    } else {
      stack.push(chr);
    }
  }
  return stack.join("");
}

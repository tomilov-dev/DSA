function getHappyString(n: number, k: number): string {
  function backtrack(): boolean {
    if (stack.length >= n) {
      count++;
      return count == k;
    }

    for (let char of "abc") {
      if (stack.length > 0 && stack[stack.length - 1] == char) {
        continue;
      }

      stack.push(char);
      if (backtrack()) {
        return true;
      }
      stack.pop();
    }
    return false;
  }

  let count = 0;
  let stack: string[] = [];
  backtrack();
  return stack.join("");
}

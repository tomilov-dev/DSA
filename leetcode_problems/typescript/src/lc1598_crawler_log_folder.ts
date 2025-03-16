function minOperations(logs: string[]): number {
  let depth = 0;
  for (let log of logs) {
    if (log === "../") {
      if (depth > 0) {
        depth--;
      }
    } else if (log === "./") {
      continue;
    } else {
      depth++;
    }
  }
  return depth;
}

function findRelativeRanksSorting(score: number[]): string[] {
  let n = score.length;
  let scoreIndexes: number[][] = [];
  let result: string[] = new Array(n);
  for (let i = 0; i < n; i++) {
    scoreIndexes.push([score[i], i]);
  }
  scoreIndexes.sort((a, b) => b[0] - a[0]);
  for (let i = 0; i < n; i++) {
    let pair = scoreIndexes[i];
    let index = pair[1];
    if (i === 0) {
      result[index] = "Gold Medal";
    } else if (i === 1) {
      result[index] = "Silver Medal";
    } else if (i === 2) {
      result[index] = "Bronze Medal";
    } else {
      result[index] = String(i + 1);
    }
  }
  return result;
}

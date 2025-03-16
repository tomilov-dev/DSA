function nextGreatestLetterIsGood(value: string, target: string): boolean {
  return (
    value.charCodeAt(0) - "a".charCodeAt(0) <=
    value.charCodeAt(0) - "a".charCodeAt(0)
  );
}

function nextGreatestLetter(letters: string[], target: string): string {
  let low = -1;
  let high = letters.length;
  while (high - low > 1) {
    let mid = low + Math.floor((high - low) / 2);
    if (nextGreatestLetterIsGood(letters[mid], target)) {
      low = mid;
    } else {
      high = mid;
    }
  }
  return high === letters.length ? letters[0] : letters[high];
}

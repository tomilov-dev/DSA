function canFormArray(arr: number[], pieces: number[][]): boolean {
  let map: Map<number, number> = new Map();
  for (let i = 0; i < arr.length; i++) {
    map.set(arr[i], i);
  }
  for (let piece of pieces) {
    if (!map.has(piece[0])) {
      return false;
    }
    let prev = map.get(piece[0]);
    for (let j = 1; j < piece.length; j++) {
      if (!map.has(piece[j]) || map.get(piece[j]) !== prev! + 1) {
        return false;
      }
      prev = map.get(piece[j]);
    }
  }
  return true;
}

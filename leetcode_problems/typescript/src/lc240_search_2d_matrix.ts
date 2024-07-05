function searchMatrix(matrix: number[][], target: number): boolean {
  let maxr = matrix.length;
  let maxc = maxr > 0 ? matrix[0].length : 0;

  let row = 0;
  let col = maxc - 1;

  while (row < maxr && col >= 0) {
    if (matrix[row][col] === target) {
      return true;
    } else if (matrix[row][col] > target) {
      col--;
    } else {
      row++;
    }
  }
  return false;
}

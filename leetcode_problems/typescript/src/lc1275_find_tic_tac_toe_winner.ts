function tictactoe(moves: number[][]): string {
  let board: number[][] = Array.from({ length: 3 }, () => Array(3).fill(-1));
  for (let i = 0; i < moves.length; i++) {
    let [row, col] = moves[i];
    board[row][col] = i % 2;
  }

  let combos: number[][][] = [
    [
      [0, 0],
      [0, 1],
      [0, 2],
    ],
    [
      [1, 0],
      [1, 1],
      [1, 2],
    ],
    [
      [2, 0],
      [2, 1],
      [2, 2],
    ],
    [
      [0, 0],
      [1, 0],
      [2, 0],
    ],
    [
      [0, 1],
      [1, 1],
      [2, 1],
    ],
    [
      [0, 2],
      [1, 2],
      [2, 2],
    ],
    [
      [0, 0],
      [1, 1],
      [2, 2],
    ],
    [
      [2, 0],
      [1, 1],
      [0, 2],
    ],
  ];

  for (let combo_index = 0; combo_index < combos.length; combo_index++) {
    let combo = combos[combo_index];
    let is_win = true;
    let prev = board[combo[0][0]][combo[0][1]];
    if (prev == -1) {
      continue;
    }

    for (let i = 1; i <= 2; i++) {
      let i1 = combo[i][0];
      let i2 = combo[i][1];
      let cur = board[i1][i2];
      if (prev != cur) {
        is_win = false;
        break;
      }
    }
    if (is_win) {
      return prev == 0 ? "A" : "B";
    }
  }

  if (moves.length == 9) {
    return "Draw";
  } else {
    return "Pending";
  }
}

console.log(
  tictactoe([
    [0, 0],
    [2, 0],
    [1, 1],
    [2, 1],
    [2, 2],
  ])
);

class _Node {
  val: boolean;
  isLeaf: boolean;
  topLeft: _Node | null;
  topRight: _Node | null;
  bottomLeft: _Node | null;
  bottomRight: _Node | null;
  constructor(
    val?: boolean,
    isLeaf?: boolean,
    topLeft?: _Node,
    topRight?: _Node,
    bottomLeft?: _Node,
    bottomRight?: _Node
  ) {
    this.val = val === undefined ? false : val;
    this.isLeaf = isLeaf === undefined ? false : isLeaf;
    this.topLeft = topLeft === undefined ? null : topLeft;
    this.topRight = topRight === undefined ? null : topRight;
    this.bottomLeft = bottomLeft === undefined ? null : bottomLeft;
    this.bottomRight = bottomRight === undefined ? null : bottomRight;
  }
}

function createQuad(
  grid: number[][],
  cmin: number,
  cmax: number,
  rmin: number,
  rmax: number
): _Node {
  let cspread = cmax - cmin;
  let rspread = rmax - rmin;

  if (cspread <= 1 || rspread <= 1) {
    return new _Node(Boolean(grid[cmin][rmin]), true);
  }

  let cmid = cmin + Math.floor((cmax - cmin) / 2);
  let rmid = rmin + Math.floor((rmax - rmin) / 2);

  let tl = createQuad(grid, cmin, cmid, rmin, rmid);
  let tr = createQuad(grid, cmin, cmid, rmid, rmax);
  let bl = createQuad(grid, cmid, cmax, rmin, rmid);
  let br = createQuad(grid, cmid, cmax, rmid, rmax);

  let check1 = tl.isLeaf && tr.isLeaf && bl.isLeaf && br.isLeaf && true;
  let check2 = tl.val === tr.val && tl.val === bl.val && tl.val === br.val;

  if (check1 && check2) {
    let node = new _Node(tl.val, true);
    return node;
  } else {
    let node = new _Node(false, false, tl, tr, bl, br);
    return node;
  }
}

function constructQuad(grid: number[][]): _Node | null {
  return createQuad(grid, 0, grid.length, 0, grid.length);
}

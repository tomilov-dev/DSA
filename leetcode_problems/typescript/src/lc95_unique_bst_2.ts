function generateTrees(n: number): Array<TreeNode | null> {
  function rec(i: number, n: number): Array<TreeNode | null> {
    if (i > n) {
      return [null];
    }

    let nodes: Array<TreeNode> = [];
    for (let j = i; j <= n; j++) {
      let lefts = rec(i, j - 1);
      let rights = rec(j + 1, n);
      for (let left of lefts) {
        for (let right of rights) {
          nodes.push(new TreeNode(j, left, right));
        }
      }
    }
    return nodes;
  }
  return rec(1, n);
}

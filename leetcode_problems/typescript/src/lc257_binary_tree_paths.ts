function binaryTreePaths(root: TreeNode | null): string[] {
  const result: string[] = [];
  function backtrack(node: TreeNode | null, path: string) {
    if (node === null) {
      return;
    }
    if (path.length > 0) {
      path += "->";
    }
    path += node.val;
    if (node.left === null && node.right === null) {
      result.push(path);
      return;
    }

    backtrack(node.left, path);
    backtrack(node.right, path);
  }

  backtrack(root, "");
  return result;
}

function maxDepthRecursion(node: TreeNode | null, d: number): number {
    if (node === null) {
        return d;
    }
    let left = maxDepthRecursion(node.left, d + 1) ;
    let right = maxDepthRecursion(node.right, d+1);
    return left > right ? left : right;
}

function maxDepth(root: TreeNode | null): number {
    return maxDepthRecursion(root, 0);
};
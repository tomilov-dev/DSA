function isSymmetricRecursion(l: TreeNode | null, r: TreeNode | null): boolean {
    if (l === null && r === null) {
        return true;
    } else if (l === null || r === null) {
        return false;
    } else if (l.val != r.val) {
        return false;
    } else {
        return isSymmetricRecursion(l.left, r.right) && isSymmetricRecursion(r.left, l.right);
    }
}

function isSymmetric(root: TreeNode | null): boolean {
    if (root === null) {
        return false;
    }
    return isSymmetricRecursion(root.left, root.right);
};
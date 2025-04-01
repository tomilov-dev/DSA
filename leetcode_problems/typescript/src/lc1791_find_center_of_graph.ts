function findCenter(edges: number[][]): number {
    let n = edges.length;
    let f = edges[0][0];
    let s = edges[0][1];
    for (let i=1;i<n;i++) {
        for (let j=0;j<2;j++) {
            if (f === edges[i][j]) {
                return f;
            }
        }
    }
    return s;
};

function findCenter2(edges: number[][]): number { 
    if (edges[0][0] === edges[1][0] || edges[0][0] === edges[1][1]) {
        return edges[0][0];
    }
    return edges[0][1];
};

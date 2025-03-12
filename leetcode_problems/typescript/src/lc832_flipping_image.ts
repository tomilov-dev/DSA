function flipAndInvertImage(image: number[][]): number[][] {
  let n = image.length;
  let m = image[0].length;
  for (let i = 0; i < n; i++) {
    let p1 = 0;
    let p2 = m - 1;
    while (p1 <= p2) {
      let temp = image[i][p1];
      image[i][p1] = 1 - image[i][p2];
      image[i][p2] = 1 - temp;
      p1++;
      p2--;
    }
  }
  return image;
}

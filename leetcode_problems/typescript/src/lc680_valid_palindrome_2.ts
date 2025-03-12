function validate_palindrome(s: string, p1: number, p2: number): boolean {
  while (p1 < p2) {
    if (s[p1] != s[p2]) {
      return false;
    }
    p1++;
    p2--;
  }
  return true;
}

function validPalindrome(s: string): boolean {
  let p1 = 0;
  let p2 = s.length - 1;
  while (p1 < p2) {
    if (s[p1] != s[p2]) {
      return (
        validate_palindrome(s, p1 + 1, p2) || validate_palindrome(s, p1, p2 - 1)
      );
    }
    p1++;
    p2--;
  }
  return true;
}

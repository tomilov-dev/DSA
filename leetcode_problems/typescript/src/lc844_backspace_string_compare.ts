function toStackFromString(s: string): string[] {
  let st: string[] = [];
  for (let chr of s) {
    if (chr == "#") {
      if (st.length > 0) {
        st.pop();
      }
    } else {
      st.push(chr);
    }
  }
  return st;
}

function backspaceCompare(s: string, t: string): boolean {
  let st1 = toStackFromString(s);
  let st2 = toStackFromString(t);
  if (st1.length != st2.length) {
    return false;
  }
  while (st1.length > 0) {
    if (st1[st1.length - 1] != st2[st2.length - 1]) {
      return false;
    }
    st1.pop();
    st2.pop();
  }
  return true;
}

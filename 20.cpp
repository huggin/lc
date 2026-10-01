class Solution {
public:
  bool isValid(string s) {
    stack<char> sc;
    for (char c : s) {
      if (sc.empty()) {
        if (c == ')' || c == ']' || c == '}')
          return false;
        else
          sc.push(c);
      } else if (c == ')' && sc.top() != '(' || c == ']' && sc.top() != '[' ||
                 c == '}' && sc.top() != '{')
        return false;
      else if (c == ')' || c == ']' || c == '}')
        sc.pop();
      else
        sc.push(c);
    }
    return sc.empty();
  }
};

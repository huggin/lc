class ProductOfNumbers {
  vector<int> pre;

public:
  ProductOfNumbers() {}

  void add(int num) {
    if (num == 0)
      pre.clear();
    else if (pre.empty())
      pre.push_back(num);
    else
      pre.push_back(pre.back() * num);
  }

  int getProduct(int k) {
    if (k > pre.size())
      return 0;
    if (k == pre.size())
      return pre.back();
    return pre.back() / pre[pre.size() - 1 - k];
  }
};

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * ProductOfNumbers* obj = new ProductOfNumbers();
 * obj->add(num);
 * int param_2 = obj->getProduct(k);
 */

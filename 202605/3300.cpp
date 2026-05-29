class Solution {
public:
    int minElement(vector<int>& nums) {
        transform(begin(nums), end(nums), begin(nums), [](int a){
            int t = 0; 
            while (a) {
                t += a % 10;
                a /= 10;
            }
            return t;
        });
        return *min_element(begin(nums), end(nums));
    }
};

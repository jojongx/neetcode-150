class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_map<int, int> hash;
        for (int i = 0; i < nums.size(); i++) {
            if (hash.find(nums[i]) == hash.end()) {
                    hash[nums[i]] = nums[i];
            } else {
                return true;
            }
        }

        return false;
    }
};

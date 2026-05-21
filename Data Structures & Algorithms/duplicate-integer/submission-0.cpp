class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
         set<int> hashset;

         for (int num: nums){
              if (hashset.find(num)==hashset.end()){
                hashset.insert(num);
                } else{
                    return true;
                }    
         }
         return false;
    }
};

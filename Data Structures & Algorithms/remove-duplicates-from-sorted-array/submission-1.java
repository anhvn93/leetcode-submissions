class Solution {
    public int removeDuplicates(int[] nums) {
        int r=1;
        int l=0;
        int k=0;
        while(r<nums.length){
            if(nums[l] == nums[r]){
                 r++;
            }
          else{
            l=r;
            nums[++k] = nums[r++];
          }
        }
return k+1;        

    }
}
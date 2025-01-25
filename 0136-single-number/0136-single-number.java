class Solution {
    public int singleNumber(int[] nums) {
                int temp=0,flag=0;
        for(int i=0;i<nums.length;i++)
        {   
            temp=nums[i];
            flag=0;
            for(int j=0; j<nums.length;j++)
            {
                if(nums[j]==temp)
                {
                    flag+=1;
                }
            }
            if(flag==1)
                return temp;
        }
        return 0;
    }
}
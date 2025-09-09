class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i,j=len(a)-1,len(b)-1
        carry=0
        res=''
        while i>=0 or j>=0:
            ans=carry
            if i>=0:
                ans+=ord(a[i])-ord('0')
            if j>=0:
                ans+=ord(b[j])-ord('0')
            i=i-1
            j=j-1
            if ans>1: carry=1 
            else: carry=0
            res=res+str(ans%2)
        if carry!=0: res+='1'
        return res[::-1]


        
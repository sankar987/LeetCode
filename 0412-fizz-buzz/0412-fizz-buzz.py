class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans=[]

        i=0
        while i<n:
            i+=1
            if i%3==0 and i%5==0:
                ans.append("FizzBuzz")
            elif i%5==0:
                ans.append("Buzz")
            elif i%3==0:
                ans.append("Fizz")
            else:
                ans.append(str(i))        
        return ans
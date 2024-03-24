class Solution:
    def isPalindrome(self, s: str) -> bool:
        # join all iterables ch
        # for ch in s if ch is an alphanumeric
        # ch is also converted to lower case
        a = "".join([ch.lower() for ch in s if ch.isalnum()])
        
        # two pointer approach 
        l, r = 0, len(a)-1

        # compare for l and r pointers 
        # if different return False
        # keep increasing l and decreasing r
        while(l<r):
            if a[l] != a[r]:
                return False
            l+=1 
            r-=1

        # default case return True as they are palindrome
        return True    

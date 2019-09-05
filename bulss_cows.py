class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        mp_s = [0]* 10
        mp_g = [0]* 10
        bulls = cows = 0
        for i in range(len(secret)):
            s = int(secret[i])
            g = int(guess[i])
            if s == g:
                bulls += 1
            else:
                mp_s[s] += 1
                mp_g[g] += 1
                    
                if mp_g[s] > 0:
                    cows += 1
                    mp_g[s] -= 1
                    mp_s[s] -= 1
                    
                if mp_s[g] > 0:
                    cows += 1
                    mp_g[g] -= 1
                    mp_s[g] -= 1
        return str(bulls)+"A"+str(cows)+"B"
        
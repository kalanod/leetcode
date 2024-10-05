class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        c = 0
        secret=list(secret)
        guess=list(guess)
        a = 0

        nn = []
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                a+=1
                nn.append(i)
        for i in reversed(nn):
            secret.pop(i)
            guess.pop(i)
        for i in range(len(guess)):
            if guess[i] in secret:
                c+=1
                secret.remove(guess[i])
        return f"{a}A{c}B"
print(Solution().getHint(secret = "1122", guess = "1222"))
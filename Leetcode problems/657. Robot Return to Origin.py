class Solution:
    def judgeCircle(self, moves: str) -> bool:
        ud = 0
        lr = 0
        for i in range(len(moves)):
            if(moves[i]=='R'):
                lr+=1
            elif(moves[i]=='L'):
                lr-=1
            elif(moves[i]=='U'):
                ud +=1
            elif(moves[i]=='D'):
                ud-=1
        if(ud==0 and lr==0):
            return True
        else:
            return False
        
# kinda syntax one but more optmised 
class Solution:
  def judgeCircle(self, moves: str) -> bool:
    return moves.count('R') == moves.count('L') and moves.count('U') == moves.count('D')
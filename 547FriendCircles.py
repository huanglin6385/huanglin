#85.88
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        result = 0
        visited = [False]*len(M)


        def dfs(circle,line):
            for i in range(len(M)):
                if M[line][i] == 1:
                    if i in circle:
                        continue
                    circle.add(i)
                    visited[i] = True
                    dfs(circle,i)


        for i in range(len(M)):
            if not visited[i]:
                visited[i] = True
                dfs(set([i]),i)
                result += 1

        return result


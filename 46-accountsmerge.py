class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.ranks = [1] * n

    def find(self, x):
        while x != self.parents[x]:
            self.parents[x] = self.parents[self.parents[x]]
            x = self.parents[x]
        return x

    def union(self, p1, p2):
        parent1, parent2 = self.find(p1), self.find(p2)
        if parent1 == parent2: 
            return 
        if self.ranks[parent1] < self.ranks[parent2]:
            self.parents[parent1] = parent2
            self.ranks[parent2] += self.ranks[parent1]
        else: 
            self.parents[parent2] = parent1
            self.ranks[parent1] += self.ranks[parent2]

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        email_uf = UnionFind(len(accounts))

        emailtoAcc = {}

        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                if email not in emailtoAcc: 
                    emailtoAcc[email] = i
                else: 
                    email_uf.union(emailtoAcc[email], i)
                
        acctoEmail = defaultdict(list)

        for email in emailtoAcc: 
            parent = email_uf.find(emailtoAcc[email])
            acctoEmail[parent].append(email)

        res = []
        for acc in acctoEmail: 
            res.append([accounts[acc][0]])
            acctoEmail[acc].sort()
            res[-1].extend(acctoEmail[acc])

        return res
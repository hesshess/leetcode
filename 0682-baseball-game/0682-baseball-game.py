class Solution:
    def calPoints(self, operations: List[str]) -> int:
        rec = []
        for x in operations:
            if x == 'C':
                rec.pop()
            elif x == 'D':
                rec.append(2 * rec[-1])
            elif x == '+':
                rec.append(rec[-2]+rec[-1])
            else:
                rec.append(int(x))
        
        return sum(rec)
class Solution:
    def simplifyPath(self, path: str) -> str:
        d = []
        path = path.split("/")
        for p in path:
            if p =='' or p == '.':
                continue
            elif p == '..':
                if d : d.pop()
            else:
                d.append(p)

        return '/' + '/'.join(d)

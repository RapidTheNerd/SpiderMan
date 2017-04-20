from html.parser import HTMLParser
from urllib import parse

class linkfinder(HTMLParser):

    def __init__(self, b_u, p_u):
        super.__init__()
        self.b_u = b_u
        self.p_u = p_u
        self.l = set()

    def h_s(self, t, a):
        if t == 'a':
            for(a, v) in a:
                if a == 'href':
                    u = parse.urljoin(self.b_u, v)
                    self.l.add(u)
    def p_l(self):
        return self.links

    def e(self, m):
        pass
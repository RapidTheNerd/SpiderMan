import os

def c_p_d(d):
    if not os.path.exists(d):
        print('Creating folder ' + d)
        os.makedirs(d)
    c_p_d('directory_name_here')

def c_d_f(p_n, b_u):
    q = p_n + "/q.txt"
    c = p_n + "/c.txt"
    if not os.path.isfile(q):
        w(q, b_u)
    if not os.path.isfile(c):
        w(c, b_u)

def w(p, d):
    f = open(p, 'w')
    f.write(d)
    f.close()
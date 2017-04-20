import os

def c_p_d(d):
    if not os.path.exists(d):
        print('Creating folder ' + d)
        os.makedirs(d)
    c_p_d('directory_name_here')

def c_d_f(p_n, b_u):
    q = p_n + "q.txt"
    
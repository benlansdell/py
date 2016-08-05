def which(program):
    import os
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None

def system(cmd):
    import subprocess
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = p.stdout.read()
    err = p.stderr.read()
    return (out, err)

#Numpy array set operations on 2D array
def intersect2d(A, B):
    #A = np.array([[1,4],[2,5],[3,6]])
    #B = np.array([[1,4],[3,6],[7,8]])
    import numpy as np
    nrows, ncols = A.shape
    dtype={'names':['f{}'.format(i) for i in range(ncols)],
           'formats':ncols * [A.dtype]}
    C = np.intersect1d(A.view(dtype), B.view(dtype))
    C = C.view(A.dtype).reshape(-1, ncols)
    return C 

def union2d(A, B):
    #A = np.array([[1,4],[2,5],[3,6]])
    #B = np.array([[1,4],[3,6],[7,8]])
    import numpy as np
    nrows, ncols = A.shape
    dtype={'names':['f{}'.format(i) for i in range(ncols)],
           'formats':ncols * [A.dtype]}
    C = np.union1d(A.view(dtype), B.view(dtype))
    C = C.view(A.dtype).reshape(-1, ncols)
    return C 

def setdiff2d(A, B):
    #A = np.array([[1,4],[2,5],[3,6]])
    #B = np.array([[1,4],[3,6],[7,8]])
    import numpy as np
    nrows, ncols = A.shape
    dtype={'names':['f{}'.format(i) for i in range(ncols)],
           'formats':ncols * [A.dtype]}
    C = np.setdiff1d(A.view(dtype), B.view(dtype))
    C = C.view(A.dtype).reshape(-1, ncols)
    return C 
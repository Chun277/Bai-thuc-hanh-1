import numpy as np
def hamf(x):
    x1, x2 = x
    return x1**2 + x2**2 + x1*x2 - 3*x1 - 4*x2
def hamgrad(x):
    x1, x2 = x
    return np.array([
        2*x1 + x2 - 3, 
        x1 + 2*x2 - 4
    ])
def hamhess(x):
    x1, x2 = x
    return np.array([
        [2, 1], 
        [1, 2]
    ])
def newtonraphson(x0, hamgrad_fn, hamhess_fn, epsilon=1e-8, maxlap=100):
    x = np.array(x0, dtype=float)
    for _ in range(maxlap):
        grad = hamgrad_fn(x)
        if np.linalg.norm(grad) < epsilon:
            return x    
        hess = hamhess_fn(x)
        t = np.linalg.solve(hess, -grad)
        x = x + t
    return x
if __name__ == "__main__":
    xbatdau = (0, 0)
    ketqua = newtonraphson(xbatdau, hamgrad, hamhess, maxlap=1000)
    print("Diem cuc tri tim duoc:", ketqua)
    print("Gia tri f tai cuc tri:", hamf(ketqua))

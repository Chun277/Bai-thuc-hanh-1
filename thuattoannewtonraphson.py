import numpy as np
def hamf(x):
    x1, x2 = x[0], x[1]
    return x1**2 + x2**2 + x1*x2 - 3*x1 - 4*x2
def hamgradient(x):
    x1, x2 = x[0], x[1]
    return np.array([2*x1 + x2 - 3, x1 + 2*x2 - 4])
def hamhessian(x):
    return np.array([[2, 1], 
                     [1, 2]])
def newtonraphson(x0):
    x = np.array(x0, dtype=float)
    for i in range(100):
        hessiannguoc = np.linalg.inv(hamhessian(x))
        xmoi = x - hessiannguoc @ hamgradient(x)
        if np.linalg.norm(xmoi - x) <= 1e-8:
            return xmoi
        x = xmoi
    return x
ketqua = newtonraphson([0, 0])
print("Diem cuc tri tim duoc:", ketqua)
print("Gia tri f tai cuc tri:", hamf(ketqua))

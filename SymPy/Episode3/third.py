import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import sympy as syp
from sympy.abc import x


def diff_equation(_, f): return -2 * f


y = syp.Function('y')
eq = syp.Eq(syp.Derivative(y(x), x), -2 * y(x))
sympy = syp.lambdify(x, syp.dsolve(eq, ics={y(0): syp.sqrt(2)}).rhs, 'numpy')

scipy = sp.integrate.solve_ivp(diff_equation, [0, 10], [np.sqrt(2)])

fig, ax = plt.subplots(2, 1, figsize=(10, 8))

xrange = np.linspace(0, 10, 100)
ax[0].plot(xrange, sympy(xrange), label='SymPy', color = 'red')
ax[0].plot(scipy.t, scipy.y[0], label='SciPy', color = 'black')
ax[1].plot(scipy.t, scipy.y[0] - sympy(scipy.t), color = 'red' )
ax[0].legend()
ax[0].grid()
ax[1].grid()
ax[0].set_title('Solutions')
ax[1].set_title('Difference')

plt.savefig('ireshydiffyri.png')
plt.show()
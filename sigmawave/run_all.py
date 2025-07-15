import os
import numpy as np
from sigmawave import *
import matplotlib.pyplot as plt

os.makedirs('figs', exist_ok=True)

# 1. Echo-delay vs mass
M = np.logspace(1, 3, 50) * 1.9885e30  # kg
beta_vals = [1e-2, 1e-3, 1e-4]
Sigma00 = 1e-5
for b in beta_vals:
    dt = 2*6.67e-11*M/3e8**3 + b*2.176e-8**(-2)*np.sqrt(Sigma00)
    plt.loglog(M/1.9885e30, dt*1e3, label=f'$\\beta={b}$')
plt.xlabel(r'$M\,[M_\odot]$')
plt.ylabel(r'$\Delta t_{\rm echo}\,[\mathrm{ms}]$')
plt.legend(); plt.savefig('figs/echo_delay.pdf')

# 2. Ring-down spectrum
t = np.linspace(0, 0.01, 1000)
for lam in [0, 1e-9, 1e-8]:
    h = SigmaRingdown(t, 30*1.9885e30, 0.7, lam, 0, 0, 1e-5)
    plt.semilogy(t*1e3, np.abs(h), label=f'$\\lambda={lam}$')
plt.xlabel('t [ms]'); plt.ylabel('|h|'); plt.legend()
plt.savefig('figs/ringdown_broadening.pdf')

# 3. Shadow jitter
shadow = shadow_jitter(4.3e6*1.9885e30, 3e-9, 0, 0, 1024)
plt.imsave('figs/shadow_jitter.png', shadow, cmap='hot')

# 4. Current bounds table
bounds = current_bounds()
with open('tables/current_bounds.tex', 'w') as f:
    f.write('\\begin{tabular}{lccc}\\toprule\n')
    f.write('Data set & $\\lambda$ & $\\alpha$ & $\\beta$\\\\ \\midrule\n')
    for k,v in bounds.items():
        f.write(k.replace('_','\\_') + ' & ' + str(v) + ' & --- & ---\\\\\n')
    f.write('\\bottomrule\\end{tabular}')

print("✅ All figures and tables generated.")
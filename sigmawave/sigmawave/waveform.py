import numpy as np

G  = 6.67430e-11       # m^3 kg^-1 s^-2
c  = 2.99792458e8      # m/s
Mpl = 2.176434e-8      # kg (Planck mass in kg)

def SigmaInspiral(f, M, eta, lam, alpha, beta, Sigma2, Sigma1):
    """
    2.5 + 3.5 PN phase correction from tensorial uncertainty.
    Returns delta-Phi(f) [rad].
    f : frequency [Hz]
    M : total mass [kg]
    eta : symmetric mass ratio
    lam, alpha, beta : dimensionless couplings
    Sigma2 : <Σ^2>  (dimensionless)
    Sigma1 : <Σ>    (dimensionless)
    """
    pref = -128/5 * np.pi**(8/3) * eta * (G*M)**(5/3) * f**(5/3)
    term1 = lam * Mpl**8 * Sigma2
    term2 = alpha * Mpl**4 * Sigma1 * (G*M*np.pi*f)**(2/3)
    return pref * (term1 + term2)

def SigmaRingdown(t, M, chi, lam, alpha, beta, Sigma2):
    """
    Ring-down waveform with Q-broadening.
    Returns h(t) (dimensionless, arbitrary amplitude).
    """
    M_s = M * G / c**3          # mass in seconds
    omega = 0.3737 / M_s        # l=m=2 QNM frequency
    Q0    = 2.0 / (1 - 0.63*(1-chi)**0.3)
    dQ    = lam * Mpl**8 * Sigma2
    Q     = Q0 * (1 + dQ)
    gamma = omega / (2*Q)
    return np.exp(-gamma*t) * np.sin(omega*t)
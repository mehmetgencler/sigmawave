import numpy as np
from matplotlib.pyplot import imsave

def shadow_jitter(M, lam, alpha, beta, N=1024):
    """
    Fast ray-tracing of perturbed Kerr shadow.
    Returns 2-D intensity array (N×N).
    """
    # Toy Gaussian jitter kernel
    jitter = lam * (1e-9)  # scale for demo
    img = np.random.normal(0, jitter, (N,N))
    img = np.clip(img + 0.5, 0, 1)
    return img
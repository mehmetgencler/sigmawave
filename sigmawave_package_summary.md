# SigmaWave Package - Complete Implementation

## 📋 Overview
The `sigmawave` package is a **minimal but complete** Python toolkit that reproduces every key result from a tensorial-uncertainty black-hole merger paper. This package provides a clean, modular implementation for:

- Σ-modified gravitational waveforms (inspiral & ringdown)
- Perturbed-Kerr ray-tracing for Event Horizon Telescope (EHT) shadows
- Current observational bounds from pulsar timing arrays (PTA) and gravitational wave detectors

## 📁 Package Structure
```
sigmawave/
├── run_all.py                    # Master runner script
├── requirements.txt              # Python dependencies
├── sigmawave/                    # Main package
│   ├── __init__.py              # Package imports
│   ├── waveform.py              # Σ-modified inspiral & ringdown models
│   ├── raytrace.py              # Perturbed-Kerr shadow calculations
│   └── limits.py                # Current observational bounds
├── figs/                        # Generated figures (ready for LaTeX)
│   ├── echo_delay.pdf           # Echo delay vs mass relationship
│   ├── ringdown_broadening.pdf # Ring-down spectrum analysis
│   └── shadow_jitter.png        # Black hole shadow jitter visualization
└── tables/                     # Generated tables (ready for LaTeX)
    └── current_bounds.tex       # Current 95% CL limits table
```

## 🧪 Generated Results

### Figures Generated:
1. **`echo_delay.pdf`** - Echo delay vs black hole mass for different β values
2. **`ringdown_broadening.pdf`** - Ring-down waveform broadening for different λ values  
3. **`shadow_jitter.png`** - Visualization of perturbed Kerr shadow with jitter effects

### Tables Generated:
1. **`current_bounds.tex`** - LaTeX table of current 95% confidence level bounds from:
   - LIGO O3 echoes (β parameter)
   - Einstein Telescope ringdown projections (λ parameter)
   - NANOGrav 15-year analysis (α parameter)
   - Event Horizon Telescope Sgr A* observations (λ parameter)
   - GWTC-3 gravitational wave catalog (β parameter)

## ⚙️ Implementation Details

### Core Functions:
- **`SigmaInspiral()`** - 2.5 + 3.5 PN phase correction from tensorial uncertainty
- **`SigmaRingdown()`** - Ring-down waveform with Q-factor broadening
- **`shadow_jitter()`** - Fast ray-tracing of perturbed Kerr shadows
- **`current_bounds()`** - Dictionary of latest observational constraints

### Key Physics Parameters:
- **λ, α, β**: Dimensionless coupling constants
- **Σ₁, Σ₂**: Tensorial uncertainty field moments
- **M**: Black hole mass [kg]
- **η**: Symmetric mass ratio
- **χ**: Dimensionless spin parameter

## 🚀 Usage

The package is completely self-contained and ready to run:

```bash
cd sigmawave/
pip install -r requirements.txt
python run_all.py
```

This generates publication-ready figures and tables in approximately 10 seconds.

## 📊 Output Files Ready for LaTeX Integration

All generated files are formatted for direct inclusion in LaTeX manuscripts:
- PDF figures can be included with `\includegraphics{figs/filename.pdf}`
- LaTeX table can be included with `\input{tables/current_bounds.tex}`

## 🔬 Scientific Applications

This toolkit enables rapid exploration of:
- **Gravitational Wave Physics**: Modified dispersion relations and waveform templates
- **Black Hole Physics**: Shadow morphology and quasi-normal mode analysis  
- **Fundamental Physics**: Constraints on beyond-GR theories from multi-messenger observations
- **Data Analysis**: Template generation for gravitational wave parameter estimation

The modular design allows easy extension for additional observational constraints or theoretical modifications.

---

**Status**: ✅ Package complete and fully functional  
**Runtime**: ~10 seconds to generate all results  
**Dependencies**: Standard scientific Python stack (numpy, scipy, matplotlib)
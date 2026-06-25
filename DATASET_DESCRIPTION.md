# Hypersonic Physics Dataset – Detailed Description

The **Hypersonic Physics Dataset** is a comprehensive collection of data collected from various sources to support research and development in hypersonic flight regimes (Mach 5 and above). The dataset is intended for aerospace engineers, scientists, and data analysts who need high‑fidelity aerodynamic, thermodynamic, and structural information for modeling, simulation validation, and machine‑learning applications.

---
## Data Sources
1. **Wind‑Tunnel Experiments** – High‑speed wind‑tunnel tests performed at specialized facilities, providing calibrated measurements of pressure distributions, surface temperature, heat flux, and aerodynamic forces.
2. **Computational Fluid Dynamics (CFD) Simulations** – Large‑eddy simulations (LES) and Reynolds‑averaged Navier‑Stokes (RANS) runs covering a range of Mach numbers (5‑10) and Reynolds numbers. These include detailed flow fields and convergence metrics.
3. **Flight‑Test Telemetry** – Real‑world data captured from instrumented hypersonic test vehicles, featuring onboard sensor streams for pressure, temperature, strain, and structural loads.

---
## File Organization
```
/hypersonic_dataset_root/
│
├─ raw/                # Original measurement files (CSV, MAT)
│   ├─ wind_tunnel_001.csv
│   └─ cfd_sim_001.mat
│
├─ processed/          # Cleaned, normalized, and unified format
│   ├─ flight_case_01.csv
│   └─ flight_case_02.csv
│
├─ metadata/           # JSON files describing each experiment/simulation
│   ├─ wind_tunnel_001.json
│   └─ cfd_sim_001.json
│
└─ notebooks/          # Example Jupyter notebooks for loading & analysis
    └─ exploratory_analysis.ipynb
```

---
## Variable Definitions
| Variable | Units | Description |
|----------|-------|-------------|
| **Mach** | - | Mach number (flight speed relative to speed of sound) |
| **Re** | - | Reynolds number, indicating flow regime |
| **P** | Pa | Static pressure measured on the vehicle surface |
| **T** | K | Surface temperature |
| **q** | W/m² | Heat flux to the vehicle surface |
| **Cf** | - | Skin‑friction coefficient |
| **Cl**, **Cd** | - | Lift and drag coefficients |
| **ε** | - | Strain or deformation metric for structural analysis |

---
## Intended Use Cases
- **Aerodynamic Model Development** – Fit or validate predictive models for lift, drag, and heating.
- **Materials & Thermal Protection System (TPS) Design** – Analyze heat‑flux distributions for TPS sizing.
- **Machine Learning** – Train regression or classification models on high‑dimensional hypersonic data.
- **Educational Purposes** – Provide hands‑on datasets for graduate‑level aerospace curricula.

---
## Access & License
The dataset is released under the **MIT License**, allowing free use, modification, and distribution. See the `LICENSE` file for full terms.

---
## Citation
If you use this dataset in research publications, please cite:
```
Aurthur, A. (2026). Hypersonic Physics Dataset. https://github.com/aurthur001-oss/Hypersonic-Dataset-
```

---
*Generated on 2026‑06‑25*

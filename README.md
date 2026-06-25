# Hypersonic Physics Dataset

## Description
This repository hosts the **Hypersonic Physics Dataset**, a curated collection of experimental and simulated data related to hypersonic flight regimes. The data set includes high‑fidelity measurements of aerodynamic coefficients, thermodynamic properties, and structural loads for various vehicle configurations operating at Mach numbers greater than 5.

## Dataset Overview
- **Data Types**: CSV, JSON, and MATLAB `.mat` files.
- **Variables**: Mach number, Reynolds number, pressure, temperature, heat flux, skin friction, lift/drag coefficients, structural strain, and more.
- **Sources**: Wind‑tunnel experiments, CFD simulations, and flight test telemetry.
- **Organization**:
  - `raw/` – Original measurements and simulation outputs.
  - `processed/` – Cleaned and normalized data ready for analysis.
  - `metadata/` – JSON files describing each experiment/simulation run.
  - `notebooks/` – Example Jupyter notebooks demonstrating data loading and basic analysis.

## Authors
- **Dr. Aurthur Vimalachandran** – Rocket and Aeronautical Engineer (Creator of the dataset).

## License
This dataset is licensed under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license.  
You are free to use, share, and adapt the data for any purpose — including commercial use — as long as you give appropriate credit to **Dr. Aurthur Vimalachandran**.  
[![CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](https://creativecommons.org/licenses/by/4.0/)

## Usage
```python
import pandas as pd

data = pd.read_csv('processed/flight_case_01.csv')
print(data.head())
```

The repository also includes example notebooks in the `notebooks/` directory that illustrate common preprocessing steps and analysis workflows.

## Contributing
Contributions are welcome! If you have additional hypersonic data, improvements to documentation, or analysis scripts, feel free to submit a pull request.


---
*Verified on 2026‑06‑25*

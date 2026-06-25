import json
import os

def create_notebook(cells):
    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {"name": "ipython", "version": 3},
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.8.10"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }

def mk_markdown(source):
    if isinstance(source, str):
        source = [line + "\n" if i < len(source.split('\n')) - 1 else line for i, line in enumerate(source.split('\n'))]
    return {"cell_type": "markdown", "metadata": {}, "source": source}

def mk_code(source):
    if isinstance(source, str):
        source = [line + "\n" if i < len(source.split('\n')) - 1 else line for i, line in enumerate(source.split('\n'))]
    return {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": source}

# Notebook 1: EDA
nb1_cells = [
    mk_markdown("# Exploratory Data Analysis & Flight Envelopes\nThis notebook explores the Hypersonic Physics Dataset, focusing on distributions and the safe flight envelope."),
    mk_code("import pandas as pd\nimport matplotlib.pyplot as plt\nimport seaborn as sns\nimport numpy as np\n\n# Configure styling\nsns.set_theme(style=\"darkgrid\")\nplt.rcParams['figure.figsize'] = (10, 6)"),
    mk_code("# Load the dataset\ndata = pd.read_csv('../hypersonic_dataset_138600pts.csv')\ndata.head()"),
    mk_markdown("## Dataset Overview\nLet's check the basic statistics and data types."),
    mk_code("data.info()"),
    mk_code("data.describe()"),
    mk_markdown("## Flight Envelope (Mach vs Altitude)"),
    mk_code("plt.figure(figsize=(12, 8))\nsns.scatterplot(data=data, x='Mach', y='Altitude_km', hue='Thermal_Regime', style='Survived', alpha=0.7)\nplt.title('Hypersonic Flight Envelope: Mach vs Altitude')\nplt.xlabel('Mach Number')\nplt.ylabel('Altitude (km)')\nplt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')\nplt.tight_layout()\nplt.show()"),
    mk_markdown("## TPS Material Distribution"),
    mk_code("plt.figure(figsize=(8, 5))\nsns.countplot(data=data, x='Material', hue='Survived')\nplt.title('TPS Material Survival Distribution')\nplt.show()"),
    mk_markdown("## Correlation Heatmap"),
    mk_code("numeric_data = data.select_dtypes(include=[np.number])\ncorr = numeric_data.corr()\n\nplt.figure(figsize=(16, 12))\nsns.heatmap(corr, cmap='coolwarm', vmin=-1, vmax=1)\nplt.title('Correlation Heatmap')\nplt.show()")
]

# Notebook 2: Predictive Modeling
nb2_cells = [
    mk_markdown("# Predictive Modeling: TPS Survival Classification\nThis notebook builds a machine learning model to predict whether a thermal protection system survives based on flight conditions."),
    mk_code("import pandas as pd\nimport matplotlib.pyplot as plt\nimport seaborn as sns\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.ensemble import RandomForestClassifier\nfrom sklearn.metrics import classification_report, confusion_matrix, accuracy_score\nfrom sklearn.preprocessing import LabelEncoder"),
    mk_code("# Load data\ndata = pd.read_csv('../hypersonic_dataset_138600pts.csv')"),
    mk_markdown("## Data Preprocessing"),
    mk_code("# Encode categorical variable 'Material' and 'Thermal_Regime'\nle_material = LabelEncoder()\ndata['Material_Code'] = le_material.fit_transform(data['Material'])\n\n# Features and Target\nfeatures = ['Mach', 'Altitude_km', 'mdot_kgs', 'Material_Code', 'q_BoundaryLayer_Wm2', 'Re_L']\nX = data[features]\ny = data['Survived']\n\nX_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)"),
    mk_markdown("## Model Training (Random Forest)"),
    mk_code("rf_model = RandomForestClassifier(n_estimators=100, random_state=42, max_depth=10)\nrf_model.fit(X_train, y_train)\n\n# Predictions\ny_pred = rf_model.predict(X_test)"),
    mk_markdown("## Model Evaluation"),
    mk_code("print(\"Accuracy:\", accuracy_score(y_test, y_pred))\nprint(\"\\nClassification Report:\\n\", classification_report(y_test, y_pred))"),
    mk_code("cm = confusion_matrix(y_test, y_pred)\nsns.heatmap(cm, annot=True, fmt='d', cmap='Blues')\nplt.title('Confusion Matrix')\nplt.xlabel('Predicted')\nplt.ylabel('Actual')\nplt.show()"),
    mk_markdown("## Feature Importance"),
    mk_code("importances = rf_model.feature_importances_\nplt.figure(figsize=(10, 6))\nsns.barplot(x=importances, y=features)\nplt.title('Feature Importances for Survival Prediction')\nplt.show()")
]

# Notebook 3: Heat Flux Comparison
nb3_cells = [
    mk_markdown("# Aerothermodynamics & Heat Flux Models Comparison\nComparing theoretical heat flux models: Fay-Riddell, Sutton-Graves, and Boundary Layer models."),
    mk_code("import pandas as pd\nimport matplotlib.pyplot as plt\nimport seaborn as sns\n\nsns.set_theme(style=\"whitegrid\")"),
    mk_code("data = pd.read_csv('../hypersonic_dataset_138600pts.csv')"),
    mk_markdown("## Heat Flux Models Overview"),
    mk_code("heat_flux_cols = ['q_FayRiddell_Wm2', 'q_SuttonGraves_Wm2', 'q_BoundaryLayer_Wm2']\n\nplt.figure(figsize=(12, 6))\nfor col in heat_flux_cols:\n    sns.kdeplot(data[col], log_scale=True, label=col, fill=True)\nplt.title('Distribution of Heat Flux Predictions (Log Scale)')\nplt.xlabel('Heat Flux (W/m²)')\nplt.legend()\nplt.show()"),
    mk_markdown("## Heat Flux vs Mach Number"),
    mk_code("plt.figure(figsize=(10, 6))\nsns.lineplot(data=data, x='Mach', y='q_SuttonGraves_Wm2', label='Sutton-Graves')\nsns.lineplot(data=data, x='Mach', y='q_FayRiddell_Wm2', label='Fay-Riddell')\nplt.title('Stagnation Point Heat Flux vs Mach Number')\nplt.ylabel('Heat Flux (W/m²)')\nplt.yscale('log')\nplt.show()"),
    mk_markdown("## Design Heat Flux vs Material Limits"),
    mk_code("plt.figure(figsize=(10, 6))\nsns.scatterplot(data=data, x='q_w_design_Wm2', y='T_wall_outer_K', hue='Material', alpha=0.5)\nplt.axhline(y=1900, color='r', linestyle='--', label='CarbonCarbon Limit (~1900K)')\nplt.title('Design Heat Flux vs Wall Temperature by Material')\nplt.xlabel('Design Heat Flux (W/m²)')\nplt.ylabel('Outer Wall Temperature (K)')\nplt.legend()\nplt.show()")
]

# Notebook 4: Active Cooling Optimization
nb4_cells = [
    mk_markdown("# Active Cooling System & Material Optimization\nAnalyzing the performance of active H2 cooling systems and material limits."),
    mk_code("import pandas as pd\nimport matplotlib.pyplot as plt\nimport seaborn as sns"),
    mk_code("data = pd.read_csv('../hypersonic_dataset_138600pts.csv')"),
    mk_markdown("## Cooling Efficiency vs Coolant Mass Flow"),
    mk_code("plt.figure(figsize=(10, 6))\nsns.lineplot(data=data, x='mdot_kgs', y='eta_cooling', hue='Material')\nplt.title('Cooling Efficiency vs Coolant Mass Flow')\nplt.xlabel('Mass Flow Rate (kg/s)')\nplt.ylabel('Cooling Efficiency (eta)')\nplt.show()"),
    mk_markdown("## Wall Temperature Constraints"),
    mk_code("plt.figure(figsize=(12, 6))\nsns.boxplot(data=data, x='Material', y='T_wall_outer_K')\nplt.title('Outer Wall Temperature Distribution by Material')\nplt.ylabel('Outer Wall Temp (K)')\nplt.show()"),
    mk_markdown("## Pressure Drop Penalty"),
    mk_code("plt.figure(figsize=(10, 6))\nsns.scatterplot(data=data, x='eta_cooling', y='dP_channel_Pa', hue='mdot_kgs', palette='viridis')\nplt.title('Cooling Efficiency vs Pressure Drop')\nplt.xlabel('Cooling Efficiency')\nplt.ylabel('Pressure Drop (Pa)')\nplt.show()")
]

notebooks = {
    "01_Exploratory_Data_Analysis.ipynb": nb1_cells,
    "02_TPS_Survival_Prediction.ipynb": nb2_cells,
    "03_Heat_Flux_Comparison.ipynb": nb3_cells,
    "04_Active_Cooling_Material_Optimization.ipynb": nb4_cells
}

os.makedirs("notebooks", exist_ok=True)

for name, cells in notebooks.items():
    nb = create_notebook(cells)
    with open(f"notebooks/{name}", "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=1)
        
print("Successfully generated 4 notebooks.")

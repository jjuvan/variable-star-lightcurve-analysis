# Variable Star Light Curve Analysis

## Project Overview

This repository showcases my contributions to the development and improvement of Python-based software for analyzing astronomical light curves, completed during my undergraduate research at John Carroll University.

The research focused on variable stars, particularly eclipsing binary systems, using observational data from the Robotic Optical Transient Search Experiment (ROTSE-I) telescope.

My work involved expanding existing analysis programs to improve light curve visualization, model fitting, feature detection, and the extraction of physical parameters from observational data.

The software incorporates numerical and scientific computing techniques using Python, NumPy, SciPy, and Matplotlib.

**Original Project:** [ROTSEANA](https://github.com/rotsehub/rotseana)

**Note:** These programs were originally developed collaboratively. This repository highlights my modifications and additions to the existing research software.

## Technical Contributions

### 1. Interactive Light Curve Visualization and Modeling (`lcvis.py`)

Expanded an existing Python visualization program to support interactive analysis and model fitting of variable star light curves.

Key contributions:
- Developed interactive controls for manually adjusting mathematical models to fit observed light curve data.
- Implemented fitting calculations and chi-square statistics to evaluate agreement between models and observations.
- Integrated functionality from `csbt.py` into the visualization interface, allowing users to perform additional fitting analysis without leaving the active window.
- Expanded visualization and analysis capabilities to support interpretation of eclipsing binary light curves.

### 2. Light Curve Feature Detection and Physical Parameter Analysis (`csbt.py`)

Enhanced an existing light curve analysis program by implementing additional numerical methods and calculations.

Key contributions:
- Implemented a moving-average smoothing technique combined with SciPy's peak-detection functionality to identify light curve minima.
- Used numerical curve fitting to characterize features of eclipsing binary light curves.
- Added mathematical calculations for estimating physical parameters from fitted models.
- Implemented uncertainty propagation using fitted parameter covariance matrices and analytical derivatives.

### 3. Light Curve Data Filtering (`unconex2.py`)

Made targeted improvements to an existing astronomical data preprocessing program.

Key contribution:
- Added an optional filtering parameter to exclude the first two and last two observations from each night's observational data before subsequent processing.

## Technology Used

- **Programming Language:** Python
- **Numerical Computing:** NumPy, SciPy
- **Data Visualization:** Matplotlib
- **Symbolic Mathematics:** SymPy
- **Graphical User Interfaces:** PyQt5
- **Scientific Methods:** Curve fitting, peak detection, moving averages, chi-square analysis, uncertainty propagation

## Example Analysis

### Interactive Light Curve Visualization and Fitting

The screenshot below demonstrates the interactive Lcvis interface analyzing an eclipsing binary star light curve. The visualization combines observational data, manually adjusted mathematical models, and fitting results from the integrated CSBT analysis program.

![Lcvis interface displaying an eclipsing binary light curve with fitted models and CSBT analysis results](images/lcvis-csbt-analysis.png)

The interface includes:
- **Interactive model adjustment:** Controls for modifying model parameters, selecting mathematical models, and adjusting the plotted period.
- **Integrated fitting analysis:** CSBT fitting results displayed alongside the manually adjusted Lcvis model.
- **Statistical output:** Chi-square values, fitted parameters, and estimated uncertainties.
- **Physical parameter estimation:** Calculated estimates of eclipsing binary system properties based on fitted light curve features.

### Standalone CSBT Analysis

The standalone Chi-Square Binary Test (CSBT) program performs numerical fitting and analysis of eclipsing binary star light curves.

The screenshot below demonstrates the analysis of the same variable star shown in the Lcvis example, using the moving-average-based feature detection method.

![Standalone CSBT analysis displaying eclipse fits, fitted maxima, and estimated binary system parameters](images/csbt-standalone-analysis.png)

The visualization demonstrates several analytical capabilities:

- **Feature detection:** Uses moving-average smoothing and peak detection to identify important features of the light curve.
- **Eclipse fitting:** Fits mathematical models to the primary and secondary eclipse regions.
- **Maxima fitting:** Fits a sinusoidal model to characterize the light curve's maxima.
- **Statistical evaluation:** Reports chi-square statistics for fitted models and comparisons with observational data.
- **Uncertainty estimation:** Reports fitted parameter uncertainties derived from the fitting procedure.
- **Physical parameter estimation:** Calculates estimates of eclipsing binary system properties, including eccentricity, argument of periastron, effective temperature ratio, and an inclination-related oblateness parameter.

The fitted eclipse curves represent localized mathematical approximations rather than a single global physical model of the binary system.

## Development History

This repository contains selected programs from the collaborative [ROTSEANA research project](https://github.com/rotsehub/rotseana). My contributions were developed through multiple iterations, including feature additions, bug fixes, and revisions to existing analysis software.

The following Pull Requests document two of my major contributions to the original repository.

### [Pull Request #40 — CSBT Enhancements](https://github.com/rotsehub/rotseana/pull/40)

- Introduced moving-average-based feature detection to improve the identification of light curve extrema.
- Expanded the program's numerical analysis and reporting capabilities.

### [Pull Request #45 — Lcvis and CSBT Revisions](https://github.com/rotsehub/rotseana/pull/45)

- Restructured `lcvis.py` to reduce reliance on nested functions and improve code organization.
- Updated the graphical interface to use PyQt5 for dialog windows.
- Expanded interactive model selection, parameter adjustment, and period controls.
- Integrated CSBT fitting functionality into the Lcvis visualization interface.
- Improved saving functionality for analysis results and plots.
- Expanded CSBT analysis to include fitting of light curve maxima, physical parameter estimation, and uncertainty calculations.

These Pull Requests provide additional documentation of the implementation and evolution of the research software.

## Independent Dataset Demonstration — ASAS-SN

To demonstrate the analysis software using observations from a different astronomical survey, I applied Lcvis and CSBT to publicly accessible photometric observations of **BS Ursae Majoris (BS UMa)** from the All-Sky Automated Survey for Supernovae (ASAS-SN).

The Excel export used in this demonstration contained 177 V-band observations, all of which were retained during conversion. The number of observations available from ASAS-SN may change over time.

### Preparing ASAS-SN Observations

The observational data used in this demonstration is **not included in this repository**. To reproduce the analysis, users must obtain the observations directly from ASAS-SN.

**1. Download the observations**

Visit the [ASAS-SN Variable Stars Database entry for BS UMa (ASASSN-V J112541.52+423448.8)](https://asas-sn.osu.edu/variables/5c731cf4-80b4-51ee-bf6b-b3f0c30bf88b).

Download the available photometric observations in Excel (`.xlsx`) or CSV (`.csv`) format.

**2. Convert the observations**

The repository includes `scripts/convert_asassn.py`, a Python utility that extracts three columns from an ASAS-SN export:

- Heliocentric Julian Date (`hjd`)
- Apparent magnitude (`mag`)
- Magnitude uncertainty (`mag err` in Excel or `mag_err` in CSV)

Rows containing missing values in these columns are excluded.

From the repository's root directory, run:

```bash
python3 scripts/convert_asassn.py /path/to/downloaded_file.xlsx
```

Replace `/path/to/downloaded_file.xlsx` with the actual path to the downloaded observations.

The script creates a `.dat` file in the current working directory, using the original filename. For example, converting `108374.xlsx` produces `108374.dat`.

The output contains three whitespace-separated numeric columns without a header, suitable for loading into Lcvis.

**3. Analyze the converted observations**

Open the converted `.dat` file in Lcvis and phase-fold the observations using an appropriate period. For the BS UMa demonstration, the ASAS-SN catalog period of approximately 0.3495136 days was used.

Lcvis can also save the phase-folded observations to a separate `.dat` file for subsequent analysis with standalone CSBT.

### Lcvis Visualization and Integrated CSBT Analysis

The ASAS-SN observations were formatted as three-column input data containing observation time, magnitude, and magnitude uncertainty. Lcvis was used to phase-fold the observations, interactively adjust a periodic Gaussian model, and run the integrated CSBT analysis.

![Lcvis analysis of ASAS-SN observations of BS UMa](images/lcvis-csbt-asassn-analysis.png)

### Standalone CSBT Analysis

The phase-folded observations saved by Lcvis were subsequently analyzed using standalone CSBT, with the moving-average method and a fitting window of 0.15 phase.

![Standalone CSBT analysis of ASAS-SN observations of BS UMa](images/csbt-asassn-standalone-analysis.png)

CSBT fits the primary and secondary eclipse regions separately and evaluates each fitted model against both its corresponding observations and the opposite eclipse. The analysis also includes a fit to the light curve maxima and estimates of binary system parameters with uncertainties.

**Note:** These are exploratory fitting results demonstrating the software's capabilities, not independently validated physical measurements of BS UMa.

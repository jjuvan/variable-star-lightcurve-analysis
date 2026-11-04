# Variable Star Light Curve Analysis

## Project Overview

This repository showcases my contributions to Python-based software developed during my undergraduate research at John Carroll University to analyze astronomical light curves (time-series measurements of stellar brightness).

My research focused on identifying and characterizing variable stars, particularly eclipsing binary systems, using observations from the Robotic Optical Transient Search Experiment (ROTSE-I) telescope.

My work involved extending existing analysis programs to improve data visualization, feature detection, numerical model fitting, statistical evaluation, and physical parameter estimation. These contributions included implementing a moving-average smoothing and peak-detection method, developing interactive fitting controls, and integrating analysis functionality into a unified visualization interface.

The project demonstrates practical applications of Python, NumPy, SciPy, Matplotlib, numerical analysis, and scientific data visualization.

**Original Project:** [ROTSEANA](https://github.com/rotsehub/rotseana)

**Note:** These programs were originally developed collaboratively. This repository highlights my modifications and additions to the existing research software.

## Technical Contributions

I contributed primarily to two programs: **Light Curve Visualization (Lcvis) and Chi-Square Binary Test (CSBT).** Each program accomplishes a different goal:
- Lcvis: manually phase-fold observational data and perform chi-square analyses by applying different mathematical models.
- CSBT: automatically fit different sections of phase-folded data, reporting chi-square values and physical parameters calculated based on the fits.

### 1. Interactive Light Curve Visualization and Modeling (lcvis.py)

Significantly extended existing Python visualization program to support manual model fitting and statistical analysis of variable star light curves.

Key contributions:
- Developed interactive controls for selecting mathematical models, adjusting fitt parameters, and modifying period used to phase-fold observational data.
- Implemented chi-square calculations to compare fitted models against observed light curves.
- Integrated CSBT fitting functionality directly into Lcvis interface, allowing users to perform automatic fitting and view fitting results alongside manually adjusted models.
- Improved organization and usability of the program through code restructuring and updates to its GUI.

### 2. Light Curve Feature Detection and Physical Parameter Analysis (`csbt.py`)

Enhanced existing Python analysis program by implementing additional methods for identifying, fitting, and characterizing features of eclipsing binary light curves.

Key contributions:
- Implemented moving-average smoothing and SciPy peak detection to identify light curve extrema and improve selection of eclipse regions for fitting.
- Expanded numerical curve-fitting functionality to characterize eclipse features and light curve maxima.
- Added calculations to estimate physical properties of eclipsing binary systems from fitted model parameters.
- Implemented uncertainty propagation using fitted parameter covariance matrices and analytical derivatives to estimate uncertainties in derived physical parameters.

## Technology and Methods

**Programming Language:** Python

**Libraries and Frameworks:**
- NumPy — Numerical computing and array operations
- SciPy — Signal processing, peak detection, and numerical curve fitting
- Matplotlib — Data visualization and plotting
- SymPy — Symbolic mathematics and analytical derivatives
- PyQt5 — Graphical user interface components

**Analytical Methods:**
- Time-series analysis and phase folding
- Moving-average smoothing and peak detection
- Numerical curve fitting and model evaluation
- Chi-square per degree of freedom statistical analysis
- Covariance-based uncertainty estimation and propagation

## Installation

The software was tested using **Python 3.10.14** on macOS.

**1. Clone the repository**

```bash
git clone https://github.com/jjuvan/variable-star-lightcurve-analysis.git
cd variable-star-lightcurve-analysis
```

**2. Create a virtual environment**

Using Python 3.10:

```bash
python3.10 -m venv .venv
```

**3. Activate the virtual environment**

On macOS or Linux:

```bash
source .venv/bin/activate
```

On Windows (Command Prompt):

```cmd
.venv\Scripts\activate.bat
```

**4. Install the required dependencies**

```bash
python -m pip install -r requirements.txt
```

The required Python packages and their tested versions are listed in `requirements.txt`.

**5. Run the analysis software**

Once the dependencies are installed, Lcvis and CSBT can be launched using the commands provided in the sections below.

The virtual environment should remain activated while running the programs.

## Example Analysis

### Interactive Light Curve Visualization and Fitting

The screenshot below demonstrates the interactive Lcvis interface analyzing an eclipsing binary star light curve. The visualization combines observational data, manually adjusted mathematical models, and fitting results from the integrated CSBT analysis program.

![Lcvis interface displaying an eclipsing binary light curve with fitted models and CSBT analysis results](images/lcvis-csbt-analysis.png)

The interface includes:
- **Interactive model adjustment:** Controls for selecting mathematical models, modifying model parameters, and adjusting the plotted period.
- **Integrated fitting analysis:** CSBT fitting results displayed alongside the manually-adjusted Lcvis model.
- **Statistical output:** Chi-square values and fitted parameters for *both* Lcvis and CSBT models, with estimated uncertainties for CSBT fits.
- **Physical parameter estimation:** Calculated estimates of eclipsing binary system properties based on CSBT-fitted light curve features.

### Standalone CSBT Analysis

CSBT can also be utilized as a standalone program, performing the same numerical fitting and analysis of eclipsing binary star light curves as in the Lcvis interface.

The screenshot below demonstrates the analysis of the same variable star shown in the Lcvis example, using the moving-average-based feature detection method.

![Standalone CSBT analysis displaying eclipse fits, fitted maxima, and estimated binary system parameters](images/csbt-standalone-analysis.png)

The visualization demonstrates several analytical capabilities:

- **Feature detection:** Uses moving-average smoothing and peak detection to identify the two minima of the light curve.
- **Eclipse fitting:** Fits parabolic models to the primary and secondary eclipse regions.
- **Maxima fitting:** Fits a squared-sinusoidal model to characterize the light curve's maxima.
- **Statistical evaluation:** Reports chi-square statistics for fitted models and cross-fit comparisons.
- **Uncertainty estimation:** Reports model parameter uncertainties derived from the fitting procedure.
- **Physical parameter estimation:** Calculates estimations of eclipsing binary system properties, including eccentricity, argument of periastron, effective temperature ratio, and an inclination-related oblateness parameter, along with their propagated uncertainties based on fits.

The fitted eclipse curves represent localized mathematical approximations rather than a single global physical model of the binary system.

## Independent Dataset Demonstration — ASAS-SN

To demonstrate the analysis software using observations beyond the original ROTSE-I research dataset, I applied Lcvis and CSBT to publicly accessible photometric observations of **BS Ursae Majoris (BS UMa)** from the All-Sky Automated Survey for Supernovae (ASAS-SN). This demonstration provides an additional example of the software's data preparation, visualization, feature detection, and fitting capabilities using observations from an independent astronomical survey.

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

The script creates a `.dat` file in the current working directory, using the original filename. For example, converting `observations.xlsx` produces `observations.dat`.

The output contains three whitespace-separated numeric columns without a header, suitable for loading into Lcvis.

**3. Analyze the converted observations**

Open the converted `.dat` file in Lcvis and phase-fold the observations using an appropriate period. For the BS UMa demonstration, the ASAS-SN catalog period of approximately 0.3495136 days was used.

Lcvis can also save the phase-folded observations to a separate `.dat` file for subsequent analysis with standalone CSBT.

### Lcvis Visualization and Integrated CSBT Analysis

The ASAS-SN observations were formatted as three-column input data containing observation time, magnitude, and magnitude uncertainty. Lcvis was used to phase-fold the observations, interactively adjust a Periodic Gaussian model, and run CSBT analysis. All of the relevant information regarding both the Lcvis and CSBT fits can be seen to the right of the plot.

![Lcvis analysis of ASAS-SN observations of BS UMa](images/lcvis-csbt-asassn-analysis.png)

### Standalone CSBT Analysis

The phase-folded observations saved by Lcvis were then analyzed using standalone CSBT, with the same moving-average method and a fitting window of 0.15 phase.

![Standalone CSBT analysis of ASAS-SN observations of BS UMa](images/csbt-asassn-standalone-analysis.png)

CSBT finds and fits the primary and secondary eclipse regions separately and evaluates each fitted model against both its corresponding observations and the opposite eclipse. The analysis also includes a fit to the light curve maxima and estimations of binary system parameters with uncertainties.

**Note:** These are exploratory fitting results demonstrating the software's capabilities, not independently validated physical measurements of BS UMa.

## Input Data Formats

Lcvis and standalone CSBT use different input formats.

### Lcvis Input

Lcvis accepts a whitespace-separated `.dat` file containing three numeric columns without a header:

```text
observation_time  magnitude  magnitude_error
```

For the ASAS-SN demonstration, these columns represent Heliocentric Julian Date (HJD), apparent magnitude, and magnitude uncertainty.

Lcvis uses the observation times and a specified period to phase-fold the light curve.

### Standalone CSBT Input

Standalone CSBT requires observations that have already been phase-folded. These can be exported directly from Lcvis.

The input contains three numeric columns:

```text
phase  magnitude  magnitude_error
```

The first column contains phase values rather than observation times.

**Important:** The ASAS-SN conversion script produces input for Lcvis, not standalone CSBT. To use the converted observations with standalone CSBT, first phase-fold and save them using Lcvis.

## Running Lcvis

Lcvis provides an interactive interface for visualizing and analyzing variable-star light curves.

After installing the dependencies listed in `requirements.txt`, launch Lcvis from the repository's root directory:

```bash
python3 src/lcvis.py path/to/observations.dat -p0 [period]
```

Here:

- `path/to/observations.dat` represents the three-column data file generated by `convert_asassn.py`. Replace it with the actual output filename.
- `-p0 [period]` specifies the initial period in days used to phase-fold the observations. Replace `[period]` with your desired value. Default is `1`.

For BS UMa:

```bash
python3 src/lcvis.py observations.dat -p0 0.3495136
```

Lcvis allows users to interactively inspect the phase-folded light curve, adjust fitting models, and run the integrated CSBT analysis.

![Lcvis analysis of ASAS-SN observations of BS UMa](images/lcvis-csbt-asassn-analysis.png)

You can see that there are various models, parameters, sliders, text boxes, and buttons displayed. They are as follows:
- **Arguments:** choose which parameter to adjust in Lcvis, either in phase-folding or in model adjustment.
  - **Period:** phase-fold of the observational data, in days.
  - **Amplitude:** amplitude of the model.
  - **Model X-Shift**: horizontal shift of the model.
  - **Model Y-Shift**: vertical shift of the model (note the inverted Y-axis to reflect that dimmer magnitudes are more positive).
  - **Full Width at Half Max:** specific to Periodic Gaussian model, controls the FWHM of the function.
- **Models:** choose a model to fit to the observational data.
  - **Sine, 1 Cycle per Phase**
  - **Sine, 2 Cycles per Phase**
  - **Absolute Sine**
  - **Periodic Gaussian** (repeats every 0.5 phase)
- **Parameter Slider (long slider):** scroll through the selected argument at a certain stepsize.
- **Minima x^2 Width (short slider):** set the window size for chi-square calculations, sampling observations only within those regions.
- **2x Period:** double the plot's current period.
- **1/2x Period:** halve the plot's current period.
- **+[Parameter]:** increase the parameter by one stepsize.
- **-[Parameter]:** decrease the parameter by one stepsize.
- **[Parameter] Max:** set the parameter's max value for the slider for fine-tuning.
- **[Parameter] Min:** set the parameter's min value for the slider for fine-tuning.
- **[Parameter] Stepsize:** set the parameter's stepsize value for the slider and +/- buttons.
- **Magnitude Max:** set the plot's maximum magnitude.
- **Magnitude Min:** set the plot's minimum magnitude.
- **Magnitude Range:** set the plot's magnitude range around the center of the plot.
- **Save:** save the plot. Choose between the phased data (`.dat`) or an interactive plot image (`.pkl`). For the plot, you can choose to save no models, Lcvis model only, CSBT model only (if displayed), or both. Can choose to overwrite files with the same name if desired, otherwise file names will tack on a `_dupe` extension with a unique number.
- **Run csbt.py:** run CSBT in the Lcvis interface. Choose the method, number of points for the method, and window size of the eclipses.
- **Clear CSBT Output:** clear the current CSBT output.

At the very bottom of the window are the current selected parameter, its min/max slider values, and its current stepsize, as well as where the observational data is centered at in the plot.

To the right of the plot contains all of the information, including:
- Lcvis model equation and current parameter values
- Lcvis chi-square calculations
- Phase-folded period
- Plot Y-axis information
- CSBT output, with input parameters, including:
  - Fit equations for each minimum and the maxima, as well as parameter uncertainties
  - Chi-square calculations for corresponding observational data and cross-fits
  - Binary parameters with uncertainties

If you save a `.pkl` file, you can re-open the file using `unpickle.py`:

```bash
python3 scripts/unpickle.py /path/to/lcvis_data.dat
```

Note that in order to run CSBT in the Lcvis window, `lcvis.py` and `csbt.py` **must** remain in the same directory because Lcvis imports functionality from CSBT to perform integrated light-curve analysis. Both programs are provided in the repository's `src/` directory. When running Lcvis, preserve this directory structure.

The phase-folded observations can also be saved as a separate `.dat` file for use with standalone CSBT.

## Running Standalone CSBT

CSBT can be run independently of Lcvis to analyze previously phase-folded light curves.

Unlike Lcvis, which accepts observation times and performs phase folding, standalone CSBT requires a `.dat` file containing phase-folded observations, which can be saved directly from Lcvis.

After saving the phase-folded observations from Lcvis, run the following command from the repository's root directory:

```bash
python3 src/csbt.py path/to/observations_lcvis.dat -m [method] -w [window] -n [num_points] -p [show_plot]
```

Replace `observations_lcvis.dat` with the actual filename saved by Lcvis.

**Arguments:**

- `-m [method]`: Select method to identify light-curve extrema. Choose between `move_avg` and `low_mags`. Default is `move_avg`.
- `-w [window]`: Sets the fitting window width, in phase units, for identifying and fitting light-curve minima. Default is `0.10`. 
- `-n [num_points]`: Sets how many points are used for sampling in determining moving average or lowest magnitudes. Default is `20`.
- `-p [show_plot]`: Show output plot. Default is `True`.

Different datasets may require adjustments to the fitting parameters.

For BS UMa:

```bash
python3 src/csbt.py observations_lcvis.dat -m move_avg -w 0.15
```

![Standalone CSBT analysis of ASAS-SN observations of BS UMa](images/csbt-asassn-standalone-analysis.png)

CSBT fits the primary and secondary eclipse regions and the light-curve maxima. It also calculates fitting statistics and estimates binary-system parameters with associated uncertainties. This information is the *same* as the reported information in Lcvis, so long as the same data and input parameters are provided.

## Development History

This repository contains selected programs from the collaborative [ROTSEANA research project](https://github.com/rotsehub/rotseana). My contributions were developed through multiple iterations, including feature additions, bug fixes, and revisions to existing analysis software.

The following Pull Requests document two of my major contributions to the original repository.

### [Pull Request #40 — CSBT Enhancements](https://github.com/rotsehub/rotseana/pull/40)

- Introduced moving-average-based feature detection to improve the identification of light curve extrema.
- Expanded the program's numerical analysis and reporting capabilities.

### [Pull Request #45 — Lcvis and CSBT Revisions](https://github.com/rotsehub/rotseana/pull/45)

- Restructured `lcvis.py` to reduce reliance on nested functions and improve code organization.
- Updated the GUI to use PyQt5 for dialog windows.
- Expanded interactive model selection, parameter adjustment, and period controls.
- Integrated CSBT fitting functionality into the Lcvis visualization interface.
- Improved saving functionality for analysis results and plots.
- Expanded CSBT analysis to include fitting of light curve maxima, physical parameter estimation, and uncertainty calculations.

These Pull Requests provide additional documentation of the implementation and evolution of the research software.

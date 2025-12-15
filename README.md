# 🌌 Gaia Analyzer

A complete end-to-end pipeline for querying Gaia DR3 stars, generating HR diagrams, performing clustering, cross-matching with TESS observations, analyzing light curves, and estimating stellar parameters.

This project serves as a compact research toolkit for stellar astrophysics, Gaia–TESS data science, and time-series analysis.

---

## ✨ Overview

**Gaia Analyzer** provides a unified workflow to:

- Query **Gaia DR3** data using astroquery  
- Visualize the **Hertzsprung–Russell (HR) diagram**  
- Perform **machine learning clustering** (K-Means, DBSCAN)  
- Cross-match **Gaia → DR2 → TIC**  
- Download and analyze **TESS light curves**  
- Perform **Lomb–Scargle period analysis**  
- Generate **phase-folded light curves**  
- Compute **stellar parameters** such as temperature, luminosity, radius, mass, and approximate age  

---

## 🚀 Features

### ⭐ Gaia DR3 Query Tools
- Query stars by **source_id**, magnitude range, or sky region  
- Clean and filter Gaia data  
- Compute **parallax-based distance**  
- Derive **absolute magnitude (M_G)**  

---

### ⭐ HR Diagram Module
- HR diagram using Gaia BP–RP vs. M_G  
- Temperature-colored diagrams  
- Density maps  
- Optional region labels and stylistic enhancements  

---

### ⭐ Machine Learning (Module 1)
- Feature engineering (color index, absolute magnitude)  
- Standardization + PCA  
- **K-Means** clustering  
- **DBSCAN** clustering (identifies white dwarfs and outliers)  
- Cluster-labeled HR diagrams  

---

### ⭐ Gaia ⇨ TESS Crossmatch (Module 2)
- Convert **Gaia DR3 → DR2 → TIC**  
- Find matching TESS sources  
- Download **PDCSAP light curves** using Lightkurve  
- Generate:
  - Raw light curve  
  - Cleaned/detrended light curve  
  - Lomb–Scargle periodogram  
  - Phase-folded light curve  

---

### ⭐ Stellar Parameter Estimation (Module 3)
Based on Gaia photometry and empirical relations:

- Effective Temperature (Teff)  
- Luminosity (L/L☉)  
- Radius (R/R☉)  
- Mass (M/M☉)  
- Approximate age estimate  

---
## 📊 HR Diagrams

### 1️⃣ Basic HR Diagram
<img src="docs/example_plots/hr_basic.png" width="500">

### 2️⃣ Temperature-Colored HR Diagram
<img src="docs/example_plots/hr_temperature.png" width="500">

### 3️⃣ KDE Density HR Diagram
<img src="docs/example_plots/hr_density_kde.png" width="500">

### 4️⃣ Stellar Regions HR Diagram
<img src="docs/example_plots/hr_stellar_regions.png" width="500">

### 5️⃣ Distance-Colored HR Diagram
<img src="docs/example_plots/hr_distance.png" width="500">





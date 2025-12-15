#  Gaia Stellar Analyzer

A complete mini–pipeline for exploring stellar populations using **Gaia photometry** and analyzing stellar variability with **TESS light curves**.  
The project includes HR diagram construction, clustering methods, period detection, and phase-folded light curve visualization.



# Gaia HR Diagram Analysis

##  K-Means Clustering
Identifies major stellar groups (main sequence, red giants, etc.) in BP–RP vs. absolute magnitude space.

<img src="docs/hr_kmeans.png" width="500">



##  DBSCAN Clustering
Density-based clustering reveals dense stellar groups while naturally ignoring outliers.

<img src="docs/hr_dbscan.png" width="500">



#  TESS Light Curve Analysis

##  Raw TESS Light Curve
Unprocessed brightness variations from TESS.

<img src="docs/tess_raw_lightcurve.png" width="600">



## Detrended TESS Light Curve
Removes long-term trends and prepares the data for period analysis.

<img src="docs/tess_detrended_lightcurve.png" width="600">



# Period Search

##  Lomb–Scargle Periodogram
Primary period detection over a standard frequency range.

<img src="docs/tess_periodogram.png" width="600">



## Wide-Range Periodogram
Explores long periods (0–1500 days), useful when searching for slow variability.

<img src="docs/tess_periodogram_alt.png" width="600">



## Filtered (Short-Period) Periodogram
Focuses on short periods (0–100 days) to identify fast variability.

<img src="docs/tess_periodogram_filtered.png" width="600">



#  Phase-Folded Light Curves

##  Phase-Folded Light Curve (P = 0.00136 days)
Displays periodic modulation using the strongest short-period peak.

<img src="docs/tess_phase_folded.png" width="600">



##  Phase-Folded Light Curve (P = 0.07885 days)
An additional candidate period revealed in the wide-range search.

<img src="docs/tess_phase_folded_0.07885d.png" width="600">



#  Summary

This project demonstrates:
- How to build HR diagrams from Gaia DR3
- How to classify stars using unsupervised ML (K-Means, DBSCAN)
- How to extract and clean TESS light curves
- How to detect stellar variability using Lomb–Scargle periodograms
- How to visualize periodicity through phase-folded light curves

It serves as a compact, reproducible stellar-analysis pipeline suitable for learning, exploration, and future scientific development.





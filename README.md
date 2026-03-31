# SP2026-FP01-Ice-Sheet-Velocity
Exploring the ice sheet velocity change of Whillans Ice Plain, West Antarctica between 2008 and 2019.

## Project Title:  Ice Sheet Velocity Change at Whillans Ice Plain
## Name(s) & Handles: 
- Kaitlyn Sanchez - K-Sanchez126
- Emilia Orta - emiliaorta
- Kadidia Mariko -  kamam203

## Short Summary: 
- This project will explore how the velocity of the Whillans Ice Plain in West Antarctica changed between 2008 and 2019 using remote sensing data, such as SAR and optical imagery from multiple satellites. The primary output will be figures showing the spatial and temporal patterns of velocity, as well as any correlations between velocity change and tidal forcings and between velocity change and the timing of stick-slip events.

## Introduction:
![Ice Study Location](images/IceStudyLocation.gif) 
&#9; Whillans Ice Plain (WIP) is the lower part of the Mercer and Whillans ice stream in West Antarctica. It drains from the interior ice of the West Antarctic Ice Sheet onto the Ross Ice Shelf[1]. Ice changes in Antarctica are usually due to activity in the ice streams, and understanding the conditions that lead to different ice stream acceleration changes helps to determine how sea level may change in the future. Both deceleration and stick-slip motion of the ice stream could cause it to stagnate (as seen in nearby streams like Kamb). Significant changes in Whillans ice stream speak to the stabilization of the West Antarctica ice sheet and how sea level rise will be affected going forward [3-7].

&#9; Rather than being governed by continuous flow, one of the drivers of the motion is stick-slip events. These events cause the ice sheet to move forward by about 0.2-0.6 m in about 30-60 minutes, either once or twice a day, depending on the tidal features. Namely, in order to have a secondary slip in a day, there must be a low-moderate tide height and a semi-diurnal tidal cycle [3].Examination of the long-term velocity time series shows that the deceleration is not occurring at a steady rate but varies on smaller time scales. Additionally, based on point location measurements, the velocity deceleration is non-uniform across the ice sheet as well as through time[2] . The spatial and temporal resolution over time determines how ice is moving in the interior of the ice stream and at the margins. Having constraints of this motion beyond just the point measurements we currently have allows us to better estimate how the Whillans ice stream motion will behave in the future, which is a factor involved in sea-level rise and how climate change impacts the cryosphere [1].

&#9; Based on current GPs records and a catalog of stick-slip events, it is expected to find that Whillians deceleration varies through time (such as on interannual timescales) and that this variability also varies spatially. There are currently GNSS-derived average velocities that show the velocity is correlated with tidal forces. The derived velocities from ITS_LIVE should also show these tidal forcing, and time heterogeneities and also show the spatial variability which is not currently clear. [3-6].

&#9;
  Using remote sensing data to look at the velocity changes over time provides greater insight as to how the velocity change has varied spatially. Additionally, this project aims to make connections between velocity changes, tidal forcings, and the timing of stick-slip events. 

## Problem Statement: 
- Although GPS studies have shown at specific locations that ice sheet velocity at Whillans Ice Stream has slowed, how that deceleration has changed over the full ice sheet, how the velocity fluctuates across different time scales, and if there is a correlation between the velocity change and stick-slip events and tidal forcings, is still not well documented.

## Questions the Project Will Answer:
- Are there detectable relationships between ice surface velocity, timing of stick-slip events, and tidal forcings?
- How has the temporal variability of ice surface velocity changed between 2008 and 2019, and how does it vary on seasonal/decadal timescales?
-What are the spatial patterns of ice surface velocity/how does the magnitude of velocity slowing vary between different features of the ice sheet (such as the grounding zone, the middle of the ice sheet, and the margins). 
 
## Objectives:
- Clean and analyze velocity from ITS_LIVE time series across Whillans Ice Plain to produce figures that show how velocity has changed over time and space.
-Identify correlations between velocity, tidal forcings, and stick-slip timings.

## Tools/Packages: 
- Itslive-py
- Xarray
- Pyproj 
- Scipy 
- Pandas 
- Numpy
- Matplotlib 
- Cartopy


One line is plotted for each axis, and they are color-coated

# Project Methodology and Outcomes

## Planned Methodology
Based on the GPS station locations used for the tidal features present in another dataset (Kaitlyn’s icequake project), determine the spatial region that will be used for looking at the velocities. Then, using **EarthData** and **ITS_LIVE**, open the relevant datacube tiles.

## Data Collection & Processing
* **Velocity Field:** Get the full velocity field across the region of interest for all available timestamps between 2008-2019 to create a spatiotemporal array.
* **Data Cleaning:** 
    * Remove filler values and incorrect data points.
    * Drop measurements with component uncertainties above a certain threshold (e.g., 50 m/yr).
* **Spatial Mapping:** Create maps of average velocity and velocity trends (linear slope) for each grid cell.
* **Point Time Series:** Extract at GPS locations by reprojecting coordinates to the Antarctic polar stereographic coordinate system.
* **Interpolation:** Adjust data to match the temporal resolution of the tidal data set.
* **Analysis:** Look at temporal variability using trends, rolling means, and standard deviations.
* **Correlations:** Perform correlations between the velocity time series.

## Expected Outcomes & Observations
* The velocity is decreasing over time and is non-uniform across the ice plain.
* Velocity acceleration changes are correlated with the timing of stick-slip events and tidal forcings.

## Proposed Figures
1. **Figure 1 (Spatial Velocity):** Two plots: a bar chart of velocity vs GPS station coordinates and a line graph of velocity over time (years).
2. **Figure 2 (Slip Prediction):** Scatter plot of 30-day prior mean vs time-to-next-slip, color-coded by record position.
3. **Figure 3 (Heatmap):** Velocity correlation with other features.
4. **Figure 4 (Prediction Accuracy):** True vs. predicted time-to-next-slip (with/without velocity feature).
5. **Figure 5 (Time Series):** Two-axis plot of velocity and rolling mean slip occurrence over time.

##References:
[1]
S. P. Carter, H. A. Fricker, and M. R. Siegfried, “Evidence of rapid subglacial water piracy under Whillans Ice Stream, West Antarctica,” Journal of Glaciology, vol. 59, no. 218, pp. 1147–1162, 2013, doi: https://doi.org/10.3189/2013jog13j085.
[2]
R. Bindschadler, P. Vornberger, and L. Gray, “Changes in the ice plain of Whillans Ice Stream, West Antarctica,” Journal of Glaciology, vol. 51, no. 175, pp. 620–636, 2005, doi: https://doi.org/10.3189/172756505781829070.
[3]
J. P. Winberry, S. Anandakrishnan, R. B. Alley, D. A. Wiens, and M. J. Pratt, “Tidal pacing, skipped slips and the slowdown of Whillans Ice Stream, Antarctica,” Journal of Glaciology, vol. 60, no. 222, pp. 795–807, 2014, doi: https://doi.org/10.3189/2014jog14j038.
[4]
A. S. Gardner et al., “ITS_LIVE global glacier velocity data in near-real time,” The cryosphere, vol. 19, no. 9, pp. 3517–3533, Sep. 2025, doi: https://doi.org/10.5194/tc-19-3517-2025.
[5]
Z. S. Katz, M. R. Siegfried, and L. Padman, “Slip‐Event Timing and Ice Velocity Vary at Long‐Period Ocean Tidal Frequencies at Whillans Ice Plain, West Antarctica,” Journal of Geophysical Research: Earth Surface, vol. 131, no. 1, Jan. 2026, doi: https://doi.org/10.1029/2025jf008770.
[6]
B. P. Lipovsky and E. M. Dunham, “Slow‐slip events on the Whillans Ice Plain, Antarctica, described using rate‐and‐state friction as an ice stream sliding law,” Journal of Geophysical Research Earth Surface, vol. 122, no. 4, pp. 973–1003, Apr. 2017, doi: https://doi.org/10.1002/2016jf004183.
[7]
M. Dirscherl, A. J. Dietz, S. Dech, and C. Kuenzer, “Remote sensing of ice motion in Antarctica – A review,” Remote Sensing of Environment, vol. 237, p. 111595, Feb. 2020, doi: https://doi.org/10.1016/j.rse.2019.111595.
[8]
G. Guerin, Aurélien Mordret, D. Rivet, B. P. Lipovsky, and B. M. Minchew, “Frictional Origin of Slip Events of the Whillans Ice Stream, Antarctica,” Geophysical Research Letters, vol. 48, no. 11, Jun. 2021, doi: https://doi.org/10.1029/2021gl092950.



 

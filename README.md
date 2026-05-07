# SP2026-FP01-Ice-Sheet-Velocity
Exploring the temporal and spatial variability in  ice sheet velocity change of Whillans Ice Plain, West Antarctica between 2008 and 2019.

## Project Title:  Ice Sheet Velocity Change at Whillans Ice Plain
## Name(s) & Handles: 
- Kaitlyn Sanchez - K-Sanchez126
- Emilia Orta - emiliaorta
- Kadidia Mariko -  kamam203

## Short Summary: 
- This project will explore how the velocity of the Whillans Ice Plain in West Antarctica changed between 2008 and 2019, as well as how it changed spatially using GPS and GNSS data. The primary output is figures that show preprocessing changes, the spatial and temporal patterns of velocity, and correlations between velocity change stick-slip events.

## How to Use Repository: 
 &nbsp; The main code for this workflow can be found in the Notebooks folder in the extract_and_preproc notebook. In order to run it, the PPP.zip file will need to be downloaded from the Katz et al., 2026 Zenodo. The file should then be extracted and placed in a Data folder in the SP2026-FP01-Ice-Sheet-Velocity directory. Adjust the directory such that the path configuration is accurate: PPP_dir = "../Data/PPP/PPP/". Another required file is StationInformation.csv, which should also be downloaded from the same Zenodo repository and placed in the Data folder, as it contains the GNSS station coordinate metadata used for the station location maps and spatial station ordering in Figures 2 and 4. Additionally, in order to get the preprocessed stick-slip catalog, the Whillians-GPS-Data-and-Features.csv should be downloaded from the Mines Glaciology Github and put in the same file folder. The script in the extract notebook is fully contained. Once it runs, the figure notebooks can be run in any order. Each figure notebook takes inputs that are generated from the extraction notebook and outputs figures in the figure file. It is worth noting that the extraction notebook has a run time of about 3 hours, however, the cleaned and preprocessed data is save to a csv in the data directory so that any figure can be generated and edited without having to rerun that notebook more than once.   

## Introduction:
![Ice Study Location](images/IceStudyLocation.gif)
Figure demonstrating location of Whillans Ice Plain [1]. 
 
&nbsp; Whillans Ice Plain (WIP) is the lower part of the Mercer and Whillans ice stream in West Antarctica. It drains from the interior ice of the West Antarctic Ice Sheet onto the Ross Ice Shelf[1]. Ice changes in Antarctica are usually due to activity in the ice streams, and understanding the conditions that lead to different ice stream acceleration changes helps to determine how sea level may change in the future. Both deceleration and stick-slip motion of the ice stream could cause it to stagnate (as seen in nearby streams like Kamb). Significant changes in Whillans ice stream speak to the stabilization of the West Antarctica ice sheet and how sea level rise will be affected going forward [3-7].

 &nbsp;  Rather than being governed by continuous flow, one of the drivers of the motion is stick-slip events. These events cause the ice sheet to move forward by about 0.2-0.6 m in about 30-60 minutes, either once or twice a day, depending on the tidal features. Namely, in order to have a secondary slip in a day, there must be a low-moderate tide height and a semi-diurnal tidal cycle [3].
 
 &nbsp;  Since the spatial and temporal resolution over time determines how ice is moving in the interior of the ice stream and at the margins, having better constraints of this motion would allow us to better estimate how the Whillans ice stream motion will behave in the future[1].

 &nbsp;  Based on current GPS records and a catalog of stick-slip events, it is expected to find that Whillians deceleration varies through time (such as on interannual timescales) and that the velocity varies spatially across features such as the grounding line and grounded versus floating ice [3-6].
 
## Research Questions: 
- How does the ice sheet velocity vary across Whillans Ice Plain on a decadal time scale?

- How is the temporal variation in ice sheet velocity correlated to the amount of 12 versus 24-hour slip events that occur? 
  
- Objectives:
  - Compute and clean velocity from PPP files derived from GNSS data at various GPS locations across Whillans Ice Plain to produce figures that show how velocity has changed over time and space.
  - Identify correlations between velocity and stick-slip timings.

## Datasets:
- Whillans Ice Plain GNSS RINEX, Kinematic Positions, Stick-Slip Event Catalog, and Station Metadata [PPP Files and Station Metadata from Zenodo](https://zenodo.org/records/17797751)
- Whillans Ice Plain Stick Slip Events [Event catalog](https://github.com/MinesGlaciology/whillans-surf/blob/main/notebooks/data_preproc/09-18.csv)

## Tools/Packages: 
- Os [Os](https://docs.python.org/3/library/os.html)
- Pyproj [Pyproj](https://pyproj4.github.io/pyproj/latest/)
- Scipy [Scipy](https://docs.scipy.org/doc/scipy/)
- Pandas [Pandas](https://pypi.org/project/pandas/#documentation)
- Numpy [Numpy](https://numpy.org/)
- Matplotlib [Matplotlib](https://matplotlib.org/)
- Cartopy [Cartopy](https://cartopy.readthedocs.io/stable/)
- Glob [Glob](https://docs.python.org/3/library/glob.html)



## Planned Methodology
- Based on the GPS station locations used for the tidal features present in (Katz et al., 2026) determine the spatial region that will be used for looking at the velocities. Then, use the precise point positioning files to compute the velocity. 
- Get the PPP file into a cleaned data frame of GPS epochs using the backward and forward passes as position estimates to construct the decimal lat and long from the degree-minute-seconds column, and apply a filter based on the position RMS to limit noise 
- Project the coordinates from lat, lon to Antarctic polar stereographic coordinates 
- Create daily background/time series velocity 
- Loop over every station and then concatenate it into one file 
- Use the daily velocity estimates in a 30-day window to compute a median value for each station for each of the icequakes 
- Create figures that tell the story of this data 
  - Show why smoothing with the 30-day median shows useful signal 
  - Creating a time series of the background velocity with spatial coordinates/cartopy in the background  
  - Show different smoothing techniques to clean the background velocity data 
  - Plot of velocity time series (one for each station)
  - Plot how the change in velocity corresponds to the stick-slip events 

## Results Summary: 
 &nbsp; The 30-day smoothed velocity records show a deceleration of Whillans Ice Plain across the observation period. Figures 4 and 5 both show that overall the velocity was considerably higher in the early part of the record (2008-2011) than by the end (2017-2018). However, this slowdown is not uniform across the ice plain. Figure 2 shows that gz-series stations near the western margin consistently record the highest velocities, while la- and mg-series stations further into the interior record lower velocities throughout. The spatial gradient visible in Figure 2's map panel is consistent with ice flowing fastest near the margins. Importantly, the deceleration appears across all station locations rather than localized to any one part of the ice plain, suggesting an overarching change in the ice stream over this period.

 &nbsp; Figure 5 shows how velocity and slip timing relate to each other inversely. The 30-day median time to the next slip event aligns with the velocity through the early part of the record, with both showing similar low-frequency variability between 2008 and roughly 2014. After around 2015, the two series begin to diverge. As velocity declines, the time between slip events becomes longer and more variable. This is consistent with a shift toward longer-period slip recurrence as the ice stream slows, since a slower-moving ice stream takes longer to build up the stress needed to trigger the next slip event. This suggests that the decadal slowdown may have shifted the slip cycle away from shorter semi-diurnal recurrence and toward longer diurnal recurrence over the observation period.

## Contribution Statement: 
- Kaitlyn: Extraction and preprocessing, project introduction, slideshow, figure 1 and 3 interpretation, findings analysis, README final requirements, repository formatting  
- Emilia: Figure 2, 4, and 5 and the corresponding interpretation, repository clean up, and README picture 
- Kadidia: Stats, exploratory figures, Figure 1 and 3, and initial README updates  

## Anticipated Challenges: 
- We were originally going to use ITS_LIVE velocity data derived from Sentinel-1. However, there was a gap in coverage for this region of Antarctica during the 2008-2019 time range. Therefore, we had to pivot to backing out the velocity from the PPP files based on GNSS data instead.
- The positions from the PPP were taken at 15 second intervals, so deriving the velocity was too noisy to capture meaninful long term signals. 

## References:
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



 

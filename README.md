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
     Whillans Ice Plain (WIP) is the lower part of the Mercer and Whillans ice stream in West Antarctica. It drains from the interior ice of the West Antarctic Ice Sheet onto the Ross Ice Shelf. Ice changes in Antarctica are usually due to activity in the ice streams, and understanding the conditions that lead to different ice stream acceleration changes helps to determine how sea level may change in the future. Both deceleration and stick-slip motion of the ice stream could cause it to stagnate (as seen in nearby streams like Kamb). Significant changes in Whillans ice stream speak to the stabilization of the West Antarctica ice sheet and how sea level rise will be affected going forward [1-4].

    Rather than being governed by continuous flow, one of the drivers of the motion is stick-slip events. These events cause the ice sheet to move forward by about 0.2-0.6 m in about 30-60 minutes, either once or twice a day, depending on the tidal features. Namely, in order to have a secondary slip in a day, there must be a low-moderate tide height and a semi-diurnal tidal cycle [Zach’s paper].Examination of the long-term velocity time series shows that the deceleration is not occurring at a steady rate but varies on smaller time scales. Additionally, based on point location measurements, the velocity deceleration is non-uniform across the ice sheet as well as through time. The spatial and temporal resolution over time determines how ice is moving in the interior of the ice stream and at the margins. Having constraints of this motion beyond just the point measurements we currently have allows us to better estimate how the Whillans ice stream motion will behave in the future, which is a factor involved in sea-level rise and how climate change impacts the cryosphere [paper above].

    Based on current GPs records and a catalog of stick-slip events, it is expected to find that Whillians deceleration varies through time (such as on interannual timescales) and that this variability also varies spatially. There are currently GNSS-derived average velocities that show the velocity is correlated with tidal forces. The derived velocities from ITS_LIVE should also show these tidal forcing, and time heterogeneities and also show the spatial variability which is not currently clear. [refs 1-3].

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




 

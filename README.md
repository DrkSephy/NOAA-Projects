NOAA-Projects
-------------

This repository contains source code of various projects I work on as a Graduate researcher at the City College of New York inside of 
[G.L.A.S.S LAB](https://bitbucket.org/glasslab/profile/members). My tasks involve creating web applications for [NOAA-CREST](http://crest.ccny.cuny.edu/) and subsequently [NOAA](http://www.noaa.gov/).

Completed Works
---------------

NOAA SQUAM Granule Visualization
--------------------------------

One of NOAA's web products is the [SST Quality Monitor](http://www.star.nesdis.noaa.gov/sod/sst/squam/HR/index.html#), which maps sea-surface temperature across the globe through granules (images) provided by two satellites which sweep the globe. From the scale below each satellite image, we can see the agreement/disagreement of data, marked by shades of blue and purple.

![alt tag](https://github.com/DrkSephy/NOAA-Projects/blob/master/img/squam.png)

 My task was to write scripts and provide JavaScript which would allow users to hover over regions of the globe and display the corresponding granule. To do so, I used [d3](http://d3js.org/) to build a [voronoi diagram](http://en.wikipedia.org/wiki/Voronoi_diagram). The input to these voronoi diagrams are the computed `latitude` and `longitude` centers of each granule for all regions of the Earth, which in turn builds a set of SVG polygons. 

 ![alt tag](https://github.com/DrkSephy/NOAA-Projects/blob/master/img/squam.gif)

 Voronoi diagrams allow the user to determine which region they are currently in by computing the centers of all polygons, which are also computed inside of a JSON file containing the `image` and `ID` associated with each `polygon/region`. By attaching event handlers to these polygons through D3, the user can hover over each area and see the corresponding granule. By clicking on the region, the granule opens in a new tab with higher resolution. 

LICENSE
-------

The actual images used in any of the demos presented here are not contained within this repository, as they are not part of the public domain. The only source code listed on this page are those that are written myself and are seperate from [NOAA](http://www.noaa.gov/) and [NOAA-CREST](http://crest.ccny.cuny.edu/). 

As such, the JavaScript and conversion files may be useful for those interested in Voronoi diagram generation using D3. All **source code** is licensed under the [MIT License](https://github.com/DrkSephy/NOAA-Projects/blob/master/LICENSE.txt). If any part of this source code is reused, a link back to [my github profile](https://github.com/DrkSephy) would be appreciated. 



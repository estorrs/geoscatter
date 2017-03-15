# geoscatter

**A python API for adding points and heatmaps to a map.**

## Usage

First we import the GeoScatter and GeoPoint classes from geoscatter

```python
from geoscatter.GeoScatter import GeoScatter
from geoscatter.GeoScatter import GeoPoint
```

To use geoscatter, you will need a Google Static Maps API key.  It's quick and free, just go [here](https://developers.google.com/maps/documentation/static-maps/) and click *Get A Key* in the top right corner of the page. 
```python
googleMapsApiKey = "INSERT YOUR API KEY HERE!!"
```

To begin, we define our map.  To do this we specify the center of the map by creating a GeoPoint containing the latitude and longitude of the center coordinate (Columbia, Mo in this case).  We can also specify a zoom level between 1 and 20 and the size of the map in pixels.  A quick note on map size, if a size below 150 or above 600, good results can't be guaranteed. Additionally you have the ability to choose to get a map with or without labels.   
```python
cLat = 38.536178
cLon = -92.302498
center = GeoPoint(cLat, cLon)

gs = GeoScatter(googleMapsApiKey, center, zoom = 3, imgSize = 600, mapLabels=False)
```

### Adding points

Before we add some points to our map, I'd like to take a moment to say the dataset I'll be using in these examples are the starting location of all US tornado tracks since 1950 (National Weather Service) and all significant global earthquakes since 2500 B.C. (USGS). 

There are multiple ways we can add points to our map.  First we can add points by file.  The file format must have two fields.  This first field is the point latitude and the second is the longitude.  The fields can be separated by either a comma or tab.  So both latitude,longitude and latitude	longitude are acceptable. 

Lets plot all tornadoes in the United States since 1950. 
```python
gs.addPoints("../example_data/tornado_locations.csv", s =.5, alpha = .4, c = 'r', marker='o')
```
![GitHub Logo](/images/tornadoes/all_tornadoes.png)

We can also change the point shape, size, color, and transparency.  It's messy but here we plot the tornadoes in Missouri as 10 pixel wide blue triangles with no transparency.  For more about [marker](http://matplotlib.org/api/markers_api.html) and [color](https://matplotlib.org/api/colors_api.html) see matplotlib's documentation.
```python
gs = GeoScatter(googleMapsApiKey, center, zoom=7, imgSize = 600, mapLabels=False)
gs.addPoints("../example_data/tornado_locations.csv", s =10, alpha = 1.0, c = 'b', marker='v')
```
![GitHub Logo](/images/tornadoes/missouri_tornadoes_notransparency.png)

What if we wan't to points in the same dataset to be different sizes?  We can do that.  Another way we can add points by file is to use a file that has three fields.  The first two fields are the points latitude and the points longitude.  The third field is the point size.  The fields can be separated by commas or tabs. 

Here we plot the same tornadoes, but the size of the point corresponds to the number of deaths the tornado caused. 
```python
gs = GeoScatter(googleMapsApiKey, center, zoom = 7, imgSize = 600, mapLabels=False)
gs.addPoints("../example_data/tornadoes_deaths.csv", s =1, alpha = .4, c = 'r', marker='o')
```
![GitHub Logo](/images/tornadoes/missouri_tornadoes_deaths.png)

When we add points this way, the size parameter becomes a scalar.  So for instance, if we want to make the points 3X larger, we can do that. 

```python 
gs = GeoScatter(googleMapsApiKey, center, zoom = 7, imgSize = 600, mapLabels=False)
gs.addPoints("../example_data/tornadoes_deaths.csv", s =3, alpha = .4, c = 'r', marker='o')
```
![GitHub Logo](/images/tornadoes/missouri_tornadoes_deaths_s3.png)

### Adding heatmaps

We can also add heatmaps to our map.  First we create a map of all *"significant"* earthquakes in the past 4500 years.  

```python
cLat = 0
cLon = 0
center = GeoPoint(cLat, cLon)
gs = GeoScatter(googleMapsApiKey, center, zoom = 1, imgSize = 600, mapLabels=False)
gs.addPoints("../example_data/earthquake_locations.csv", s =5, alpha = 1.0, c = '#FFFF00', marker='s')
```
![GitHub Logo](/images/earthquakes/all_earthquakes.png)

Now we add a heatmap.  A brief warning that when the quantity of points starts to get into the thousands you may have to wait a few seconds for the heatmap to generate.  And even longer if you are using more points than that. 
```python
gs.addHeatmap(colorscheme = "coolwarm", bw=25.0, alpha=.4)
```
![GitHub Logo](/images/earthquakes/all_earthquakes_heatmap.png)

The heatmap bandwidth can also be changed. The bandwidth is a parameter that controls the smoothness of the heatmap.  Therefore, a larger bandwidth will result in a more homogenous heatmap.  

Here we zoom in on California and use a bandwidth of 10.0. 

```python
cLat = 39.140328
cLon = -120.034881
center = GeoPoint(cLat, cLon)
gs = GeoScatter(googleMapsApiKey, center, zoom = 5, imgSize = 600, mapLabels=False)
gs.addPoints("../example_data/earthquake_locations.csv", s =5, alpha = 1.0, c = '#FFFF00', marker='s')
gs.addHeatmap(colorscheme = "coolwarm", bw=10.0, alpha=.4)
```
![GitHub Logo](/images/earthquakes/california_earthquakes_heatmap_bw10.png)

And a bandwidth of 100.0. 

```python
gs = GeoScatter(googleMapsApiKey, center, zoom = 5, imgSize = 600, mapLabels=False)
gs.addPoints("../example_data/earthquake_locations.csv", s =5, alpha = 1.0, c = '#FFFF00', marker='s')
gs.addHeatmap(colorscheme = "coolwarm", bw=100.0, alpha=.4)
```
![GitHub Logo](/images/earthquakes/california_earthquakes_heatmap_bw100.png)

We can also alter the colorscheme. For more on [colorschemes](http://matplotlib.org/examples/color/colormaps_reference.html) visit matplotlib's documentation. 

```python
gs = GeoScatter(googleMapsApiKey, center, zoom = 5, imgSize = 600, mapLabels=False)
gs.addPoints("../example_data/earthquake_locations.csv", s =5, alpha = 1.0, c = '#FFFF00', marker='s')
gs.addHeatmap(colorscheme = "Reds", bw=25.0, alpha=.4)
```
![GitHub Logo](/images/earthquakes/california_earthquake_heatmap_reds.png)

### Adding multiple datasets

Multiple sets of points can also be plotted.  Here we plot both earthquakes (blue for better contrast) and tornadoes.  

```python 
cLat = 36.157467
cLon = -120.862654
center = GeoPoint(cLat, cLon)
gs = GeoScatter(googleMapsApiKey, center, zoom = 6, imgSize = 600, mapLabels=False)
gs.addPoints("../example_data/earthquake_locations.csv", s =5, alpha = 1.0, c = 'b', marker='s')
gs.addPoints("../example_data/tornado_locations.csv", s=5, alpha = 1.0, c = 'r', marker='v')
```
![GitHub Logo](/images/earthquakes/california_earthquakes_tornadoes.png)

We can also do separate heatmaps. 

```python
gs = GeoScatter(googleMapsApiKey, center, zoom = 6, imgSize = 600, mapLabels=False)
gs.addPoints("../example_data/earthquake_locations.csv", s =5, alpha = 1.0, c = 'b', marker='s')
gs.addHeatmap(colorscheme = "Blues", bw=30.0, alpha=.4)
gs.addPoints("../example_data/tornado_locations.csv", s=5, alpha = 1.0, c = 'r', marker='v')
gs.addHeatmap(colorscheme = "Reds", bw=30.0, alpha=.4)
```
![GitHub Logo](/images/earthquakes/california_earthquakes_tornadoes_heatmap.png)


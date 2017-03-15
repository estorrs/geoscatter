##geoscatter

**A python API for adding points and heatmaps to a map. **

#Usage

First we import the GeoScatter and GeoPoint classes from geoscatter

```python
from geoscatter.GeoScatter import GeoScatter
from geoscatter.GeoScatter import GeoPoint
```

To use geoscatter you will need a Google Static Maps API key.  It's quick and free, just go [here](https://developers.google.com/maps/documentation/static-maps/) and click *Get A Key* in the top right corner of the page. 
```python
googleMapsApiKey = "INSERT YOUR API KEY HERE!!"
```

To begin, we define our map.  To do this we specify the center of the map by creating a GeoPoint containing the latitude and longitude of the center coordinate (Saint Louis, Mo in this case).  We can also specify a zoom level between 1 and 20 and the size of the map in pixels.  A quick note on map size, if a size below 150 or above 600, good results can't be guaranteed. Additionally you can choose to get a map with or without labels.   
```python
cLat = 38.536178
cLon = -92.302498
center = GeoPoint(cLat, cLon)

gs = GeoScatter(googleMapsApiKey, center, zoom=7, imgSize=600, mapLabels=False)
```

Before we add some points to our map, I'd like to take a moment to say the dataset I'll be using in these examples are all US tornadoes since 1950 (National Weather Service) and all significant global earthquakes since 2500 B.C. (USGS). 

Lets plot all tornadoes in the United States since 1950. 
```python
gs.addPoints("../example_data/tornado_locations.csv", s =2, alpha = .4, c = 'r', marker='o')
```
![GitHub Logo](/images/tornadoes/all_tornadoes.png)
Format: ![Alt Text](url)


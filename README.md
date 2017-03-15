geoplot: a python API for populating maps with points and heatmaps. 

```python
from geoscatter.GeoScatter import GeoScatter
from geoscatter.GeoScatter import GeoPoint

googleMapsApiKey = "AIzaSyAYiqF5K_nJegdPsYOuq80ufWk_x2ffGCc"

cLat = 38.536178
cLon = -92.302498
center = GeoPoint(cLat, cLon)

gs = GeoScatter(googleMapsApiKey, center, zoom = 7, imgSize = 600, mapLabels=False)
gs.addPoints("../example_data/tornado_locations.csv", s =2, alpha = .4, c = 'r', marker='o')
```

![GitHub Logo](/images/logo.png)
Format: ![Alt Text](url)
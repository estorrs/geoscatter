
from geoplot.GeoScatter import GeoScatter
from geoplot.GeoPoint import GeoPoint

googleMapsApiKey = "################"

# 54.599559, -5.927397
cLat = 54.599559
cLon = -5.927397
center = GeoPoint(cLon, cLat)
gs = GeoScatter(googleMapsApiKey, center, zoom = 11, imgSize = 600)


gs.addPoints("../example_data/loyalistPoints.csv", s = 10, alpha = .4, c = 'r', marker='o')
gs.addHeatmap(colorscheme = "Reds", bw=25.0, alpha=.4)
gs.addPoints("../example_data/republicanPoints.csv", s=10,  alpha=.4, c='g', marker="v")
gs.addHeatmap(colorscheme = "Greens", bw=25.0, alpha = .4)
 

gs.showMap()




from geoplot.GeoScatter import GeoScatter
from geoplot.GeoPoint import GeoPoint

googleMapsApiKey = "AIzaSyAYiqF5K_nJegdPsYOuq80ufWk_x2ffGCc"

# 54.599559, -5.927397
cLat = 54.599559
cLon = -5.927397
center = GeoPoint(cLon, cLat)
gs = GeoScatter(googleMapsApiKey, center, zoom = 12, imgSize = 600)


gs.addPoints("../example_data/belfastLoyalistPoints.csv", s = 10, alpha = .4, c = '#FD9008', marker='s')
#gs.addHeatmap(colorscheme = "Oranges", bw=25.0, alpha=.3)
gs.addPoints("../example_data/belfastRepublicanPoints.csv", s = 10,  alpha=.4, c='g', marker="v")
#gs.addHeatmap(colorscheme = "Greens", bw=25.0, alpha = .3)
 

gs.showMap()



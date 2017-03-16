from geoscatter import GeoScatter
from geoscatter import GeoPoint

googleMapsApiKey = "###########"

cLat = 39.140328
cLon = -120.034881
center = GeoPoint(cLat, cLon)
gs = GeoScatter(googleMapsApiKey, center, zoom = 5, imgSize = 600, mapLabels=False)
gs.addPoints("../example_data/earthquake_locations.csv", s =0, alpha = 1.0, c = '#FFFF00', marker='s')
gs.addHeatmap(colorscheme = "coolwarm", bw=25.0, alpha=.4)
gs.showMap()




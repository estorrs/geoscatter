from geoscatter.GeoScatter import GeoScatter
from geoscatter.GeoScatter import GeoPoint

googleMapsApiKey = "AIzaSyAYiqF5K_nJegdPsYOuq80ufWk_x2ffGCc"

cLat = 39.140328
cLon = -120.034881
center = GeoPoint(cLat, cLon)
gs = GeoScatter(googleMapsApiKey, center, zoom = 5, imgSize = 600, mapLabels=False)
gs.addPoints("../example_data/earthquake_locations.csv", s =0, alpha = 1.0, c = '#FFFF00', marker='s')
gs.addHeatmap(colorscheme = "coolwarm", bw=25.0, alpha=.4)
gs.showMap()

# 
# # 38.536178, -92.302498
# 
# 
# #gs.addHeatmap(colorscheme = "coolwarm", bw=25.0, alpha=.4)
# cLat = 38.536178
# cLon = -92.302498
# center = GeoPoint(cLat, cLon)
# ###all_tornadoes.png
# # gs = GeoScatter(googleMapsApiKey, center, zoom = 3, imgSize = 600, mapLabels=False)
# # gs.addPoints("../example_data/tornado_locations.csv", s =.5, alpha = .4, c = 'r', marker='o')
# 
# 
# ##missouri_Tornadoes.png
# # gs = GeoScatter(googleMapsApiKey, center, zoom = 7, imgSize = 600, mapLabels=False)
# # gs.addPoints("../example_data/tornado_locations.csv", s =2, alpha = .4, c = 'r', marker='o')
# 
# ###missouri_Tornadoes_s10.png
# # gs = GeoScatter(googleMapsApiKey, center, zoom = 7, imgSize = 600, mapLabels=False)
# # gs.addPoints("../example_data/tornado_locations.csv", s =10, alpha = .4, c = 'r', marker='o')
# 
# ###missouri_Tornadoes_bluetriangles.png
# # gs = GeoScatter(googleMapsApiKey, center, zoom = 7, imgSize = 600, mapLabels=False)
# # gs.addPoints("../example_data/tornado_locations.csv", s =10, alpha = .4, c = 'b', marker='v')
# 
# ###missouri_Tornadoes_notransparency.png
# # gs = GeoScatter(googleMapsApiKey, center, zoom = 7, imgSize = 600, mapLabels=False)
# # gs.addPoints("../example_data/tornado_locations.csv", s =10, alpha = 1.0, c = 'b', marker='v')
# 
# # ###missouri_Tornadoes_deaths.png
# # gs = GeoScatter(googleMapsApiKey, center, zoom = 7, imgSize = 600, mapLabels=False)
# # gs.addPoints("../example_data/tornadoes_deaths.csv", s =1, alpha = .4, c = 'r', marker='o')
# 
# # ###missouri_Tornadoes_deaths_s3.png
# # gs = GeoScatter(googleMapsApiKey, center, zoom = 7, imgSize = 600, mapLabels=False)
# # gs.addPoints("../example_data/tornadoes_deaths.csv", s =3, alpha = .4, c = 'r', marker='o')
# 
# # ###missouri_Tornadoes_deaths_s3_labels.png
# # gs = GeoScatter(googleMapsApiKey, center, zoom = 7, imgSize = 600, mapLabels=True)
# # gs.addPoints("../example_data/tornadoes_deaths.csv", s =3, alpha = .4, c = 'r', marker='o')
# 
# # ###missouri_Tornadoes_deaths_s3_labels.png
# 
# pts = []
# inputFile = file("../example_data/tornadoes_deaths.csv", "r")
# for line in inputFile: 
#     line = line.strip()
#     pieces = line.split(",")
#     newPoint = GeoPoint(float(pieces[0]), float(pieces[1]))
#     newPoint.magnitude = float(pieces[2])
#     pts.append(newPoint)
#     
# gs = GeoScatter(googleMapsApiKey, center, zoom = 7, imgSize = 600, mapLabels=True)
# gs.addPoints(pts, s =3, alpha = .4, c = 'r', marker='o')
# 
# 
# 
# ###all_earthquakes.png
# cLat = 0
# cLon = 0
# center = GeoPoint(cLat, cLon)
# # gs = GeoScatter(googleMapsApiKey, center, zoom = 1, imgSize = 600, mapLabels=False)
# # gs.addPoints("../example_data/earthquake_locations.csv", s =5, alpha = 1.0, c = '#FFFF00', marker='s')
# 
# 
# 
# 
# ###all_earthquakes_heatmap.png
# # gs = GeoScatter(googleMapsApiKey, center, zoom = 1, imgSize = 600, mapLabels=False)
# # gs.addPoints("../example_data/earthquake_locations.csv", s =5, alpha = 1.0, c = '#FFFF00', marker='s')
# # gs.addHeatmap(colorscheme = "coolwarm", bw=25.0, alpha=.4)
# 
# #39.140328, -120.034881
# cLat = 39.140328
# cLon = -120.034881
# center = GeoPoint(cLat, cLon)
# # ###california_earthquakes_heatmap.png
# # gs = GeoScatter(googleMapsApiKey, center, zoom = 5, imgSize = 600, mapLabels=False)
# # gs.addPoints("../example_data/earthquake_locations.csv", s =5, alpha = 1.0, c = '#FFFF00', marker='s')
# # gs.addHeatmap(colorscheme = "coolwarm", bw=25.0, alpha=.4)
# 
# # # ###california_earthquakes_heatmap_bw10.png
# # gs = GeoScatter(googleMapsApiKey, center, zoom = 5, imgSize = 600, mapLabels=False)
# # gs.addPoints("../example_data/earthquake_locations.csv", s =5, alpha = 1.0, c = '#FFFF00', marker='s')
# # gs.addHeatmap(colorscheme = "coolwarm", bw=10.0, alpha=.4)
# 
# # # ###california_earthquakes_heatmap_bw100.png
# # gs = GeoScatter(googleMapsApiKey, center, zoom = 5, imgSize = 600, mapLabels=False)
# # gs.addPoints("../example_data/earthquake_locations.csv", s =5, alpha = 1.0, c = '#FFFF00', marker='s')
# # gs.addHeatmap(colorscheme = "coolwarm", bw=100.0, alpha=.4)
# 
# # # ###california_earthquakes_heatmap_nopoints.png
# # gs = GeoScatter(googleMapsApiKey, center, zoom = 5, imgSize = 600, mapLabels=False)
# # gs.addPoints("../example_data/earthquake_locations.csv", s =0, alpha = 1.0, c = '#FFFF00', marker='s')
# # gs.addHeatmap(colorscheme = "coolwarm", bw=25.0, alpha=.4)
# 
# # ###california_earthquakes_heatmap_reds.png
# # gs = GeoScatter(googleMapsApiKey, center, zoom = 5, imgSize = 600, mapLabels=False)
# # gs.addPoints("../example_data/earthquake_locations.csv", s =5, alpha = 1.0, c = '#FFFF00', marker='s')
# # gs.addHeatmap(colorscheme = "Reds", bw=25.0, alpha=.4)
# 
# #36.157467, -120.862654
# cLat = 36.157467
# cLon = -120.862654
# center = GeoPoint(cLat, cLon)
# 
# # ###california_earthquakes_tornadoes.png
# # gs = GeoScatter(googleMapsApiKey, center, zoom = 6, imgSize = 600, mapLabels=False)
# # gs.addPoints("../example_data/earthquake_locations.csv", s =5, alpha = 1.0, c = 'b', marker='s')
# # gs.addPoints("../example_data/tornado_locations.csv", s=5, alpha = 1.0, c = 'r', marker='v')
# 
# # ###california_earthquakes_tornadoes_heatmap.png
# # gs = GeoScatter(googleMapsApiKey, center, zoom = 6, imgSize = 600, mapLabels=False)
# # gs.addPoints("../example_data/earthquake_locations.csv", s =5, alpha = 1.0, c = 'b', marker='s')
# # gs.addHeatmap(colorscheme = "Blues", bw=30.0, alpha=.4)
# # gs.addPoints("../example_data/tornado_locations.csv", s=5, alpha = 1.0, c = 'r', marker='v')
# # gs.addHeatmap(colorscheme = "Reds", bw=30.0, alpha=.4)
# 
# 
# gs.showMap()



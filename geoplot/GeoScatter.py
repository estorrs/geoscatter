
import cStringIO
import matplotlib.pyplot as plt
import mercantile
import numpy as np
import os
import urllib
from GeoPoint import GeoPoint

from PIL import Image
from scipy.interpolate import interp1d
from sklearn.neighbors.kde import KernelDensity

'''
Plots points and heatmaps on a map

Map obtained from google maps api, for which an active api key must be provided

Image size can be no larger than 600

'''
class GeoScatter:
    def __init__(self, apiKey, cPoint, zoom=7, imgSize=256, mapLabels=False):
        if (not isinstance(cPoint, GeoPoint)): 
            raise ValueError("cPoint must be a GeoPoint")
        self.center = cPoint
        self.zoom = zoom

        '''
        map zoom returned by google maps api assumes a 256x256 image
        '''
        
        #images larger than 600X600 may cooperate with the google maps api and os correcly
        if imgSize>600: 
            raise ValueError("image must be smaller than 600")
        
        self._baseImageWidth = 256
        self._baseImageHeight = 256
        self._imageWidth = imgSize
        self._imageHeight = imgSize
        
        self._widthAdjustment = float(self._imageWidth)/self._baseImageWidth
        self._heightAdjustment = float(self._imageHeight)/self._baseImageHeight
        
        '''
        The Mercator tiles for google maps api and the mercantile api are slightly different, so they need to be adjusted so \
        points show up in the correct location
        '''
        self._widthCorrection = .996
        self._heightCorrection = 1.001
        
        '''
        to keep track of the current set of points GeoScatter is operating on
        '''
        self._xCoordinates = []
        self._yCoordinates = []
        
        '''
        the plot
        '''
        self._fig = plt.figure().add_subplot(111)
        
        '''
        get the map
        '''
        self._getMap(apiKey, mapLabels)
        
    
    '''
    display the map
    '''
    def showMap(self):
        plt.show()
         
         
    '''
    Add points to the map.  If a point is outside the map bounds then it is not plotted. 
    '''
    def addPoints(self, pts, c='b', s=2, marker="o", edgecolors="none", alpha=1.0):
        
        '''
        do Mercator conversions in order to plot points on map
        '''
        tile = mercantile.tile(self.center.longitude, self.center.latitude, self.zoom)
        bounds = mercantile.bounds(tile.x, tile.y, tile.z)
        nwCorner = mercantile.xy(bounds.west, bounds.north, self.zoom)
        seCorner = mercantile.xy(bounds.east, bounds.south, self.zoom)
        center = mercantile.xy(self.center.longitude, self.center.latitude, self.zoom)
        
        x0 = nwCorner[0]
        x1 = seCorner[0]
        y0 = seCorner[1]
        y1 = nwCorner[1]
        
        width = abs(x1 - x0)
        height = abs(y1 - y0)
        
        leftBound = center[0] - (self._widthAdjustment * width/2)
        rightBound = center[0] + (self._widthAdjustment * width/2)
        topBound = center[1] + (self._heightAdjustment * height/2)
        bottomBound = center[1] - (self._heightAdjustment * height/2)
        
        lonInterp = interp1d([leftBound, rightBound],[0, self._imageWidth])
        latInterp = interp1d([bottomBound,topBound],[0, self._imageHeight]) 

        """
        check for .csv file
        """
        if isinstance(pts, str): 
            ptsFile = file(pts, "r")
            pts = self._getGeoPointsFromFile(ptsFile)
        elif isinstance(pts, file): 
            pts = self._getGeoPointsFromFile(pts)
        
        self._xCoordinates = []
        self._yCoordinates = []
        sizes = []
        for gp in pts: 
            meterCoord = mercantile.xy(gp.longitude, gp.latitude)
            lonInMeters = meterCoord[0]
            latInMeters = meterCoord[1]
            if (lonInMeters >= leftBound and lonInMeters <= rightBound and latInMeters >= bottomBound and latInMeters <= topBound):
                x = lonInterp(lonInMeters) * self._widthCorrection
                y = self._imageHeight - latInterp(latInMeters)* self._heightCorrection
                self._xCoordinates.append(x)
                self._yCoordinates.append(y)
                sizes.append(gp.magnitude*s)
               
        self._fig.scatter(self._xCoordinates, self._yCoordinates, s=sizes, alpha = alpha, c = c, edgecolors = edgecolors, marker=marker)

    '''
    adds a heatmap to the plot
    '''
    def addHeatmap(self, colorscheme = "coolwarm", alpha = .3, bw = 10.0):
        pts = []
        x = range(0, self._imageWidth, 1)
        y = range(0, self._imageHeight, 1)
        for i in x: 
            for j in y: 
                pts.append([float(i), float(j)])
        numpyPts = np.array(pts)

        #check to see if points have been added to map
        if len(self._xCoordinates) == 0: 
            raise RuntimeError("map has no points")
        
        TwoDArray = []
        for i in range(len(self._xCoordinates)): 
            TwoDArray.append([self._yCoordinates[i], self._xCoordinates[i]])
         
        X = np.array(TwoDArray)
        
        '''
        get probablilities for the heatmap
        '''
        kde = KernelDensity(kernel='gaussian', bandwidth = bw).fit(X)
        log_probability = kde.score_samples(numpyPts)
        points = np.exp(log_probability)
        points = np.reshape(points, (self._imageWidth, self._imageHeight))
        
        '''
        plot the heatmap
        '''
        self._fig.imshow(points, cmap=colorscheme, interpolation='nearest', alpha = alpha)
        
    '''
    load map into plot using given key
    '''
    def _getMap(self, apiKey, mapLabels): 
        if mapLabels: 
            mapUrl = "https://maps.googleapis.com/maps/api/staticmap?center=" + str(self.center.latitude) + "," + str(self.center.longitude) + "&zoom=" + str(self.zoom) + "&size=" + str(self._imageWidth) + "x" + str(self._imageHeight) + "&key=" + apiKey
        else: 
            mapUrl = "https://maps.googleapis.com/maps/api/staticmap?center=" + str(self.center.latitude) + "," + str(self.center.longitude) + "&zoom=" + str(self.zoom) + "&size=" + str(self._imageWidth) + "x" + str(self._imageHeight) + "&style=feature:all|element:labels|visibility:off&key=" + apiKey
        
        socket = urllib.urlopen(mapUrl)
        imgData = cStringIO.StringIO(socket.read())
      
        img = Image.open(imgData)
        
        img.save("activeMap.png")
        img = plt.imread("activeMap.png")
        self._fig.imshow(img)
        self._fig.axis("off")
        
        os.remove("activeMap.png")
                
    '''
    read in points from a .csv or .tsv file. 
    format can either be: 
        latitude,longitude
                or 
        latitude,longitude,magnitude
    where magnitude is the relative size of the point
    '''
    def _getGeoPointsFromFile(self, ptsFile):
        pts = []
        for line in ptsFile: 
            if line.__contains__(","): 
                pieces = line.strip().split(",")
            elif line.__contains__("\t"): 
                pieces = line.strip().split("\t")
            else: 
                raise ValueError("incorrect file format, must be comma seperated or tab seperated")
            
            if len(pieces) == 2: 
                pts.append(GeoPoint(float(pieces[1]), float(pieces[0])))
            elif len(pieces) == 3: 
                gp = GeoPoint(float(pieces[1]), float(pieces[0]))
                gp.magnitude = float(pieces[2])
                pts.append(gp)
            else: 
                raise ValueError("points file must be lat,lon or lat,lon,magnitude")
        return pts
            
         
    
    
        
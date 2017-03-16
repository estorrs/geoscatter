from distutils.core import setup
setup(
  name = 'geoscatter',
  packages = ['geoscatter'], # this must be the same as the name above
  version = '0.5',
  description = 'A Python API for adding points and heatmaps to maps', 
  author = 'Erik Storrs',
  author_email = 'estorrs@slu.edu',
  url = 'https://github.com/estorrs/geoscatter', # use the URL to the github repo
  download_url = 'https://github.com/estorrs/geoscatter/archive/0.5.tar.gz', # I'll explain this in a second
  keywords = ['map', 'plot', 'heatmap', 'points', 'scatter', 'figure', 'contour', 'density', 'geoscatter', 'gis', 'coordinate'], # arbitrary keywords
  license='MIT',
  classifiers=[],
  
  install_requires=['matplotlib', 'mercantile', 'numpy', 'scipy', 'sklearn', 'Pillow'],
) 

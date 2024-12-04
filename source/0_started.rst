

Introduction
=============

Présentation générale
----------------------

QGis a été développé à partir des librairies de l’OGR: GDAL/GEOS. La plupart de ces librairies sont développées en C++ et existent en version python par un système de binding, c’est-à-dire des fonctions qui font indirectement référence aux fonctions écrites C++. Ces librairies sont aussi utilisées par d’autres outils libres de SIG: PostGIS, GRASS, GeoServer, gvSIG, etc. Elles se décomposent en 4  principales librairies complémentaires:

* GEOS: Geometry Engine Open Source (transformations géométriques des données en format vectoriel)
* GDAL: ensemble des fonctions consacré à la gestion et à la manipulation des rasters
* OGR: ensemble des fonctions de gestion des formats et des données sous le format vectoriel
* PROJ4: ensemble des fonctions liées aux transformations des systèmes de référencement géographiques



.. .. figure:: img/OverviewLibrairiePythonSIG.png
..    :width: 500px
..    :align: center
.. 
..    Figure : Imbrication des principales librairies géospatiales



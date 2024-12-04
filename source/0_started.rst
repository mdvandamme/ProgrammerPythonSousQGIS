

Introduction
=============

Présentation générale
----------------------

QGis a été développé à partir des librairies de l’OGR: GDAL/GEOS. La plupart de ces librairies sont développées en C++. Ces librairies se décomposent en 4  principales librairies complémentaires:

* GEOS: Geometry Engine Open Source (transformations géométriques des données en format vectoriel)
* GDAL: ensemble des fonctions consacré à la gestion et à la manipulation des rasters
* OGR: ensemble des fonctions de gestion des formats et des données sous le format vectoriel
* PROJ4: ensemble des fonctions liées aux transformations des systèmes de référencement géographiques

Les librairies de l’OGR écrites en C++ sont aussi utilisées par d’autres outils libres de SIG: PostGIS, GRASS, GeoServer, gvSIG, etc. Les librairies python « GDAL,OGR » (dans les blocs en bleu dans la figure ?? ci-dessous) ne sont que des bindings, c’est-à-dire des fonctions qui font indirectement référence aux fonctions écrites C++.



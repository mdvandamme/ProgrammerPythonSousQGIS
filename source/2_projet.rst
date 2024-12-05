

Le projet QGis
===============

Un projet QGis permet de gérer un ensemble de couches avec leurs propriétés (sémiologie par exemple), la projection de la carte, une échelle, etc. L'application QGis ne gère qu'un seul et unique projet à la fois: deux projets ne peuvent pas être ouverts en même temps, et il y a toujours un projet ouvert, vide ou existant. Par son caractère unique, l'implémentation du concept projet suit la modélisation du design pattern Singleton. Cela veut dire que pour interagir avec le projet QGis (comme accéder aux propriétés ou aux traitements) on accède à l'instance courante directement à partir de la classe *QgsProject*:

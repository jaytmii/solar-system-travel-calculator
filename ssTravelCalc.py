import matplotlib.pyplot as plt
import math

class Planet:
# Attributes
    def __init__(self,planetName,x,y,z):
        self.planetName = planetName
        self.x = x
        self.y = y
        self.z = z

class Star:
# Attributes
    def __init__(self,starName,x,y,z):
        self.starName = starName
        self.x = x
        self.y = y
        self.z = z

class Moon:
# Attributes
    def __init__(self,moonName,x,y,z):
        self.moonName = moonName
        self.x = x
        self.y = y
        self.z = z

class Asteroid:
# Attributes
    def __init__(self,asteroidName,x,y,z):
        self.asteroidName = asteroidName
        self.x = x
        self.y = y
        self.z = z

class Ship:
# Atributes
    def __init__(self,engineType,civOrMil,thrust,x,y,shipName):
        self.engineType = engineType
        self.civOrMil = civOrMil
        self.thrust= thrust # in KPH (Kilometers per second)
        self.x = x
        self.y = y
        self.shipName = shipName

# Acceleration metrics
# 1/3 g 3.26 m/s ==> 11.736 km/h
# 1 g 9.8 m/s ==> 35.28 km/h

#  Totals are based off distance in KM from the sun, and then divided by 1 million
Sol = Star("Sol", 0, 0, 0)
Mercury = Planet("Mercury",40.725502, 40.725502, 0)
Venus = Planet("Venus",67.641786, 67.641786, 0)
Earth = Planet("Earth", -93.973388, -93.973388, 0)
Luna = Moon("Luna",-97.973388,-97.973388,0)
Mars = Planet("Mars", 151.508376, -151.508376, 0)
Phobos = Moon("Phobos", 151.508376, -149.508376, 0)
Deimos = Moon("Deimos", 151.508376, -153.508376, 0)
Ceres = Asteroid("Ceres", -247.075876, -247.075876,0 )
Vesta = Asteroid("Vesta", -353, 353, 0)
Pallas = Asteroid("Pallas", 414, -414, 0)
Ganymede = Moon("Ganymede",792.072511,-792.072511,0 )
Europa = Moon("Europa",461.069846,-461.069846,0)
Io = Moon("Io",792.736961,-792.736961,0)
Callisto = Moon("Callisto",464.486314,-461.486314,0)
Jupiter = Planet("Jupiter",-461.486314, -461.486314, 0 )
Hygiea = Asteroid("Hygiea",470, 470, 0)
Saturn = Planet("Saturn",908.512186, 908.512186, 0)
Uranus = Planet("Uranus",1808.483129, -1808.483129, 0)
Neptune = Planet("Neptune", 2780.024276, 2780.024276, 0)
Pluto = Planet("Pluto", 3238.226177, 3238.226177, 0)
researchColony = Asteroid("rc",-430,-430,0)
luckyStrike = Ship("Fusion","Civillian",11.7,-431.486314, -431.486314,"PCH Lucky Strike")


# ENTIRE SOLAR SYSTEM (Minus the Moons)
# x = [Sol.x,Mercury.x, Venus.x,Earth.x, Mars.x, Ceres.x, Vesta.x, Pallas.x,Jupiter.x,Hygiea.x,Saturn.x,Uranus.x,Neptune.x,Pluto.x, Ship.x]
# y = [Sol.y,Mercury.y, Venus.y,Earth.y, Mars.y, Ceres.y, Vesta.y, Pallas.y,Jupiter.y,Hygiea.y,Saturn.y,Uranus.y,Neptune.y,Pluto.y, Ship.y]
# n = [Sol.starName,Mercury.planetName, Venus.planetName,Earth.planetName, Mars.planetName, Ceres.asteroidName, Vesta.asteroidName, Pallas.asteroidName,
# Jupiter.planetName,Hygiea.asteroidName,Saturn.planetName,Uranus.planetName,Neptune.planetName,Pluto.planetName, Ship.shipName]

# INNER SYTSTEM
# x = [Sol.x,Mercury.x, Venus.x,Earth.x,Luna.x, Mars.x, Phobos.x,Deimos.x]
# y = [Sol.y,Mercury.y, Venus.y,Earth.y,Luna.y, Mars.y, Phobos.y,Deimos.y]
# n = [Sol.starName,Mercury.planetName, Venus.planetName,Earth.planetName, Luna.moonName, Mars.planetName, Phobos.moonName,Deimos.moonName]

# JOVIAN SYSTEM
x = [Jupiter.x,Ganymede.x, Europa.x,Io.x,Callisto.x, luckyStrike.x]
y = [Jupiter.y,Ganymede.y, Europa.y,Io.y,Callisto.y, luckyStrike.y]
n = [Jupiter.planetName,Ganymede.moonName, Europa.moonName,Io.moonName,Callisto.moonName, luckyStrike.shipName]

fig, ax = plt.subplots()
ax.scatter(x, y)

for i, txt in enumerate(n):
    ax.annotate(txt, (x[i], y[i]))

def distanceCalcs(xp1,yp1,xp2,yp2,accel):
    d = math.sqrt(((xp2-xp1)**2+(yp2-yp1)**2))
    print("Coordinate differential :", d)
    km = int(d*1000000)
    print("kilometers :", km)
    t = 2*(math.sqrt(((2/2)*km)/accel))
    t = int(t)
    print("travel in seconds",t)
    hours = (t/60)/60
    print("travel in hours: ", hours)

distanceCalcs(luckyStrike.x,luckyStrike.y,researchColony.x,researchColony.y,3.26)

plt.title("Jovian System")
plt.xlabel("Coordinates")
plt.ylabel("Coordinates")
plt.show()


import random
from graphics import *
import time
import math


class Center(object):

    def __init__(self, x1: int, y1: int):
        self.__centerX = x1
        self.__centerY = y1
        self.__accelerate = 0
        self.__health = 100
        self.__direction = 90  # degrees


        self.__listCenter = []
        self.__listCenter.append(x1)
        self.__listCenter.append(y1)
        self.__listCenter.append(90)

        self.__point = Point(self.__listCenter[0], self.__listCenter[1])


    def newCenter(self):
        newCenter = [0, 0]

        newCenter[0] = 1.0 * math.cos(self.getTheta(self.__listCenter[2]))
        newCenter[1] = 1.0 * -math.sin(self.getTheta(self.__listCenter[2]))


        return newCenter

    def getRadius(self):
        radius = math.sqrt((self.__listCenter[0]-0)**2 + (self.__listCenter[1]-0)**2)
        return radius


    def getTheta(self, degrees):

        remainder = degrees % 360

        return remainder * math.pi / 180

    def calcTheta(self):

        return math.atan(self.__listCenter[1] / self.__listCenter[0])

    def rotateCenter(self, direction):

        self.__listCenter[2] = self.__listCenter[2] + direction

    def drawCenter(self, win: GraphWin):
        self.__point.setFill("White")
        self.__point.draw(win)

    def moveCenter(self, win: GraphWin):
        center = self.newCenter()

        dx = center[0]
        dy = center[1]

        if self.__listCenter[0] + dx > win.getWidth():
            center[0] -= win.getWidth()

        elif self.__listCenter[0] + dx < 0:
            center[0] += win.getWidth()

        if self.__listCenter[1] + dy > win.getWidth():
            center[1] -= win.getWidth()

        elif self.__listCenter[1] + dy < 0:
            center[1] += win.getWidth()

        self.updateCenter(center)
        self.__point.move(center[0], center[1])


    def coast(self, i, win):
        center = [0, 0]

        center[0] = (1 / i) * math.cos(self.getTheta(self.__listCenter[2]))
        center[1] = (1 / i) * -math.sin(self.getTheta(self.__listCenter[2]))

        dx = center[0]
        dy = center[1]


        if self.__listCenter[0] + dx > win.getWidth():
            center[0] -= win.getWidth()

        elif self.__listCenter[0] + dx < 0:
            center[0] += win.getWidth()

        if self.__listCenter[1] + dy > win.getWidth():
            center[1] -= win.getWidth()

        elif self.__listCenter[1] + dy < 0:
            center[1] += win.getWidth()

        self.updateCenter(center)
        self.__point.move(center[0], center[1])

        #return center




    def updateCenter(self, center):

        self.__listCenter[0] += center[0]
        self.__listCenter[1] += center[1]


    def getList(self):
        return self.__listCenter

    def getHeading(self):
        heading = self.__listCenter[2]
        return self.getTheta(heading)

    def getX(self):
        return self.__listCenter[0]

    def getY(self):
        return self.__listCenter[1]

    def setX(self, x):
        self.__listCenter[0] += x

    def setY(self, y):
        self.__listCenter[1] += y

    def getPoint(self):
        return Point(self.__listCenter[0], self.__listCenter[1])

    # def isHit(self, objectList: list):
    #     listIndex = 0
    #
    #     while listIndex < len(objectList):
    #         if Circle.testCollision_CircleVsPoint(objectList[listIndex].getSelf(), self.__point):
    #             self.__point.undraw()
    #             objectList[listIndex].getSelf().undraw()
    #             objectList.pop(listIndex)
    #
    #
    #
    #             return True
    #         listIndex += 1
    #         return False




class Asteroid(Center):

    def __init__(self, x, y):
        super().__init__(x, y)

        self.__radius = random.randrange(12, 25)

        self.__dx = random.randrange(-1, 1, 1)
        self.__dy = random.randrange(-1, 1, 1)

        self.__asteroid = Circle(Point(self.getX(), self.getY()), self.__radius)

        # self.__x1 = x
        # self.__x2 = self.__x1 + 18
        # self.__x3 = self.__x1 + 38
        # self.__x4 = self.__x1 + 56
        # self.__x5 = self.__x1 + 38
        # self.__x6 = self.__x1 + 18
        # self.__y1 = y
        # self.__y2 = self.__y1 - 18
        # self.__y3 = self.__y2
        # self.__y4 = self.__y1
        # self.__y5 = self.__y1 + 10
        # self.__y6 = self.__y1 + 10
        #
        # self.__dx = random.randrange(-5, 50, 3)
        # self.__dy = random.randrange(-5, 15, 3)
        #
        #
        #
        # self.__asteriod = Polygon(Point(self.__x1, self.__y1), Point(self.__x2, self.__y2), Point(self.__x3, self.__y3), Point(self.__x4, self.__y4), Point(self.__x5, self.__y5), Point(self.__x6, self.__y6))


    def drawAsteroid(self, win: GraphWin):
        self.__asteroid.setFill("grey")
        self.__asteroid.draw(win)


    def moveAsteroid(self, win: GraphWin):

        if self.getX() + self.__dx > win.getWidth():
            self.__dx -= win.getWidth()

        elif self.getX() + self.__dx < 0:
            self.__dx += win.getWidth()

        if self.getY() + self.__dy > win.getWidth():
            self.__dy -= win.getWidth()

        elif self.getY() + self.__dy < 0:
            self.__dy += win.getWidth()


        self.setX(self.__dx)
        self.setY(self.__dy)

        self.__asteroid.move(self.__dx, self.__dy)

    def collision(self, asteroidList: list, bulletList: list):
        asterIndex = 0

        while asterIndex < len(asteroidList):
            if self != asteroidList[asterIndex]:
                if Circle.testCollision_CircleVsCircle(self.__asteroid, asteroidList[asterIndex].__asteroid):
                    asteroidList[asterIndex].__asteroid.undraw()
                    asteroidList.pop(asterIndex)
                    return True

            asterIndex += 1
            return False

    def getLocation(self):
        point = Point(self.getX(), self.getY())
        return point

    def isHit(self, missileList: list):
        listIndex = 0

        while listIndex < len(missileList):
            if Circle.testCollision_CircleVsCircle(self.__asteroid, missileList[listIndex].getSelf()):
                self.__asteroid.undraw()
                missileList[listIndex].getSelf().undraw()
                missileList.pop(listIndex)

                return True
            listIndex += 1
            return False

class Rocket(Center):

    def __init__(self, x, y, theta):
        super().__init__(x, y)
        self.__theta = theta

        self.__P1 = self.nosePoint()
        self.__P2, self.__P3 = self.cornerPoint()

        self.__ship = Polygon(self.__P1, self.__P2, self.__P3)


    def nosePoint(self):
        x = 16 * math.cos(-self.__theta)
        y = 16 * math.sin(-self.__theta)

        return Point((self.getX() + x), (self.getY() + y))


    def cornerPoint(self):

        theta = math.atan(2.5) + math.pi / 2

        x = math.sqrt(725) * math.cos(-self.__theta - theta)
        y = math.sqrt(725) * math.sin(-self.__theta - theta)

        x2 = math.sqrt(725) * math.cos(-self.__theta + theta)
        y2 = math.sqrt(725) * math.sin(-self.__theta + theta)

        return Point((self.getX() + x), (self.getY() + y)), Point((self.getX() + x2), (self.getY() + y2))


    def drawShip(self, win: GraphWin):
        self.__ship.setFill(color_rgb(255, 255, 255))
        self.__ship.draw(win)

    def undraw(self):
        self.__ship.undraw()

    def angle(self):
        return -self.__theta

class Missile(object):

    def __init__(self, rocket: Rocket):
        self.__xy = rocket.getPoint()
        self.__x = self.__xy.getX()
        self.__y = self.__xy.getY()
        self.__size = 3
        self.__disTravel = 0

        self.__dx = 0
        self.__dy = 0
        self.calcAngle(rocket)

        self.___missile = Circle(self.__xy, self.__size)


    def calcDistance(self):

        x1 = self.__xy.getX()
        y1 = self.__xy.getY()
        self.__disTravel += math.sqrt((x1 - self.__x)**2 + (y1 - self.__y)**2)
        return self.__disTravel


    def calcAngle(self, rocket: Rocket):
        theta = rocket.angle()
        self.__dx = math.cos(theta)
        self.__dy = math.sin(theta)


    def drawMissile(self, win: GraphWin):
        self.___missile.setFill("white")
        self.___missile.draw(win)

    def moveMissile(self, win: GraphWin):

        if self.__x + self.__dx > win.getWidth():
            self.__dx -= win.getWidth()

        elif self.__x + self.__dx < 0:
            self.__dx += win.getWidth()

        if self.__y + self.__dy > win.getWidth():
            self.__dy -= win.getWidth()

        elif self.__y + self.__dy < 0:
            self.__dy += win.getWidth()

        self.__x += self.__dx
        self.__y += self.__dy


        self.___missile.move(self.__dx, self.__dy)

    def undrawMissile(self):
        self.___missile.undraw()

    def getLocation(self):
        point = Point(self.__x, self.__y)
        return point

    def getSelf(self):

        return self.___missile





def main():
    win = GraphWin("Asteroids", 600, 600, autoflush = False)
    win.setBackground("black")
    coast = False

    asteroidList = []
    missileList = []

    origin = Center(300, 300)
    rocket = Rocket(300, 300, math.pi/2)
    rocket.drawShip(win)


    for i in range(0):
        asteroidList.append((Asteroid(random.randrange(50, 500), random.randrange(50, 550))))
        asteroidList[i].drawAsteroid(win)

    while True:
        keyboard = win.checkKeys()
        print(keyboard)
        print(origin.getList())


        if 'Left' in keyboard:
            degree = .5
            origin.rotateCenter(degree)
            rocket.undraw()
            rocket = Rocket(origin.getX(), origin.getY(), origin.getHeading())
            rocket.drawShip(win)


        if 'Right' in keyboard:
            degree = -.5
            origin.rotateCenter(degree)
            rocket.undraw()
            rocket = Rocket(origin.getX(), origin.getY(), origin.getHeading())
            rocket.drawShip(win)

        if 'Up' in keyboard:
            origin.moveCenter(win)
            rocket.undraw()
            rocket = Rocket(origin.getX(), origin.getY(), origin.getHeading())
            rocket.drawShip(win)
            coast = True

        if coast == True and 'Up' not in keyboard:
            for i in range(1,200):
                origin.coast(i, win)
                rocket.undraw()
                rocket = Rocket(origin.getX(), origin.getY(), origin.getHeading())
                rocket.drawShip(win)
                time.sleep(1)

            coast = False



        if 'Down' in keyboard:

            if len(missileList) < 200:
                missileList.append(Missile(rocket))
                missileList[-1].drawMissile(win)


        for asteroid in asteroidList:

            if asteroid.isHit(missileList):
                element = asteroidList.index(asteroid)
                asteroidList.pop(element)

            asteroid.moveAsteroid(win)



        for missile in missileList:
            if missile.calcDistance() > 10000:
                element = missileList.index(missile)
                missile.undrawMissile()
                missileList.pop(element)
            missile.moveMissile(win)  # Double move missile so it outpaces forward movement of spaceship
            missile.moveMissile(win)

        print(f"Asteroids remaining: {len(asteroidList)}")
        print(f"Missile List: {len(missileList)}")




        win.update()
        #time.sleep()
    win.getMouse()
    win.close()


main()

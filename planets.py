{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "TclError",
     "evalue": "invalid command name \".!canvas\"",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTclError\u001b[0m                                  Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-1-b6b0bb4bb90f>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     61\u001b[0m     \u001b[0mellipse\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mMars\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m4\u001b[0m\u001b[1;33m*\u001b[0m\u001b[0mo\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m160\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m0.5\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     62\u001b[0m     \u001b[0mellipse\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mJupiter\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m*\u001b[0m\u001b[0mo\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m200\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m0.35\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 63\u001b[1;33m     \u001b[0mellipse\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mSaturn\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mo\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m240\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m0.3\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m<ipython-input-1-b6b0bb4bb90f>\u001b[0m in \u001b[0;36mellipse\u001b[1;34m(p, o, a, e)\u001b[0m\n\u001b[0;32m     53\u001b[0m     \u001b[0mx\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mr\u001b[0m\u001b[1;33m*\u001b[0m\u001b[0mmath\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcos\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmath\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mradians\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mo\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m+\u001b[0m\u001b[0ma\u001b[0m\u001b[1;33m*\u001b[0m\u001b[0me\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     54\u001b[0m     \u001b[0my\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mr\u001b[0m\u001b[1;33m*\u001b[0m\u001b[0mmath\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msin\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmath\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mradians\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mo\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 55\u001b[1;33m     \u001b[0mp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mgoto\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mx\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0my\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     56\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     57\u001b[0m \u001b[1;32mfor\u001b[0m \u001b[0mo\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m3601\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\users\\zhang\\miniconda3\\lib\\turtle.py\u001b[0m in \u001b[0;36mgoto\u001b[1;34m(self, x, y)\u001b[0m\n\u001b[0;32m   1774\u001b[0m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_goto\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mVec2D\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m*\u001b[0m\u001b[0mx\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1775\u001b[0m         \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1776\u001b[1;33m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_goto\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mVec2D\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mx\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0my\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1777\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1778\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mhome\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\users\\zhang\\miniconda3\\lib\\turtle.py\u001b[0m in \u001b[0;36m_goto\u001b[1;34m(self, end)\u001b[0m\n\u001b[0;32m   3156\u001b[0m                       (self.currentLineItem,\n\u001b[0;32m   3157\u001b[0m                       \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcurrentLine\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 3158\u001b[1;33m                       \u001b[0mscreen\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_pointlist\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcurrentLineItem\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   3159\u001b[0m                       self.items[:])\n\u001b[0;32m   3160\u001b[0m                       )\n",
      "\u001b[1;32mc:\\users\\zhang\\miniconda3\\lib\\turtle.py\u001b[0m in \u001b[0;36m_pointlist\u001b[1;34m(self, item)\u001b[0m\n\u001b[0;32m    753\u001b[0m         (9.9999999999999982, 0.0)]\n\u001b[0;32m    754\u001b[0m         >>> \"\"\"\n\u001b[1;32m--> 755\u001b[1;33m         \u001b[0mcl\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcv\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcoords\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mitem\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    756\u001b[0m         \u001b[0mpl\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m[\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mcl\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mi\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m-\u001b[0m\u001b[0mcl\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mi\u001b[0m\u001b[1;33m+\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mfor\u001b[0m \u001b[0mi\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mlen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mcl\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m2\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    757\u001b[0m         \u001b[1;32mreturn\u001b[0m  \u001b[0mpl\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m<string>\u001b[0m in \u001b[0;36mcoords\u001b[1;34m(self, *args, **kw)\u001b[0m\n",
      "\u001b[1;32mc:\\users\\zhang\\miniconda3\\lib\\tkinter\\__init__.py\u001b[0m in \u001b[0;36mcoords\u001b[1;34m(self, *args)\u001b[0m\n\u001b[0;32m   2464\u001b[0m         return [self.tk.getdouble(x) for x in\n\u001b[0;32m   2465\u001b[0m                            self.tk.splitlist(\n\u001b[1;32m-> 2466\u001b[1;33m                    self.tk.call((self._w, 'coords') + args))]\n\u001b[0m\u001b[0;32m   2467\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0m_create\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mitemType\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0margs\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mkw\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;31m# Args: (val, val, ..., cnf={})\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   2468\u001b[0m         \u001b[1;34m\"\"\"Internal function.\"\"\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mTclError\u001b[0m: invalid command name \".!canvas\""
     ]
    }
   ],
   "source": [
    "import math\n",
    "import turtle\n",
    "wn=turtle.Screen()\n",
    "turtle.clearscreen()\n",
    "wn.bgcolor('black')\n",
    "\n",
    "Mercury=turtle.Turtle()\n",
    "Vernus=turtle.Turtle()\n",
    "Earth=turtle.Turtle()\n",
    "Mars=turtle.Turtle()\n",
    "Jupiter=turtle.Turtle()\n",
    "Saturn=turtle.Turtle()\n",
    "Sun=turtle.Turtle()\n",
    "\n",
    "Sun.pensize(10)\n",
    "Sun.shape('circle')\n",
    "Sun.color('yellow')\n",
    "\n",
    "Mercury.up()\n",
    "Mercury.fd(40)\n",
    "Mercury.down()\n",
    "Vernus.up()\n",
    "Vernus.fd(80)\n",
    "Vernus.down()\n",
    "Earth.up()\n",
    "Earth.fd(120)\n",
    "Earth.down()\n",
    "Mars.up()\n",
    "Mars.fd(160)\n",
    "Mars.down()\n",
    "Jupiter.up()\n",
    "Jupiter.fd(200)\n",
    "Jupiter.down()\n",
    "Saturn.up()\n",
    "Saturn.fd(240)\n",
    "Saturn.down()\n",
    "\n",
    "def planet(name,color):\n",
    "    name.pencolor(color)\n",
    "    name.color(color)\n",
    "    name.shape('circle')\n",
    "    name.speed(0)\n",
    "\n",
    "planet(Mercury,'purple')\n",
    "planet(Vernus,'yellow')\n",
    "planet(Earth,'blue')\n",
    "planet(Mars,'red')\n",
    "planet(Jupiter,'green')\n",
    "planet(Saturn,'pink')\n",
    "\n",
    "def ellipse(p,o,a,e):\n",
    "    r=a*(1-e**2)/(1+e*math.cos(math.radians(o)))\n",
    "    x=r*math.cos(math.radians(o))+a*e\n",
    "    y=r*math.sin(math.radians(o))\n",
    "    p.goto(x,y)          \n",
    "\n",
    "for o in range(1,3601):                \n",
    "    ellipse(Mercury,16*o,40,0.65)\n",
    "    ellipse(Vernus,12*o,80,0.45)\n",
    "    ellipse(Earth,8*o,120,0.2)\n",
    "    ellipse(Mars,4*o,160,0.5)\n",
    "    ellipse(Jupiter,2*o,200,0.35)\n",
    "    ellipse(Saturn,o,240,0.3)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

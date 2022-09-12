#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
from math import pi


def square_root(a):
    return a**0.5
#return.math.sqrt(a)


def square(a):
    return a*a


def average(a, b, c) :
    return( a+b+c)/3


def to_radians(angle_degs, angle_mins, angle_secs):

   #transformer les deg en degrés décimal
    #degres_decimal = angle_degs + (angle_mins + (angle_secs / 60)) / 60

   #transformer les degres en radiant
    #rad=(degres_decimal * pi)/180

    return math.radians(angle_degs + (angle_mins + (angle_secs / 60)) / 60)


def to_degrees(angle_rads):

    angle_deg = angle_rads * 180 / pi
    min= (angle_deg-int(angle_deg))*60
    sec= (min - int(min))*60

    return round(angle_deg),round(min) , round(sec)


def to_celsius(temperature):
    return (temperature - 32)/1.8

def to_farenheit(temperature):
    return (temperature * 1.8)+ 32


def main() -> None:
    print(f"La racine carré de 144 est : {square_root(144)}")

    print(f"Le carré de 12 est : {square(12)}")

    print(f"Moyenne des nombres 2, 4, 6: {average(2, 4, 6)}")

    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(100, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()

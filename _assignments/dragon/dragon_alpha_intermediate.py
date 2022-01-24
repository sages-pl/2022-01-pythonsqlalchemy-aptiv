"""
>>> import sys; sys.tracebacklimit = 0
>>> from random import seed; seed(0)

>>> wawelski = Dragon(name='Wawelski', position_x=50, position_y=120)
>>> wawelski.set_position(x=10, y=20)
>>> wawelski.move(left=10, down=20)
>>> wawelski.move(left=10, right=15)
>>> wawelski.move(right=15, up=5)
>>> wawelski.move(down=5)
>>> assert wawelski.make_damage() in range(5, 20)
>>> wawelski.take_damage(10)
>>> wawelski.take_damage(5)
>>> wawelski.take_damage(3)
>>> wawelski.take_damage(2)
>>> wawelski.take_damage(15)
>>> wawelski.take_damage(25)
>>> wawelski.take_damage(75)
Wawelski is dead
{'gold': 98, 'position': (20, 40)}
"""

from random import randint



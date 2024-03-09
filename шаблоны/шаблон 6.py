"""import turtle as t

mashtab = 50
n = 7
t.left(90)
for i in range(n):
    t.forward(10 * mashtab)
    t.right(120)
t.up()
for x in range(11):
    for y in range(11):
        t.goto(x * mashtab, y * mashtab)
        t.dot(5)"""
"""import turtle as t

mashtab = 30
n = 2
t.left(90)
for i in range(n):
    t.forward(8 * mashtab)
    t.right(90)
    t.forward(18 * mashtab)
    t.right(90)
t.up()
n = 1
for i in range(n):
    t.forward(4 * mashtab)
    t.right(90)
    t.forward(10 * mashtab)
    t.left(90)
t.down()
n = 2
for i in range(n):
    t.forward(17 * mashtab)
    t.right(90)
    t.forward(7 * mashtab)
    t.right(90)
for x in range(20):
    for y in range(20):
        t.goto(x * mashtab, y * mashtab)
        t.dot(5)"""
import turtle as t

mashtab = 10
n = 20
t.left(90)
for i in range(n):
    for j in range(4):
        t.forward(15 * mashtab)
        t.right(90)
    t.backward(20 * mashtab)
    t.right(90)
t.up()
input()
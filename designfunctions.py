def jump(t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def polygon(agent, side, size, c):
    agent.color(c)
    angle = 360/side
    agent.begin_fill()
    for x in range(side):
        agent.forward(size)
        agent.right(angle)
    agent.end_fill()


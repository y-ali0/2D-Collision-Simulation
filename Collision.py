# Session6Collision.py

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import itertools

class Canvas():
    """This class creates the canvas object."""
    def __init__(self):
        """With self you can access private attributes of the object."""
        self.size = 20
        self.blocks = []
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot()

    def add_block(self, block):
        """Every time a block is created it gets put into the array."""
        self.blocks.append(block)

    def update_blocks(self):
        """This method moves and draws all blocks."""
        self.ax.clear()
        for i, block in enumerate(self.blocks):
            block.move()
            block.draw()

    def fix_axes(self):
        """The axes would change with each iteration otherwise."""
        self.ax.set_xlim((-self.size/2, self.size/2))
        self.ax.set_ylim((-0.25, 0.25))

    def check_collision(self):
        """This method checks if blocks are colliding."""
        combinations = list(itertools.combinations( range(len(self.blocks)), 2))

        for pair in combinations:
            self.blocks[pair[0]].collide(self.blocks[pair[1]])


class Block():
    """This class creates the block object."""
    def __init__(
        self,
        canvas,
        mass,
        position=0,
        velocity=0
    ):
        self.canvas = canvas
        self.mass = mass
        self.position = position
        self.velocity = velocity
        # The block is automatically added to the canvas
        self.canvas.add_block(self)
        self.color = "black"

    def move(self):
         """The block is moved based on the velocity."""
         self.position = self.position + self.velocity
        

    def draw(self):
        """The method to draw the block. Note: if you don’t specify color of the block the color of each new element that is plotted will be randomly asigned. """
        canvas.ax.plot(self.position, 0, "o")

    def collide(self, other):
        # Threshold has to be sufficiently high for collisions to trigger.
        if abs(self.position - other.position) < 0.5:
             # The velocities after collision, v used as a variable to save the initial self.velocity so other.velocity can be calculated using the initial self.velocity
             v = self.velocity
             self.velocity = (2*other.mass)/(self.mass+other.mass)*other.velocity + (self.mass-other.mass)/(self.mass+other.mass)*self.velocity 
             other.velocity = (other.mass-self.mass)/(self.mass+other.mass)*other.velocity+(2*self.mass)/(self.mass+other.mass)*v
             
 
            
canvas = Canvas()
block1 = Block(canvas, mass=1, position=2, velocity=-0.05)
block2 = Block(canvas, mass=30, position=-2, velocity=-0.02)
block3 = Block(canvas, mass=2, position=8, velocity=-0.05)
block4 = Block(canvas, mass=40, position=-6, velocity=-0.1)
block5 = Block(canvas, mass=50, position=-9, velocity=-0.005)
block6 = Block(canvas, mass=70, position=-8, velocity=-0.01)
block7 = Block(canvas, mass=3, position=4, velocity=0.1)
block8 = Block(canvas, mass=4, position=8, velocity=0.06)
block9 = Block(canvas, mass=5, position=10, velocity=-0.05)
block10 = Block(canvas, mass=90, position=-1, velocity=0.1)
wall1 = Block(canvas, mass=9999999999, position=-10.2, velocity=0)
wall2 = Block(canvas, mass=9999999999, position=10.2, velocity=0)

time = []
block1pos = []
block3pos = []
block1velocity = []
block3velocity = []


def animate(i):
    """This controls the animation."""
    time.append(i)
    block1pos.append(block1.position)
    block3pos.append(block3.position)
    block1velocity.append(block1.velocity)
    block3velocity.append(block3.velocity)    
    print("The frame is:", i)
    canvas.update_blocks()
    canvas.check_collision()
    canvas.fix_axes()

# This calls the animate function and creates animation.
anim = animation.FuncAnimation(canvas.fig, animate, frames=500, interval=10)

# This prepares the writer for the animation.
writervideo = animation.FFMpegWriter(fps=60)
# This plays the animation.
plt.show()


plt.hist(block1pos,bins=10, label="mass = 1")
plt.hist(block3pos,bins=10, label="mass = 2")
plt.legend(loc="upper right")
plt.ylabel("Frequency")
plt.xlabel("Position")
plt.show()

plt.hist(block1velocity,bins=100, label="mass = 1")
plt.hist(block3velocity,bins=100, label="mass = 2")
plt.legend(loc="upper right")
plt.ylabel("Frequency")
plt.xlabel("Velocity")
plt.show()

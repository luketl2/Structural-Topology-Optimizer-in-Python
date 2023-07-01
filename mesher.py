from matplotlib import pyplot as plt
import numpy as np
import pygmsh

with pygmsh.geo.Geometry() as geom:
    geom.add_polygon(
        [
            [0.0, 0.0],
            [1.0, -0.2],
            [1.1, 1.2],
            [0.1, 0.7],
        ],
        mesh_size=0.1,
    )
    mesh = geom.generate_mesh()

nodes = mesh.points

plt.triplot(nodes[:,0], nodes[:,1], color='blue', label = 'Nodes')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()

plt.show()
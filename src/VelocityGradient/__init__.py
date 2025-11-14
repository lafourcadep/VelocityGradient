from ovito.data import DataCollection, CutoffNeighborFinder
from ovito.pipeline import ModifierInterface
from traits.api import Float
import numpy as np

class VelocityGradient(ModifierInterface):

    cutoff = Float(4.0, label="Cutoff radius")
    
    def modify(self, data: DataCollection, frame: int, **kwargs):
        
        if 'Velocity' not in data.particles:
            raise RuntimeError(
                "Missing required particle properties: 'Velocity'.\n"
                "Please make sure the data contains per-particle velocity vector."
            )
        
        L = np.zeros((data.particles.count,9))
        finder = CutoffNeighborFinder(self.cutoff, data)
        velocities = data.particles.velocities
        for index in range(data.particles.count):
            yield 'Calculating velocity gradient tensor'
            neigh_vel = velocities[ [neigh.index for neigh in finder.find(index)] ]
            delta_v = neigh_vel-velocities[index]
            delta_x = finder.neighbor_vectors(index)
            A = np.linalg.inv(delta_x.T @ delta_x)
            B = delta_v.T @ delta_x
            L[index] = np.dot(B,A).reshape(9)
        data.particles_.create_property("L", data=L)

from compas_cem.diagrams import TopologyDiagram
from compas_cem.elements import Node
from compas_cem.elements import DeviationEdge
from compas_cem.elements import TrailEdge
from compas_cem.equilibrium import static_equilibrium
from compas_cem.loads import NodeLoad
from compas_cem.optimization import Optimizer
from compas_cem.optimization import PointConstraint
from compas_cem.optimization import TrailEdgeParameter
from compas_cem.plotters import Plotter
from compas_cem.supports import NodeSupport


# 1. Define inputs
# Instantiate an empty topology diagram
topology = TopologyDiagram()

# Add nodes
topology.add_node(Node(1, xyz=[0., 0., 0.]))
topology.add_node(Node(2))
topology.add_node(Node(3))

# Add edges
# The sign of the length indicates the force state
topology.add_edge(TrailEdge(1, 2, length=-1.))
topology.add_edge(TrailEdge(2, 3, length=-1.))

# Indicate support node
topology.add_support(NodeSupport(3))

# Add load
topology.add_load(NodeLoad(1, vector=[1., 0., 0.]))

# Build trails automatically
topology.build_trails(auxiliary_trails=False)

# 2. Form-Finding
# Generate form diagram in static equilibrium
form = static_equilibrium(topology, tmax=1, eta=1e-5)

# 3. Constrained Form-Finding
# Instantiate an optimizer
optimizer = Optimizer()

# Set target position for node 3
constraint = PointConstraint(3, point=[3., 0., 0.])
optimizer.add_constraint(constraint)

# Define optimization parameters
optimizer.add_parameter(TrailEdgeParameter((1, 2)))
optimizer.add_parameter(TrailEdgeParameter((2, 3)))

# Solve constrained form-finding problem
cform = optimizer.solve(topology, "SLSQP", eps=1e-6)

# 4. Visualize constrained form diagram
plotter = Plotter()
plotter.add(cform)
plotter.show()
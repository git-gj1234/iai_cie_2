from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
import networkx as nx
import matplotlib.pyplot as plt
from pgmpy.inference import VariableElimination

# Defining Bayesian Structure
model = BayesianNetwork([('Guest', 'Host'), ('Price', 'Host')])

# Defining the CPDs:
cpd_guest = TabularCPD('Guest', 3, [[0.33], [0.33], [0.33]])
cpd_price = TabularCPD('Price', 3, [[0.33], [0.33], [0.33]])
cpd_host = TabularCPD('Host', 3, [[0, 0, 0, 0, 0.5, 1, 0, 1, 0.5],
                                   [0.5, 0, 1, 0, 0, 0, 1, 0, 0.5],
                                   [0.5, 1, 0, 1, 0.5, 0, 0, 0, 0]],
                      evidence=['Guest', 'Price'], evidence_card=[3, 3])

# Associating the CPDs with the network structure.
model.add_cpds(cpd_guest, cpd_price, cpd_host)

# Check the model
model.check_model()
infer = VariableElimination(model)
posterior_p = infer.query(['Host'], evidence={'Guest': 2, 'Price': 2})
print(posterior_p)
# Draw the Bayesian Network using NetworkX
pos = nx.circular_layout(model)  # You can change this to other layouts
labels = {node: node for node in model.nodes()}
nx.draw(model, pos=pos, labels=labels, with_labels=True, node_size=1000, node_color='skyblue', font_size=10, font_color='black', font_weight='bold')

# Save the plot
plt.savefig('model.png')
plt.show()

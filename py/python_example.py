import networkx as nx
from math import floor
import matplotlib.pyplot as plt

print("Please input the integer you wish to analyze:")
myNum = int(input())

# Below we identify the number of digits the given
# number has (in decimal).
n = -1
i = 0
x = myNum
while n < 0:
  i += 1
  x = floor(x/10)
  # We check this by iteratively checking
  if x == 0:
    n = i
  # previous version, w/o floor.
  # pretty sure it's slower.
  # if x - (x%(pow(10,i))) == 0:
  #   n = i

# Need list for dynamic colors.
node_colors = []
G = nx.DiGraph()
G.add_node(myNum)
# Red indicates starting (given) value.
node_colors.append('red')
done = False
p = myNum
while not done:
  c = (myNum*p)%(pow(10,n))
  if c not in G:
    G.add_node(c)
    node_colors.append('yellow')
  else:
    # Now we check if our starting number is excluded
    # from the cycle and indicate it with cyan if so.
    if c != myNum:
      node_colors[list(G.nodes).index(c)] = 'cyan'
    done = True
  G.add_edge(p,c)
  p = c

print(str(myNum)+" generates a graph "+
      "of "+str(G.order())+" nodes.")

# Would have this be lists, but sets have optimal
# runtime efficiency for setdiff operations...
universe = set(G.nodes)
group = set()
e = nx.find_cycle(G,p)
for edge in e:
  group.add(edge[0])
  universe.remove(edge[0])

if(len(universe) > 0):
  print("The following are not within the closed,"+    " potential group:")
  print(universe)

print("The following are within the closed, potential group:")
print(group)
# I used to have a better layout, but circular
# does the job for now.
pos = nx.circular_layout(G)
nx.draw(G,pos,with_labels=True,node_color=node_colors)
plt.savefig(str(myNum)+'.png',format="PNG")
print("Graph created.")
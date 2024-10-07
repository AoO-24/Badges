class Area:
  def __init__(self, name):
    self.name = name
    self.subarea = []

  def add_subarea(self, name):
    self.subarea.add(Area(name)
    



def dfs(self, visited = None):
  if visited is None:
    visited = set()
  print(self.name)
  visited.add(self)
  for sub in self.subarea:
    if sub not in visited:
      sub.dfs(visited)


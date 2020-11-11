from libseidrfile import SeidrFile_Internal
class SeidrFile(object):
  """docstring for SeidrFile"""
  def __init__(self, path):
    super(SeidrFile, self).__init__()
    self.path = path
    self.sf_ptr = SeidrFile_Internal(path)
    self.attr = self.sf_ptr.attr()
    self.nodes = self.sf_ptr.nodes()
    self.supplementary = self.sf_ptr.supplementary()
    self.algorithms = self.sf_ptr.algorithms()

  def algorithms(self):
    return self.algorithms

  def attr(self):
    return self.attr

  def supplementary(self):
    return self.supplementary

  def nodes(self):
    return self.nodes

  def centrality(self):
    return self.sf_ptr.centrality()

  def edge_scores(self):
    return self.sf_ptr.edge_scores()

  def edge_ranks(self):
    return self.sf_ptr.edge_ranks()

  def edge_supplementary(self):
    return self.sf_ptr.edge_supplementary()

  def edge_index(self):
    return self.sf_ptr.edge_index()

  def edge_flag(self):
    return self.sf_ptr.edge_flag()

  def edge(self):
    return self.sf_ptr.edge()

  def next_edge(self):
    return self.sf_ptr.next_edge()

  def make_networkit_graph(self, graph, weighted = True, algorithm = None):
    if graph.numberOfNodes() > 0:
      raise ValueError("You need to supply an empty graph")
    self.sf_ptr.reset()
    graph.addNodes(self.attr['nodes'])
    if not algorithm:
      algorithm = self.algorithms[-1]
    si = self.algorithms.index(algorithm)
    for e in edgeIterator(self):
      if weighted:
        graph.addEdge(e['index'][0], e['index'][1], e['scores'][si])
      else:
        graph.addEdge(e['index'][0], e['index'][1])
    self.sf_ptr.reset()
    return graph

  def __reset__(self):
    self.sf_ptr.reset()

class edgeIterator(object):
  """docstring for edgeIterator"""
  def __init__(self, seidrfile):
    super(edgeIterator, self).__init__()
    self.seidrfile = seidrfile

  def __len__(self):
    return self.seidrfile.attr.edges

  def __iter__(self):
    return self

  def __next__(self):
    if not self.seidrfile.next_edge():
      self.seidrfile.__reset__();
      raise StopIteration
    return self.seidrfile.edge()

class scoreIterator(object):
  """docstring for scoreIterator"""
  def __init__(self, seidrfile):
    super(scoreIterator, self).__init__()
    self.seidrfile = seidrfile

  def __len__(self):
    return self.seidrfile.attr.edges

  def __iter__(self):
    return self

  def __next__(self):
    if not self.seidrfile.next_edge():
      self.seidrfile.__reset__();
      raise StopIteration
    return self.seidrfile.edge_scores()

class rankIterator(object):
  """docstring for rankIterator"""
  def __init__(self, seidrfile):
    super(rankIterator, self).__init__()
    self.seidrfile = seidrfile

  def __len__(self):
    return self.seidrfile.attr.edges

  def __iter__(self):
    return self

  def __next__(self):
    if not self.seidrfile.next_edge():
      self.seidrfile.__reset__();
      raise StopIteration
    return self.seidrfile.edge_ranks()

class supplementaryIterator(object):
  """docstring for supplementaryIterator"""
  def __init__(self, seidrfile):
    super(supplementaryIterator, self).__init__()
    self.seidrfile = seidrfile

  def __len__(self):
    return self.seidrfile.attr.edges

  def __iter__(self):
    return self

  def __next__(self):
    if not self.seidrfile.next_edge():
      self.seidrfile.__reset__();
      raise StopIteration
    return self.seidrfile.edge_supplementary()

class flagIterator(object):
  """docstring for flagIterator"""
  def __init__(self, seidrfile):
    super(flagIterator, self).__init__()
    self.seidrfile = seidrfile

  def __len__(self):
    return self.seidrfile.attr.edges

  def __iter__(self):
    return self

  def __next__(self):
    if not self.seidrfile.next_edge():
      self.seidrfile.__reset__();
      raise StopIteration
    return self.seidrfile.edge_flag()

class indexIterator(object):
  """docstring for indexIterator"""
  def __init__(self, seidrfile):
    super(indexIterator, self).__init__()
    self.seidrfile = seidrfile

  def __len__(self):
    return self.seidrfile.attr.edges

  def __iter__(self):
    return self

  def __next__(self):
    if not self.seidrfile.next_edge():
      self.seidrfile.__reset__();
      raise StopIteration
    return self.seidrfile.edge_index()
    
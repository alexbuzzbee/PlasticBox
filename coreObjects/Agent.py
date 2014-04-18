

class Agent(object):
  """The base class for Agents, which carry resources (Including population)."""
  agentType = None
  location = 0
  
  # Private
  
  # Public
  
  def destroy(self):
    del self.agentType
    del self.location
  
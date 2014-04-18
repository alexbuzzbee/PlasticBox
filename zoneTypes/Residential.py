import ZoneRCI

class Residential(ZoneRCI):
  """A residential zone, which contains people, and can send them."""
  zoneType = "res"
  population = 0
  populationElsewhere = 0
  populationMax = 0
  
  # Private
  
  def __refreshStats(self):
    self.populationMax = self.density * 10
    super().__refreshStats()
  
  def __makeWorkers(self, number):
    agent = AgentWorkers(number)
    self.agents.append(agent)
  
  # Public
  
  def produce(self):
    """Produce this zone's products and send them."""
    for agent in self.agents:
      if all(agent.agentType == "helpWanted", self.population - self.populationElsewhere > agent.workers):
        self.__makeWorkers(agent.workers)
        self.populationElsewhere = self.populationElsewhere + agent.number
      else:
        self.__makeWorkers(self.population - self.populationElsewhere)
        self.populationElsewhere = self.population
  
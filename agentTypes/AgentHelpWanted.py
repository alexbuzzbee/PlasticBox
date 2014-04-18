import Agent

class AgentHelpWanted(Agent):
  agentType = "helpWanted"
  workersWanted = 0;
  
  def __init__(self, numWorkers):
    self.workersWanted = numWorkers
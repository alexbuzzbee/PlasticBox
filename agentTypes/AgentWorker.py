import Agent

class AgentWorker(Agent):
  agentType = "workers"
  workers = 0
  
  def __init__(self, numWorkers):
    self.workers = numWorkers
  
  def dropOffWorkers(self):
    pass
  
import Agent

class AgentWorker(Agent):
  agentType = "worker"
  workers = 0
  
  def __init__(self, numWorkers):
    self.workers = numWorkers
  
  def dropOffWorkers(self):
    pass
  
# PlasticBox engine by Alex Martin.
# Error codes:
# 1 - PlasticBox engine was started as an application.

import logging
import sys
import imp
import time

# Predefined global variables:
debugStatus = True

# Functions:
def main():
  engineLogger.info("Detected that the engine has been started as an application.")
  engineLogger.critical("The PlasticBox engine should not be started as an application. Stopping.")
  sys.exit(1)

def init():
  engineLogger.info("Initializing game...")

def setupEngineLogger(debugState):
  engineLogger.setLevel(logging.DEBUG)
  # Create handlers.
  ech = logging.StreamHandler()
  efh = logging.FileHandler("engineLog.log", mode="w")
  # Set handlers' state.
  if debugState == True:
    ech.setLevel(logging.DEBUG)
    efh.setLevel(logging.DEBUG)
  else:
    ech.setLevel(logging.WARNING)
    efh.setLevel(logging.INFO)
  # Create formatter.
  formatter = logging.Formatter('%(asctime)s %(name)s - %(levelname)s:%(message)s')
  # Set formatters and add handlers.
  ech.setFormatter(formatter)
  efh.setFormatter(formatter)
  engineLogger.addHandler(ech)
  engineLogger.addHandler(efh)

def loadMod(modDir, modName):
  modContainer = imp.find_module(modName, modDir)
  imp.load_module("mod_" + modName, modContainer)

def setupEngine():
  setupEngineLogger(debugStatus)
  engineLogger.info("Logging enabled.")
  engineLogger.info("Setting up...")

engineLogger = logging.getLogger(__name__)

# Launch main if not module.
if __name__ == '__main__':
    main()


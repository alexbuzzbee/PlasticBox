# PlasticBox Game Starter by Alex Martin
# Error codes:
# None.

import logging
import PlasticBox

debugStatus = True

PlasticBox.setupEngine()

def main():
    starterLogger.debug("Entered main().")
    PlasticBox.init()

def setupStarterLogger(debugState):
  # Create handlers.
  sch = logging.StreamHandler()
  sfh = logging.FileHandler("startupLog.log", mode="w")
  # Set handlers' state.
  if debugState == True:
    sch.setLevel(logging.DEBUG)
    sfh.setLevel(logging.DEBUG)
  else:
    sch.setLevel(logging.WARNING)
    sfh.setLevel(logging.INFO)
  # Create formatter.
  formatter = logging.Formatter('%(asctime)s GameStarter - %(levelname)s:%(message)s')
  # Set formatters and add handlers.
  sch.setFormatter(formatter)
  sfh.setFormatter(formatter)
  starterLogger.addHandler(sch)
  starterLogger.addHandler(sfh)

starterLogger = logging.getLogger(__name__)
starterLogger.setLevel(logging.DEBUG)
setupStarterLogger(debugStatus)
starterLogger.info("Logging enabled.")
starterLogger.info("Ready to initialize PlasticBox.")

if __name__ == '__main__':
    main()


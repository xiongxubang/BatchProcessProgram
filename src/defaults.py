# This file stores the default parameters of the experiment.
from yacs.config import CfgNode as CN

_C = CN()

def get_cfg_defaults():
  """Get a yacs CfgNode object with default values for my_project."""
  # Return a clone so that the defaults will not be altered
  # This is for the "local variable" use pattern
  return _C.clone()


_C.Data_Name = ""
_C.Data_Size = None
_C.Para2 = None
_C.Para3 = None
_C.Para4 = None







"""
# save the cfg as .yaml file
cfg = get_cfg_defaults()
with open("output.yaml", "w") as f:
  f.write(cfg.dump())   # save config to file
"""

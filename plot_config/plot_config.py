# This file stores the default parameters of the experiment.
from yacs.config import CfgNode as CN

_C = CN()

def get_cfg_defaults():
  """Get a yacs CfgNode object with default values for my_project."""
  # Return a clone so that the defaults will not be altered
  # This is for the "local variable" use pattern
  return _C.clone()

def get_template():
    cfg = get_cfg_defaults()
    with open("./plot_config/plot_config_template.yaml", "w") as f:
        f.write(cfg.dump())   # save config to file

_C.Type = 'line'
_C.Output_file = 'output.eps'

_C.Pointsize = 2
_C.Key = 'right top'
_C.Xlabel = 'xlabel'
_C.Ylabel = 'ylabel'
_C.Xtics = []
_C.Ytics = []
_C.Xrange = ''
_C.Yrange = ''
_C.Log = []
_C.Format = ['y "%.1e"']

_C.Data = CN()
_C.Data.X_Y = []  # "1 2 4-6@2 3" means choose row 1,2,4,5,6 col 2,3 to plot, col 2 is x-axis, col 3 is y-axis
_C.Data.X_Y_Name = []
_C.Data.X_Y2 = []
_C.Data.X_Y2_Name = []



_C.Y2label = CN()
_C.Y2label.is_available = False
_C.Y2label.Y2label = 'y2label'
_C.Y2label.Y2tics = []
_C.Y2label.Y2range = []



if __name__ == "__main__":
    get_template()


"""
# save the cfg as .yaml file
cfg = get_cfg_defaults()
with open("output.yaml", "w") as f:
  f.write(cfg.dump())   # save config to file
"""

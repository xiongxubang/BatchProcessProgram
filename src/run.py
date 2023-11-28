import sys
import os
cur_file_path = os.path.abspath(os.path.dirname(__file__))
parent_path = os.path.abspath(os.path.join(cur_file_path, ".."))
sys.path.append(parent_path)            # add the project path (autoParam) to the system path

from src.main import run
from src.defaults import get_cfg_defaults


if __name__ == "__main__":
  cfg = get_cfg_defaults()
  cfg.merge_from_file(os.path.join(cur_file_path, "config.yaml"))
  cfg.freeze()

  # when running the instance, the working dir will change to the instance folder
  os.chdir(cur_file_path)       # for the better saving output file         
  run(cfg)
  os.chdir(parent_path)
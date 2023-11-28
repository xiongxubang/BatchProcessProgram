from pygnuplot import gnuplot
from plot_config.plot_config import get_cfg_defaults
import pandas as pd
import os

# default styles
linespoints = ["linespoints linetype 1 pointtype 1", "linespoints linetype 1 pointtype 2", 
               "linespoints linetype 1 pointtype 6", "linespoints linetype 1 pointtype 4",
               "linespoints linetype 1 pointtype 8", "linespoints linetype 1 pointtype 10", 
               "linespoints linetype 1 pointtype 12", "linespoints linetype 1 pointtype 14"]

dashed = ["linespoints linetype 1 pointtype 2", "linespoints linetype 2 pointtype 2",
          "linespoints linetype 4 pointtype 2", "linespoints linetype 6 pointtype 2",
          "linespoints linetype 3 pointtype 2", "linespoints linetype 5 pointtype 2"]

boxes = ["boxes fs pattern 1", "boxes fs pattern 4", "boxes fs pattern 5", "boxes fs pattern 2",
         "boxes fs pattern 6", "boxes fs pattern 7", "boxes fs pattern 8", "boxes fs pattern 10",
         "boxes fs pattern 9", "boxes fs pattern 3"]

boxes_solid = ["boxes fs solid 0.3", "boxes fs solid 0.7", "boxes fs solid 0.0", "boxes fs solid 1.0"]


def get_df(pairs):
    df = []
    with open("./bpp_config/files_path.txt", "r") as f:
        lines = f.read().splitlines()   # read all lines
        result_path = lines[3]
    table = pd.read_csv(result_path, index_col=0)

    for x_y in pairs:
        x_y = x_y.split(sep="@")
        rows_str = x_y[0]
        cols_str = x_y[1]
        rows_list = rows_str.split(sep=' ')
        cols_list = cols_str.split(sep=' ')

        rows = []
        cols = [int(cols_list[0]), int(cols_list[1])]
        for elem in rows_list:
            if '-' in elem:
                temp = elem.split(sep='-')
                begin = int(temp[0])
                end = int(temp[1])
                for i in range(begin, end+1):
                    rows.append(i)
            else:
                rows.append(int(elem))
        # selection
        df_temp = table.loc[rows, :]
        df_temp = df_temp.iloc[:, cols]
        df_temp.sort_values(by=df_temp.columns.values[0], inplace=True)     # sort by the first column (axis-x)
        df.append(df_temp)
        print(df_temp)
    
    df = pd.concat(df, axis=1)
    return df

        
def get_plot_line_command(name_list):
    command_list = []
    for i in range(len(name_list)):
        command = f'using {2*i+1+1}:{2*i+2+1} title "{name_list[i]}" with {dashed[i]}'
        command_list.append(command)
    
    return command_list

def get_plot_bar_command(name_list):
    command_list = []
    
    
    return command_list




def plot_line(cfg):
    # initialize
    g = gnuplot.Gnuplot()
    g.cmd('set size 1.000000, 0.500000')
    g.cmd('set terminal postscript portrait enhanced mono "Helvetica" 22')

    # set the output file
    g.cmd(f'set out "{cfg.Output_file}"')

    # set the labels
    g.cmd(f'set pointsize {cfg.Pointsize}')
    g.cmd(f'set xlabel "{cfg.Xlabel}"')
    g.cmd(f'set ylabel "{cfg.Ylabel}"')
    

    # set the key
    g.cmd(f'set key {cfg.Key}')

    # set the range and tics
    if cfg.Xrange != '':
        g.cmd(f'set xrange {cfg.Xrange}')
    for elem in cfg.Xtics:
        g.cmd(f'set xtics {elem}')
    if cfg.Yrange != '':
        g.cmd(f'set yrange {cfg.Yrange}')
    for elem in cfg.Ytics:
        g.cmd(f'set ytics {elem}')
    
    # set log
    for elem in cfg.Log:
        g.cmd(f'set log {elem}')
    
    # set format
    for elem in cfg.Format:
        g.cmd(f'set format {elem}')
    
    # get dataFrame
    df = get_df(cfg.Data.X_Y)

    # plot
    command = get_plot_line_command(cfg.Data.X_Y_Name)
    g.plot_data(df, *command)


    # end
    g.cmd('set size 1,1')
    g.cmd('set terminal x11')


def plot_bar(cfg):
    # initialize
    g = gnuplot.Gnuplot()
    g.cmd('set size 1.000000, 0.500000')
    g.cmd('set terminal postscript portrait enhanced mono "Helvetica" 22')

    # set the output file
    g.cmd(f'set out "{cfg.Output_file}"')

    # set the labels
    g.cmd(f'set pointsize {cfg.Pointsize}')
    g.cmd(f'set xlabel "{cfg.Xlabel}"')
    g.cmd(f'set ylabel "{cfg.Ylabel}"')

    # set the key
    g.cmd(f'set key {cfg.Key}')

    # set the range and tics
    if cfg.Xrange != '':
        g.cmd(f'set xrange {cfg.Xrange}')
    for elem in cfg.Xtics:
        g.cmd(f'set xtics {elem}')
    if cfg.Yrange != '':
        g.cmd(f'set yrange {cfg.Yrange}')
    for elem in cfg.Ytics:
        g.cmd(f'set ytics {elem}')
    
    # set log
    for elem in cfg.Log:
        g.cmd(f'set log {elem}')

    # y2 label
    if cfg.Y2label.is_available:
        g.cmd(f'set y2label "{cfg.Y2label.Y2label}"')
        if cfg.Y2label.Y2range != '':
            g.cmd(f'set y2range {cfg.Y2label.Y2range}')
        for elem in cfg.Y2label.Y2tics:
            g.cmd(f'set y2tics {elem}')

    
    # get dataFrame
    df = get_df(cfg.Data.X_Y)

    # plot
    command = get_plot_bar_command(cfg.Data.X_Y_Name)
    g.plot_data(df, *command)


    # end
    g.cmd('set size 1,1')
    g.cmd('set terminal x11')


if __name__ == "__main__":
    plot_config_dir = "./plot_config"

    with open(os.path.join(plot_config_dir, "plot_files.txt"), "r") as f:
        paths = f.read().splitlines()
        for file_path in paths: 
            cfg = get_cfg_defaults()
            cfg.merge_from_file(os.path.join(plot_config_dir, file_path))
            if cfg.Type == 'line':
                plot_line(cfg)
            elif cfg.Type == 'bar':
                plot_bar(cfg)
            else:
                print("Type error!")
    






from langchain_core.tools import tool
from pyecharts.charts import Line
from pyecharts import options as opts

@tool
def line():
    '''
    折线图生成工具，生成折线图
    '''
def plot_line(plot_args,options):
    line = Line()
    if options:
        line.set_global_opts(
            title_opts=opts.TitleOpts(title=options[0], subtitle=options[1]),
            xaxis_opts=opts.AxisOpts(name=options[2]),
            yaxis_opts=opts.AxisOpts(name=options[3]),
            legend_opts=opts.LegendOpts(pos_left=options[4], pos_top=options[5]),
            toolbox_opts=opts.ToolboxOpts(is_show=options[6] != 'False'))
    line.add_xaxis(plot_args['x_axis'])
    for k,v in plot_args['y_axis'].items():
        line.add_yaxis(k,v)
    if 'render' in plot_args: line.render(plot_args['render'])
    else: line.render("line.html")
    return '折线图生成成功'
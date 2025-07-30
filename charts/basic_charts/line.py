from langchain_core.tools import tool
from pyecharts.charts import Line
from pyecharts import options as opts

@tool
def line():
    '''
    折线图生成工具，生成折线图
    '''
def plot_line(plot_args,options):
    bar = Line()
    if options:
        bar.set_global_opts(
            title_opts=opts.TitleOpts(title=options[0], subtitle=options[1]),
            xaxis_opts=opts.AxisOpts(name=options[2]),
            yaxis_opts=opts.AxisOpts(name=options[3]),
            legend_opts=opts.LegendOpts(pos_left=options[4], pos_top=options[5]))
        if options[6] != 'False': bar.set_global_opts(options.ToolboxOpts())
    bar.add_xaxis(plot_args['x_axis'])
    bar.add_yaxis(plot_args['title'],plot_args['y_axis'])
    if 'render' in plot_args: bar.render(plot_args['render'])
    else: bar.render("line.html")
    return '折线图生成成功'
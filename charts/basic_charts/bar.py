from langchain_core.tools import tool
from pyecharts.charts import Bar
from pyecharts import options as opts

@tool
def bar():
    '''
    柱状图/条形图生成工具，生成柱状图
    '''
def plot_bar(plot_args,options):
    bar = Bar()
    if options:
        bar.set_global_opts(
            title_opts=opts.TitleOpts(title=options[0], subtitle=options[1]),
            xaxis_opts=opts.AxisOpts(name=options[2]),
            yaxis_opts=opts.AxisOpts(name=options[3]),
            legend_opts=opts.LegendOpts(pos_left=options[4], pos_top=options[5]),
            toolbox_opts=opts.ToolboxOpts(is_show=options[6] != 'False'))
    bar.add_xaxis(plot_args['x_axis'])
    for k,v in plot_args['y_axis'].items():
        bar.add_yaxis(k,v)
    if 'render' in plot_args: bar.render(plot_args['render'])
    else: bar.render("bar.html")
    return '柱状图生成成功'
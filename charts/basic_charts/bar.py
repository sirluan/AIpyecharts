from langchain_core.tools import tool
from pyecharts.charts import Bar
from pyecharts import options as opts
from dataclasses import dataclass,asdict
from ..options import AIoptions
@tool
def bar():
    '''
    柱状图/条形图生成工具，生成柱状图
    '''

@dataclass
class Bar_opts:
    title: str = ""
    sub_title: str = ""
    x_axis_label: str = ""
    y_axis_label: str = ""
    legend_pos_left: str = "center"
    legend_pos_top: str = "top"
    toolbox_opts:bool = False

template = """
        1. title: 主标题,默认为空字符串
        2. subtitle: 副标题,默认为空字符串
        3. x轴名称,默认为空字符串
        4. y轴名称,默认为空字符串
        5. lengend_pos_left:图例横向位置, 默认为'center'
        6. lengend_pos_top: 图例纵向位置，默认为'top'
        7. toolbox_ops: 工具箱配置,布尔型，默认为False"""
def plot_bar(model,plot_args,options):
    bar = Bar()
    bar_opts = Bar_opts()
    options = AIoptions(model,template=template,opt_keys=asdict(bar_opts),message=options).opts
    if options:
        bar.set_global_opts(
            title_opts=opts.TitleOpts(title=options['title'], subtitle=options['sub_title']),
            xaxis_opts=opts.AxisOpts(name=options['x_axis_label']),
            yaxis_opts=opts.AxisOpts(name=options['y_axis_label']),
            legend_opts=opts.LegendOpts(pos_left=options['legend_pos_left'], pos_top=options['legend_pos_top']),
            toolbox_opts=opts.ToolboxOpts(is_show=options['toolbox_opts'] != 'False'))
    bar.add_xaxis(plot_args['x_axis'])
    for k,v in plot_args['y_axis'].items():
        bar.add_yaxis(k,v)
    if 'render' in plot_args: bar.render(plot_args['render'])
    else: bar.render("bar.html")
    return '柱状图生成成功'






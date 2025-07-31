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
    x_axis_label_rotate: bool = False
    brush_show : bool = False
    slider_show: bool = False

template = """
        1. title: 主标题,默认为空字符串。
        2. subtitle: 副标题,默认为空字符串。
        3. x轴名称,默认为空字符串。
        4. y轴名称,默认为空字符串。
        5. lengend_pos_left:图例横向位置, 默认为'center'，可以选择'left','center','right'。
        6. lengend_pos_top: 图例纵向位置，默认为'top',可以选择;'top','bottom'。
        7. toolbox_ops: 工具箱配置,是否展示工具箱,工具箱可以保存图片、区域缩放、堆叠、折线图和柱状图相互转换操作,布尔型,默认为False。
        8、x_axis_label_rotate: x轴名称是否旋转,布尔型,默认为False。
        9. brush_show: 是否进入选择模式,开启后可以进行框选、圈选等操作,布尔型,默认为False。
        10. slider_show: 是否开启滑块，布尔型，默认为False。
        """

def plot_bar(model,plot_args,options):
    bar = Bar()
    bar_opts = Bar_opts()
    options = AIoptions(model,template=template,opt_keys=asdict(bar_opts),message=options).opts
    if options:
        bar.set_global_opts(
            title_opts=opts.TitleOpts(title=options['title'], subtitle=options['sub_title']),
            xaxis_opts=opts.AxisOpts(name=options['x_axis_label'],axislabel_opts=opts.LabelOpts(rotate=-15 if options['x_axis_label_rotate'] != 'False' else 0)),
            yaxis_opts=opts.AxisOpts(name=options['y_axis_label']),
            legend_opts=opts.LegendOpts(pos_left=options['legend_pos_left'], pos_top=options['legend_pos_top']),
            toolbox_opts=opts.ToolboxOpts(is_show=options['toolbox_opts'] != 'False'),
            brush_opts=opts.BrushOpts() if options['brush_show'] != 'False' else None,
            datazoom_opts=opts.DataZoomOpts() if options['slider_show'] != 'False' else None)
    bar.add_xaxis(plot_args['x_axis'])
    for k,v in plot_args['y_axis'].items():
        bar.add_yaxis(k,v)
    if 'render' in plot_args: bar.render(plot_args['render'])
    else: bar.render("bar.html")
    return '柱状图生成成功'






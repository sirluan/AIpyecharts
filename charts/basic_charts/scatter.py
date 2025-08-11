from langchain_core.tools import tool
from pyecharts.charts import Scatter
from pyecharts import options as opts
from dataclasses import dataclass,asdict
from ..options import AIoptions
@tool
def scatter():
    '''
    散点图生成工具，生成散点图
    '''

@dataclass
class Scatter_opts:
    title: str = ""
    sub_title: str = ""
    x_axis_label: str = ""
    y_axis_label: str = ""
    legend_pos: str = None
    toolbox_opts:bool = False
    x_axis_label_rotate: bool = False
    brush_show : bool = False
    slider_show: bool = False

template = """
        1. title: 主标题,默认为空字符串
        2. subtitle: 副标题,默认为空字符串
        3. x_axis_label: x轴名称,默认为空字符串
        4. y_axis_label: y轴名称,默认为空字符串
        5. legend_pos: 图例位置,str类型,默认为None,表示居中,如果是left表示靠左,如果是right表示靠右,不要用center,否则会报错
        6. toolbox_ops: 工具箱配置,是否展示工具箱,工具箱可以保存图片、区域缩放、堆叠、折线图和柱状图相互转换操作,布尔型,默认为False。
        7、x_axis_label_rotate: x轴名称是否旋转,布尔型,默认为False。
        8. brush_show: 是否进入选择模式,开启后可以进行框选、圈选等操作,布尔型,默认为False。
        9. slider_show: 是否开启滑块,布尔型,默认为False。"""
def plot_scatter(model,plot_args,options):
    chart = Scatter()
    scatter_opts = Scatter_opts()
    options = AIoptions(model,template=template,opt_keys=asdict(scatter_opts),message=options).opts
    chart.add_xaxis(plot_args['x_axis'])
    for yaxis in plot_args['y_axis']:
        chart.add_yaxis(series_name=yaxis['name'],y_axis=yaxis['value'])
    if options:
        chart.set_global_opts(
            title_opts=opts.TitleOpts(title=options['title'], subtitle=options['sub_title']),
            xaxis_opts=opts.AxisOpts(name=options['x_axis_label'],axislabel_opts=opts.LabelOpts(rotate=-15 if options['x_axis_label_rotate'] != 'False' else 0)),
            yaxis_opts=opts.AxisOpts(name=options['y_axis_label']),
            legend_opts=opts.LegendOpts(pos_left=options['legend_pos'],pos_top='center',orient='vertical')if options['legend_pos'] != 'None' else opts.LegendOpts(),
            toolbox_opts=opts.ToolboxOpts(is_show=options['toolbox_opts'] != 'False'),
            brush_opts=opts.BrushOpts() if options['brush_show'] != 'False' else None,
            datazoom_opts=opts.DataZoomOpts() if options['slider_show'] != 'False' else None)
        
    
    if 'render' in plot_args: chart.render(plot_args['render'])
    else: chart.render("scatter.html")
    return '散点图生成成功'

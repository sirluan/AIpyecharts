from langchain_core.tools import tool
from pyecharts.charts import Bar3D
from pyecharts import options as opts
from dataclasses import dataclass,asdict
from ..options import AIoptions
@tool
def bar3d():
    '''
    3D柱状图生成工具，生成3D柱状图
    '''

@dataclass
class Bar3D_opts:
    title: str = ""
    sub_title: str = ""
    legend_pos: str = None

template = """
        1. title: 主标题,默认为空字符串
        2. subtitle: 副标题,默认为空字符串
        3. legend_pos: 图例位置,str类型,默认为None,表示居中,如果是left表示靠左,如果是right表示靠右"""
def plot_bar3d(model,plot_args,options):
    chart = Bar3D()
    bar3d_opts = Bar3D_opts()
    options = AIoptions(model,template=template,opt_keys=asdict(bar3d_opts),message=options).opts
    chart.add(
        plot_args['data']['name'] if 'name' in plot_args['data'] else '',
        [[d[1], d[0], d[2]] for d in plot_args['data']['value']],
        xaxis3d_opts=opts.Axis3DOpts(plot_args['data']['x_label'], type_="category"),
        yaxis3d_opts=opts.Axis3DOpts(plot_args['data']['y_label'], type_="category"),
        zaxis3d_opts=opts.Axis3DOpts(type_="value"),
    )
    if options:
        chart.set_global_opts(
            title_opts=opts.TitleOpts(title=options['title'], subtitle=options['sub_title']),
            legend_opts=opts.LegendOpts(pos_left=options['legend_pos'],pos_top='center',orient='vertical')if options['legend_pos'] != 'None' else opts.LegendOpts())
        
    
    if 'render' in plot_args: chart.render(plot_args['render'])
    else: chart.render("boxplot.html")
    return '3D柱状图生成成功'

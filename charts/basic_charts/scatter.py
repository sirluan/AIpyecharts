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

template = """
        1. title: 主标题,默认为空字符串
        2. subtitle: 副标题,默认为空字符串"""
def plot_scatter(model,plot_args,options):
    chart = Scatter()
    scatter_opts = Scatter_opts()
    options = AIoptions(model,template=template,opt_keys=asdict(scatter_opts),message=options).opts
    chart.add_xaxis(plot_args['x_axis'])
    for yaxis in plot_args['y_axis']:
        chart.add_yaxis(series_name=yaxis['name'],y_axis=yaxis['value'])
    if options:
        chart.set_global_opts(
            title_opts=opts.TitleOpts(title=options['title'], subtitle=options['sub_title']))
        
    
    if 'render' in plot_args: chart.render(plot_args['render'])
    else: chart.render("scatter.html")
    return '散点图生成成功'

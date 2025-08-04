from langchain_core.tools import tool
from pyecharts.charts import Boxplot
from pyecharts import options as opts
from dataclasses import dataclass,asdict
from ..options import AIoptions
@tool
def boxplot():
    '''
    箱线图生成工具，生成箱线图
    '''

@dataclass
class Boxplot_opts:
    title: str = ""
    sub_title: str = ""

template = """
        1. title: 主标题,默认为空字符串
        2. subtitle: 副标题,默认为空字符串"""
def plot_boxplot(model,plot_args,options):
    chart = Boxplot()
    boxplot_opts = Boxplot_opts()
    options = AIoptions(model,template=template,opt_keys=asdict(boxplot_opts),message=options).opts
    chart.add_xaxis(plot_args['x_axis']) if 'x_axis' in plot_args else None
    for yaxis in plot_args['y_axis']:
        chart.add_yaxis(series_name=yaxis['name'],y_axis=chart.prepare_data(yaxis['value']))
    if options:
        chart.set_global_opts(
            title_opts=opts.TitleOpts(title=options['title'], subtitle=options['sub_title']))
        
    
    if 'render' in plot_args: chart.render(plot_args['render'])
    else: chart.render("boxplot.html")
    return '箱线图生成成功'

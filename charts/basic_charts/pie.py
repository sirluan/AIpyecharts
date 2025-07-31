from langchain_core.tools import tool
from pyecharts.charts import Pie
from pyecharts import options as opts
from dataclasses import dataclass,asdict
from ..options import AIoptions
@tool
def pie():
    '''
    饼图/扇形图生成工具，生成饼图
    '''

@dataclass
class Pie_opts:
    title: str = ""
    sub_title: str = ""

template = """
        1. title: 主标题,默认为空字符串
        2. subtitle: 副标题,默认为空字符串"""
def plot_pie(model,plot_args,options):
    chart = Pie()
    pie_opts = Pie_opts()
    options = AIoptions(model,template=template,opt_keys=asdict(pie_opts),message=options).opts
    if options:
        chart.set_global_opts(
            title_opts=opts.TitleOpts(title=options['title'], subtitle=options['sub_title']))
    chart.add(plot_args['name'], [list(i) for i in plot_args['value'].items()])
    if 'render' in plot_args: chart.render(plot_args['render'])
    else: chart.render("pie.html")
    return '饼图生成成功'

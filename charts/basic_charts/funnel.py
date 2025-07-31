from langchain_core.tools import tool
from pyecharts.charts import Funnel
from pyecharts import options as opts
from dataclasses import dataclass,asdict
from ..options import AIoptions
@tool
def funnel():
    '''
    漏斗图生成工具，生成漏斗图
    '''

@dataclass
class Funnel_opts:
    title: str = ""
    sub_title: str = ""
    is_ascend: bool = False

template = """
        1. title: 主标题,默认为空字符串
        2. subtitle: 副标题,默认为空字符串
        3. is_ascend: 是否颠倒漏斗图,默认为False"""
def plot_funnel(model,plot_args,options):
    chart = Funnel()
    funnel_opts = Funnel_opts()
    options = AIoptions(model,template=template,opt_keys=asdict(funnel_opts),message=options).opts
    if options:
        chart.set_global_opts(
            title_opts=opts.TitleOpts(title=options['title'], subtitle=options['sub_title']))
    chart.add(plot_args['name'], [list(i) for i in plot_args['value'].items()],sort_='ascending' if options['is_ascend'] != 'False' else 'descending')
    if 'render' in plot_args: chart.render(plot_args['render'])
    else: chart.render("funnel.html")
    return '漏斗图生成成功'

from langchain_core.tools import tool
from pyecharts.charts import Graph
from pyecharts import options as opts
from dataclasses import dataclass,asdict
from ..options import AIoptions
@tool
def graph():
    '''
    关系图图生成工具，生成关系图
    '''

@dataclass
class Graph_opts:
    title: str = ""
    sub_title: str = ""

template = """
        1. title: 主标题,默认为空字符串
        2. subtitle: 副标题,默认为空字符串"""
def plot_graph(model,plot_args,options):
    chart = Graph()
    graph_opts = Graph_opts()
    options = AIoptions(model,template=template,opt_keys=asdict(graph_opts),message=options).opts
    chart.add(
        plot_args['data']['name'] if 'name' in plot_args['data'] else '',
        nodes=plot_args['data']['nodes'],
        links=plot_args['data']['links'],
        repulsion= plot_args['data']['repulsion'] if  'repulsion' in plot_args['data'] else 50,
    )
    if options:
        chart.set_global_opts(
            title_opts=opts.TitleOpts(title=options['title'], subtitle=options['sub_title']))
      
    return chart

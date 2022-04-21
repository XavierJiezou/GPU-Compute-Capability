from bs4 import BeautifulSoup
from rich.console import Console
import requests
import json


def spider(url: str, save_json: str):
    """A spider to crawl the computing capability information of GPUs from NVIDIA's official website.

    Args:
        url (str): Please set to https://developer.nvidia.com/cuda-gpus.
        save_json (str): File name to save the json data.
    """
    console = Console(log_time=False, log_path=False)
    counter = 1
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'lxml')
    data = {}
    panel_group = soup.select('div.panel-group>div.panel')
    for panel in panel_group:
        panel_heading = panel.select_one('div.panel-heading>h3>a')
        panel_heading = panel_heading.contents[1].strip()
        data[panel_heading] = {}
        panel_collapse = panel.select(
            'div.panel-collapse div.col-md-6,div.col-md-12')
        for sub_panel in panel_collapse:
            sub_panel_heading = sub_panel.select_one('h3>a').string
            data[panel_heading][sub_panel_heading] = {}
            table = sub_panel.select_one('table.table')
            thead = table.select('thead>tr>th')
            tbody = table.select('tbody>tr>td')
            thead = [item.string.strip() for item in thead]
            tbody = [next(item.stripped_strings) for item in tbody]
            for k, v in zip(thead, [tbody[0::2], tbody[1::2]]):
                data[panel_heading][sub_panel_heading][k] = v
            console.log(
                f'task {counter} complete: {panel_heading} -> {sub_panel_heading}')
            counter += 1
    with open(save_json, 'w') as fp:
        json.dump(data, fp)


if __name__ == '__main__':
    spider('https://developer.nvidia.com/cuda-gpus', 'data/cuda-gpus.json')

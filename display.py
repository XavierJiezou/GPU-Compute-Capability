import json
from rich.table import Table
from rich.console import Console


def display(fname: str):
    """Display the data in a tabular manner.

    Args:
        fname (str): File name to the json data.
    """
    with open(fname) as fp:
        data = json.load(fp)
    console = Console()
    for i in data:
        for j in data[i]:
            table = Table(title=f'{i}\n{j}', title_justify='left')
            for k in data[i][j]:
                table.add_column(k)
            m_list = data[i][j]['GPU']
            n_list = data[i][j]['Compute Capability']
            for m, n in zip(m_list, n_list):
                table.add_row(m, n)
            console.print(table)


if __name__ == '__main__':
    display('cuda-gpus.json')

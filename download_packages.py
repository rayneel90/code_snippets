import pandas as pd
import subprocess
df = pd.read_csv('data/all_python_packages.csv')


lst = df[df.total_downloads > 100].file_project.tolist()
while 1:
    i = lst.pop()
    subprocess.call('pip download -d E:/pip_cache/ '+i, shell=True)


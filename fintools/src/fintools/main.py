import os
import subprocess
from typing import Optional

from .utils import streamlit_runner


class Main:

    @staticmethod
    def hello(name: Optional[str] = None) -> str:
        if name is None:
            name = "world"
        return f"Hello, {name}!"

    @staticmethod
    def streamlit(app_file: str):
        streamlit_runner(app_file=app_file)

    @staticmethod
    def console(disable_winpty: bool = False):
        cmd = "ipython"
        if os.name != "posix" and not disable_winpty:
            cmd = f"winpty {cmd}"
        return subprocess.run(cmd, shell=True, check=True, env=None)

    @staticmethod
    def notebook(port: int = 9999, no_browser: bool = False):
        cmd = f"jupyter-notebook --port {port}"
        if no_browser:
            cmd += " --no-browser"
        return os.system(cmd)

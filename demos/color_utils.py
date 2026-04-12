"""
彩色日志输出工具模块
支持跨平台彩色终端输出（Windows、macOS、Linux）
使用ANSI颜色编码，在Windows上通过colorama自动处理

作者: Crab Agent Core Team
日期: 2026-04-13
"""

import sys
from typing import Any


class Color:
    """ANSI颜色编码常量"""
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"
    
    BRIGHT_BLACK = "\033[90m"
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_WHITE = "\033[97m"


def init_color() -> None:
    """
    初始化颜色支持
    在Windows上使用colorama启用ANSI颜色
    """
    if sys.platform == "win32":
        try:
            import colorama
            colorama.init()
        except ImportError:
            pass


def colored(text: str, color: str) -> str:
    """
    将文本包装在指定颜色代码中
    
    参数:
        text: 要着色的文本
        color: 颜色代码（来自Color类）
    
    返回:
        带有颜色编码的文本
    """
    return f"{color}{text}{Color.RESET}"


def print_colored(text: str, color: str, **kwargs: Any) -> None:
    """
    打印彩色文本
    
    参数:
        text: 要打印的文本
        color: 颜色代码（来自Color类）
        **kwargs: 传递给print函数的其他参数
    """
    print(colored(text, color), **kwargs)


def print_info(text: str, **kwargs: Any) -> None:
    """打印信息类消息（青色）"""
    print_colored(text, Color.CYAN, **kwargs)


def print_success(text: str, **kwargs: Any) -> None:
    """打印成功类消息（绿色）"""
    print_colored(text, Color.GREEN, **kwargs)


def print_warning(text: str, **kwargs: Any) -> None:
    """打印警告类消息（黄色）"""
    print_colored(text, Color.YELLOW, **kwargs)


def print_error(text: str, **kwargs: Any) -> None:
    """打印错误类消息（红色）"""
    print_colored(text, Color.RED, **kwargs)


def print_header(text: str, char: str = "=", width: int = 60) -> None:
    """
    打印带边框的标题
    
    参数:
        text: 标题文本
        char: 边框字符
        width: 标题宽度
    """
    line = char * width
    print_colored(line, Color.BOLD + Color.BLUE)
    print_colored(text.center(width), Color.BOLD + Color.BRIGHT_BLUE)
    print_colored(line, Color.BOLD + Color.BLUE)


def print_section(text: str, char: str = "─", width: int = 60) -> None:
    """
    打印带边框的节标题
    
    参数:
        text: 节标题文本
        char: 边框字符
        width: 标题宽度
    """
    line = char * width
    print()
    print_colored(line, Color.MAGENTA)
    print_colored(text.center(width), Color.BOLD + Color.BRIGHT_MAGENTA)
    print_colored(line, Color.MAGENTA)


init_color()

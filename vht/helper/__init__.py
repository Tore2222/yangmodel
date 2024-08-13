from functools import wraps
from pprint import pprint
from typing import Any, Dict, Optional
from xml.etree import ElementTree
from xml.dom import minidom
import inspect

debug_function_level = 0
debug_enable = True

def inspect_classname(method):
    if hasattr(method, 'im_class'):
        for _cls in inspect.getmro(method.im_class):
            if method.__name__ in _cls.__dict__:
                return _cls
    return None

def inspect_functionname(method):
    classname = inspect_classname(method)
    return F"{classname}.<{method.__name__}>" if classname else F"<{method.__name__}>"

def debug_line(format):
    if debug_enable:
        print(debug_function_level * '\t' + str(format))

def debug_function(log_enter=False, log_exit=False, log_return=False):
    def wrapper_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            global debug_function_level, debug_enable

            if debug_enable:
                funcstr = inspect_functionname(func)

                if log_enter:
                    debug_line(F"[ENTER]: {funcstr}")

                debug_function_level += 1

            result = func(*args, **kwargs)

            if debug_enable:

                debug_function_level -= 1

                if log_exit and log_return:
                    debug_line(f"[EXIT ]: {funcstr} [RETURN]: {result}")
                elif log_exit:
                    debug_line(f"[EXIT ]: {funcstr}")

            return result
        return wrapper
    return wrapper_decorator

def casting(cast_function=None, default=None):
    def wrapper_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                return cast_function(result)
            except Exception:
                return default
        return wrapper
    return wrapper_decorator

def search_by_path(data, keys, default=None):
    res = data
    for key in keys:
        res = res.get(key, {})
        if not res:
            return default
    if not res:
        return default
    return res

def get_pretty_xml(elm):
    xmlb = ElementTree.tostring(elm, encoding='unicode')
    xmlstr = minidom.parseString(xmlb).toprettyxml(indent="   ")
    return xmlstr

def same_config_cli(candidate, running):
    return candidate == running
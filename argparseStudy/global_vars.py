import argparse
_GLOBAL_VARS = None
import os
print(os.path.abspath('.'))
import sys
sys.path.append('..')
print(sys.path)
print(__file__)
print(os.path.dirname(__file__)) # 不能在交互式shell中运行__file__

def parse_args():
    parser = argparse.ArgumentParser(description='EasyNLP Arguments',
                                     allow_abbrev=False)
    parser.add_argument(
        '--haha',
        type=int,
        default=0,
        help='Random seed used for python, numpy, pytorch, and cuda.'
    )
    group = parser.add_argument_group(title='easynlp')
    group.add_argument(
        '--random_seed',
        type=int,
        default=1234,
        help='Random seed used for python, numpy, pytorch, and cuda.'
    )
    args = parser.parse_args()
    return args

def _parse_args():
    global _GLOBAL_VARS
    
    _GLOBAL_VARS = parse_args()
    return _GLOBAL_VARS

def set_global_variables():
    args = _parse_args()


def _ensure_var_is_initialized(var, name):
    """Make sure the input variable is not None."""
    assert var is not None, '{} is not initialized.'.format(name)
    
def get_args():
    """Return arguments."""
    _ensure_var_is_initialized(_GLOBAL_VARS, 'vars')
    return _GLOBAL_VARS
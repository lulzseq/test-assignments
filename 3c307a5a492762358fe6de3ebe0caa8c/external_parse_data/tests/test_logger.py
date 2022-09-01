import pytest
from ..packages.logger import *

logger = logging.getLogger(__name__)

fixtures = {
    'msg': ['test', '@#$%^&', 111]
}


@pytest.mark.parametrize('msg', fixtures['msg'])
def test_logger(msg):
    result = log(msg)
    assert isinstance(type(result), type(None))

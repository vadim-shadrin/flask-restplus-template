import pytest

from mb_api import create_app
from tests.settings import TestConfig


@pytest.fixture(scope='module')
def test_app():
    """
    get test app
    """
    app = create_app(TestConfig)
    with app.app_context():
        yield app

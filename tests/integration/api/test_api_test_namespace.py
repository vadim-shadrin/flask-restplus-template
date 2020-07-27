import json

from fixtures import *


class TestTestNamespace:
    def test_test_namespace_root_endpoint(self, test_app):
        endpoint = '/v1/test_namespace/'
        with test_app.test_client() as client:
            result = client.get(endpoint,
                                content_type='application/json',
                                follow_redirects=True)
            assert result.status_code == 200
            assert json.loads(result.data.decode()) == {"data": "some text for example"}

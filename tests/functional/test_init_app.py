class TestSanityCheck:
    def test_sanity_check(self, test_app):
        endpoint = '/health_check'

        with test_app.test_client() as client:
            result = client.get(endpoint)
            assert result.status_code == 200
            assert result.data == b'OK'


class TestInitApi:
    def test_init_api(self, test_app):
        endpoint = '/v1/'

        with test_app.test_client() as client:
            result = client.get(endpoint)
            assert result.status_code == 200

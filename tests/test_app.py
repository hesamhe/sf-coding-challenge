from app import get_total_pages
from app import get_user_list
import unittest
from unittest import mock

# Mock requests.get() to return a mock response object
def mocked_requests_get(*args):
    class MockResponse:
        def __init__(self, json_data):
            self.json_data = json_data

        def json(self):
            return self.json_data

    if args[0] == 'https://reqres.in/api/users':
        return MockResponse(
            {
                "page": 1,
                "per_page": 6,
                "total": 12,
                "total_pages": 2,
                "data": [
                    {
                        "id": 1,
                        "email": "george.bluth@reqres.in",
                        "first_name": "George",
                        "last_name": "Bluth",
                        "avatar": "https://reqres.in/img/faces/1-image.jpg"}],
                "support": {
                    "url": "https://reqres.in/#support-heading",
                    "text": "To keep ReqRes free, contributions towards server costs are appreciated!"}})
    elif args[0] == 'https://reqres.in/api/users?page=1':
        return MockResponse(
            {
                "page": 1,
                "per_page": 6,
                "total": 12,
                "total_pages": 2,
                "data": [
                    {
                        "id": 1,
                        "email": "george.bluth@reqres.in",
                        "first_name": "George",
                        "last_name": "Bluth",
                        "avatar": "https://reqres.in/img/faces/1-image.jpg"}],
                "support": {
                    "url": "https://reqres.in/#support-heading",
                    "text": "To keep ReqRes free, contributions towards server costs are appreciated!"}})

    return MockResponse(None, 404)

# Test get_user_list() function
class TotalPagesTestCase(unittest.TestCase):

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_total_pages(self, mock_get):

        self.assertEqual(get_total_pages(), 2)

# Test total_pages() function
class UserListTestCase(unittest.TestCase):

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_user_list(self, mock_get):

        self.assertEqual(get_user_list(1),
                         [{"id": 1,
                           "email": "george.bluth@reqres.in",
                           "first_name": "George",
                           "last_name": "Bluth",
                           "avatar": "https://reqres.in/img/faces/1-image.jpg"}])

# Run tests
if __name__ == '__main__':
    unittest.main()

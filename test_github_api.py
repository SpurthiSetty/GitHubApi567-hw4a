import pytest
from unittest.mock import patch
import github_api  # Import the function to be tested

class MockResponse:
    """Mock class for simulating API responses"""
    def __init__(self, json_data, status_code, reason=""):
        self.json_data = json_data
        self.status_code = status_code
        self.reason = reason  # Add the reason attribute

    def json(self):
        return self.json_data

    def raise_for_status(self):
        if self.status_code != 200:
            raise Exception(f"Error: {self.status_code} - {self.reason}")


@patch('github_api.requests.get')
def test_get_github_repos_and_commits(mock_get):
    """Test if function correctly retrieves repositories and commit counts"""
    mock_get.side_effect = [
        MockResponse([{"name": "Repo1"}, {"name": "Repo2"}], 200),  # Repo list response
        MockResponse([{"sha": "commit1"}, {"sha": "commit2"}], 200),  # Repo1 commits response
        MockResponse([{"sha": "commit1"}, {"sha": "commit2"}], 200),  # Repo2 commits response
    ]

    expected_output = (
        "Repo: Repo1 Number of commits: 2\n"
        "Repo: Repo2 Number of commits: 2"
    )

    result = github_api.get_github_repos_and_commits("testuser")
    assert result == expected_output

# @patch('github_api.requests.get')
# def test_invalid_user(mock_get):
#     """Test function handling of an invalid user (expecting an error message)"""
#     mock_get.return_value = MockResponse(None, 404)  # Simulate 404 error response

#     result = github_api.get_github_repos_and_commits("invalid_user")
#     assert "Error" in result
@patch('github_api.requests.get')
def test_invalid_user(mock_get):
    """Test function handling of an invalid user (expecting an error message)"""
    mock_get.return_value = MockResponse(None, 404, "Not Found")  # Provide a reason for the 404 error

    result = github_api.get_github_repos_and_commits("invalid_user")
    assert "Error: 404 - Not Found" in result  # Now expecting the full error message

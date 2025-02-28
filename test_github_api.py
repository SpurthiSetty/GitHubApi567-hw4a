import unittest
from unittest.mock import patch, MagicMock
import github_api  # Replace with your actual module name
import requests

class TestGitHubAPI(unittest.TestCase):
    
    @patch('github_api.requests.get')  # Mock requests.get globally for this test class
    def test_get_github_repos_and_commits_success(self, mock_get):
        """Test fetching repositories and commit counts successfully"""

        # Mock responses for repository list
        mock_repos_response = MagicMock()
        mock_repos_response.status_code = 200
        mock_repos_response.json.return_value = [
            {"name": "repo1"},
            {"name": "repo2"}
        ]

        # Mock responses for commit list
        mock_commits_response = MagicMock()
        mock_commits_response.status_code = 200
        mock_commits_response.json.side_effect = [
            [{"sha": "123"}, {"sha": "456"}],  # Two commits for repo1
            [{"sha": "789"}]  # One commit for repo2
        ]

        # Arrange the mock calls
        mock_get.side_effect = [mock_repos_response, mock_commits_response, mock_commits_response]

        # Act
        result = github_api.get_github_repos_and_commits("test-user")

        # Assert
        expected_output = "Repo: repo1 Number of commits: 2\nRepo: repo2 Number of commits: 1"
        self.assertEqual(result, expected_output)

    @patch('github_api.requests.get')
    def test_get_github_repos_and_commits_api_error(self, mock_get):
        """Test handling of GitHub API errors"""

        # Mock repository list response with an error
        mock_repos_response = MagicMock()
        mock_repos_response.status_code = 403
        mock_repos_response.reason = "Forbidden"
        mock_get.return_value = mock_repos_response

        # Act
        result = github_api.get_github_repos_and_commits("test-user")

        # Assert
        self.assertEqual(result, "Error: 403 - Forbidden")

    @patch('github_api.requests.get')
    def test_get_github_repos_and_commits_commits_api_error(self, mock_get):
        """Test handling of commit API errors when fetching commits for a repo"""

        # Mock repository list response
        mock_repos_response = MagicMock()
        mock_repos_response.status_code = 200
        mock_repos_response.json.return_value = [{"name": "repo1"}]

        # Mock commit list response with an error
        mock_commits_response = MagicMock()
        mock_commits_response.status_code = 404
        mock_commits_response.reason = "Not Found"

        # Arrange the mock calls
        mock_get.side_effect = [mock_repos_response, mock_commits_response]

        # Act
        result = github_api.get_github_repos_and_commits("test-user")

        # Assert
        self.assertEqual(result, "Error: 404 - Not Found")

    @patch('github_api.requests.get')
    def test_get_github_repos_and_commits_request_exception(self, mock_get):
        """Test handling of a network error"""
        mock_get.side_effect = requests.exceptions.RequestException("Network Error")

        result = github_api.get_github_repos_and_commits("test-user")

        self.assertEqual(result, "Error: Network Error")


if __name__ == "__main__":
    unittest.main()

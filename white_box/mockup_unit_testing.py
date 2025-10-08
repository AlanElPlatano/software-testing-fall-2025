# -*- coding: utf-8 -*-
"""
Mock up testing examples.
"""
import unittest
from unittest.mock import MagicMock, mock_open, patch

from white_box.mockup_exercises import (
    execute_command,
    fetch_data_from_api,
    perform_action_based_on_time,
    read_data_from_file,
)


class TestDataFetcher(unittest.TestCase):
    """
    Data fetcher unittest class.
    """

    @patch("white_box.mockup_exercises.requests.get")
    def test_fetch_data_from_api_success(self, mock_get):
        """
        Success case for fetching data from API.
        """
        # Set up the mock response
        mock_get.return_value.json.return_value = {"key": "value"}

        # Call the function under test
        result = fetch_data_from_api("https://api.example.com/data")

        # Assert that the function returns the expected result
        self.assertEqual(result, {"key": "value"})

        # Assert that requests.get was called with the correct URL and timeout
        mock_get.assert_called_once_with("https://api.example.com/data", timeout=10)

    @patch("white_box.mockup_exercises.requests.get")
    def test_fetch_data_from_api_with_list_response(self, mock_get):
        """
        Test fetching data that returns a list.
        """
        # Set up the mock response with a list
        mock_get.return_value.json.return_value = [
            {"id": 1, "title": "Title 1"},
            {"id": 2, "title": "Title 2"},
        ]

        # Call the function under test
        result = fetch_data_from_api("https://api.example.com/posts")

        # Assert that the function returns the expected result
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["id"], 1)
        mock_get.assert_called_once_with("https://api.example.com/posts", timeout=10)


class TestReadDataFromFile(unittest.TestCase):
    """
    File reading unittest class.
    """

    @patch("builtins.open", new_callable=mock_open, read_data="test file content")
    def test_read_data_from_file_success(self, mock_file):
        """
        Test successful file reading.
        """
        # Call the function under test
        result = read_data_from_file("test.txt")

        # Assert that the function returns the expected content
        self.assertEqual(result, "test file content")

        # Assert that open was called with the correct filename and encoding
        mock_file.assert_called_once_with("test.txt", encoding="utf-8")

    @patch("builtins.open", side_effect=FileNotFoundError("File not found"))
    def test_read_data_from_file_not_found(self, mock_file):
        """
        Test file reading when file doesn't exist.
        """
        # Assert that FileNotFoundError is raised
        with self.assertRaises(FileNotFoundError):
            read_data_from_file("nonexistent.txt")

        # Assert that open was called with the correct filename
        mock_file.assert_called_once_with("nonexistent.txt", encoding="utf-8")

    @patch("builtins.open", new_callable=mock_open, read_data="line1\nline2\nline3")
    def test_read_data_from_file_multiline(self, mock_file):
        """
        Test reading multiline file content.
        """
        # Call the function under test
        result = read_data_from_file("multiline.txt")

        # Assert that the function returns all lines
        self.assertEqual(result, "line1\nline2\nline3")
        mock_file.assert_called_once_with("multiline.txt", encoding="utf-8")


class TestExecuteCommand(unittest.TestCase):
    """
    Command execution unittest class.
    """

    @patch("white_box.mockup_exercises.subprocess.run")
    def test_execute_command_success(self, mock_run):
        """
        Test successful command execution.
        """
        # Set up the mock result
        mock_result = MagicMock()
        mock_result.stdout = "command output"
        mock_run.return_value = mock_result

        # Call the function under test
        result = execute_command(["echo", "hello"])

        # Assert that the function returns the expected output
        self.assertEqual(result, "command output")

        # Assert that subprocess.run was called with correct parameters
        mock_run.assert_called_once_with(
            ["echo", "hello"], capture_output=True, check=False, text=True
        )

    @patch("white_box.mockup_exercises.subprocess.run")
    def test_execute_command_empty_output(self, mock_run):
        """
        Test command execution with empty output.
        """
        # Set up the mock result with empty stdout
        mock_result = MagicMock()
        mock_result.stdout = ""
        mock_run.return_value = mock_result

        # Call the function under test
        result = execute_command(["ls", "-l"])

        # Assert that the function returns empty string
        self.assertEqual(result, "")
        mock_run.assert_called_once()

    @patch("white_box.mockup_exercises.subprocess.run")
    def test_execute_command_with_multiple_args(self, mock_run):
        """
        Test command execution with multiple arguments.
        """
        # Set up the mock result
        mock_result = MagicMock()
        mock_result.stdout = "file1.txt\nfile2.txt"
        mock_run.return_value = mock_result

        # Call the function under test
        result = execute_command(["ls", "-la", "/tmp"])

        # Assert that the function returns the expected output
        self.assertEqual(result, "file1.txt\nfile2.txt")

        # Assert that subprocess.run was called with all arguments
        mock_run.assert_called_once_with(
            ["ls", "-la", "/tmp"], capture_output=True, check=False, text=True
        )


class TestPerformActionBasedOnTime(unittest.TestCase):
    """
    Time-based action unittest class.
    """

    @patch("white_box.mockup_exercises.time.time")
    def test_perform_action_when_time_less_than_10(self, mock_time):
        """
        Test action when current time is less than 10.
        """
        # Set up the mock to return a time less than 10
        mock_time.return_value = 5.0

        # Call the function under test
        result = perform_action_based_on_time()

        # Assert that "Action A" is returned
        self.assertEqual(result, "Action A")
        mock_time.assert_called_once()

    @patch("white_box.mockup_exercises.time.time")
    def test_perform_action_when_time_equals_10(self, mock_time):
        """
        Test action when current time equals 10.
        """
        # Set up the mock to return exactly 10
        mock_time.return_value = 10.0

        # Call the function under test
        result = perform_action_based_on_time()

        # Assert that "Action B" is returned (boundary condition)
        self.assertEqual(result, "Action B")
        mock_time.assert_called_once()

    @patch("white_box.mockup_exercises.time.time")
    def test_perform_action_when_time_greater_than_10(self, mock_time):
        """
        Test action when current time is greater than 10.
        """
        # Set up the mock to return a time greater than 10
        mock_time.return_value = 1000000.0

        # Call the function under test
        result = perform_action_based_on_time()

        # Assert that "Action B" is returned
        self.assertEqual(result, "Action B")
        mock_time.assert_called_once()

    @patch("white_box.mockup_exercises.time.time")
    def test_perform_action_when_time_is_zero(self, mock_time):
        """
        Test action when current time is zero (edge case).
        """
        # Set up the mock to return zero
        mock_time.return_value = 0.0

        # Call the function under test
        result = perform_action_based_on_time()

        # Assert that "Action A" is returned
        self.assertEqual(result, "Action A")
        mock_time.assert_called_once()


if __name__ == "__main__":
    unittest.main()

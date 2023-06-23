import unittest
from unittest.mock import Mock
from app.main.dataAccess.queryDao import QueryDao
from app.main.utils.prompt import Prompt
from openai import ChatCompletion
from app.main.service.textOperationService import TextOperationService

class TestTextOperationService(unittest.TestCase):
    def setUp(self):
        self.queryDao = Mock(spec=QueryDao)
        self.prompt = Mock(spec=Prompt)
        self.chatCompletion = Mock(spec=ChatCompletion)
        self.maxToken = 1024

        self.service = TextOperationService(
            queryDao=self.queryDao,
            prompt=self.prompt,
            chatCompletion=self.chatCompletion,
            maxToken=self.maxToken
        )

    def tearDown(self):
        self.queryDao = None
        self.prompt = None
        self.chatCompletion = None
        self.maxToken = None

        self.service = None
        
    def test_getSummarizeContent_with_empty_content(self):
        content = ""
        operation = "summarize_content"
        expected_result = {"error": "Content is empty."}
        expected_status_code = 400

        result, status_code = self.service.getSummarizeContent(content)
        
        self.assertEqual(result, expected_result)
        self.assertEqual(status_code, expected_status_code)
        self.queryDao.getByRequest.assert_called_once_with(operation, content)
        self.prompt.getTokenCount.assert_called_once_with(content)
        self.chatCompletion.create.assert_not_called()
        self.queryDao.addQuery.assert_not_called()

    def test_getSummarizeContent_with_existing_query(self):
        content = "Lorem ipsum dolor sit amet."
        operation = "summarize_content"
        query = "Lorem ipsum"
        self.queryDao.getByRequest.return_value = query
        expected_result = {"result": query, "message": "Request exists in cache"}
        expected_status_code = 200

        result, status_code = self.service.getSummarizeContent(content)

        self.assertEqual(result, expected_result)
        self.assertEqual(status_code, expected_status_code)
        self.queryDao.getByRequest.assert_called_once_with(operation, content)
        self.prompt.getTokenCount.assert_called_once_with(content)
        self.chatCompletion.create.assert_not_called()
        self.queryDao.addQuery.assert_not_called()

    def test_getSummarizeContent_within_token_limit(self):
        content = "Lorem ipsum dolor sit amet."
        operation = "summarize_content"
        token_count = 5
        result = "Lorem ispum"
        message = "Successfully sent a request to the OpenAI Api"

        expected_result = {"result": result, "message": message}
        expected_status_code = 200

        self.prompt.getSummarizeContentPrompt.return_value = {
            "messages": content
        }

        self.prompt.getTokenCount.return_value = token_count
        self.queryDao.getByRequest.return_value = None

        response = Mock()
        response.choices = [Mock()]
        response.choices[0].message.content = result
        self.chatCompletion.create.return_value = response

        result, status_code = self.service.getSummarizeContent(content)

        self.assertEqual(result, expected_result)
        self.assertEqual(status_code, expected_status_code)
        self.queryDao.getByRequest.assert_called_once_with(operation, content)
        self.prompt.getTokenCount.assert_called_once_with(content)
        self.chatCompletion.create.assert_called_once_with(**self.prompt.getSummarizeContentPrompt.return_value)
        self.queryDao.addQuery.assert_called()

    def test_getSummarizeContent_exceeding_token_limit(self):
        content = "Lorem ipsum dolor sit amet."
        operation = "summarize_content"
        token_count = 1500
        self.prompt.getTokenCount.return_value = token_count
        expected_result = {"error": f"Your request {token_count} tokens exceeds the max token count of {self.maxToken}."}
        expected_status_code = 400
        self.queryDao.getByRequest.return_value = None

        result, status_code = self.service.getSummarizeContent(content)

        self.assertEqual(result, expected_result)
        self.assertEqual(status_code, expected_status_code)
        self.queryDao.getByRequest.assert_called_once_with(operation, content)
        self.prompt.getTokenCount.assert_called_once_with(content)
        self.chatCompletion.create.assert_not_called()
        self.queryDao.addQuery.assert_not_called()

    def test_getFixTypos_with_empty_content(self):
        content = ""
        operation = "fix_typos"
        expected_result = {"error": "Content is empty."}
        expected_status_code = 400

        result, status_code = self.service.getFixTypos(content)
        
        self.assertEqual(result, expected_result)
        self.assertEqual(status_code, expected_status_code)
        self.queryDao.getByRequest.assert_called_once_with(operation, content)
        self.prompt.getTokenCount.assert_called_once_with(content)
        self.chatCompletion.create.assert_not_called()
        self.queryDao.addQuery.assert_not_called()

    def test_getFixTypos_with_existing_query(self):
        content = "Lorem ipsum dolor sit amet."
        operation = "fix_typos"
        query = "Lorem ipsum"
        self.queryDao.getByRequest.return_value = query
        expected_result = {"result": query, "message": "Request exists in cache"}
        expected_status_code = 200

        result, status_code = self.service.getFixTypos(content)

        self.assertEqual(result, expected_result)
        self.assertEqual(status_code, expected_status_code)
        self.queryDao.getByRequest.assert_called_once_with(operation, content)
        self.prompt.getTokenCount.assert_called_once_with(content)
        self.chatCompletion.create.assert_not_called()
        self.queryDao.addQuery.assert_not_called()

    def test_getFixTypos_within_token_limit(self):
        content = "Lorem ipsum dolor sit amet."
        operation = "fix_typos"
        token_count = 5
        result = "Lorem ispum"
        message = "Successfully sent a request to the OpenAI Api"

        expected_result = {"result": result, "message": message}
        expected_status_code = 200

        self.prompt.getFixTyposPrompt.return_value = {
            "messages": content
        }

        self.prompt.getTokenCount.return_value = token_count
        self.queryDao.getByRequest.return_value = None

        response = Mock()
        response.choices = [Mock()]
        response.choices[0].message.content = result
        self.chatCompletion.create.return_value = response

        result, status_code = self.service.getFixTypos(content)

        self.assertEqual(result, expected_result)
        self.assertEqual(status_code, expected_status_code)
        self.queryDao.getByRequest.assert_called_once_with(operation, content)
        self.prompt.getTokenCount.assert_called_once_with(content)
        self.chatCompletion.create.assert_called_once_with(**self.prompt.getFixTyposPrompt.return_value)
        self.queryDao.addQuery.assert_called()

    def test_getFixTypos_exceeding_token_limit(self):
        content = "Lorem ipsum dolor sit amet."
        operation = "fix_typos"
        token_count = 1500
        self.prompt.getTokenCount.return_value = token_count
        expected_result = {"error": f"Your request {token_count} tokens exceeds the max token count of {self.maxToken}."}
        expected_status_code = 400
        self.queryDao.getByRequest.return_value = None

        result, status_code = self.service.getFixTypos(content)

        self.assertEqual(result, expected_result)
        self.assertEqual(status_code, expected_status_code)
        self.queryDao.getByRequest.assert_called_once_with(operation, content)
        self.prompt.getTokenCount.assert_called_once_with(content)
        self.chatCompletion.create.assert_not_called()
        self.queryDao.addQuery.assert_not_called()

    def test_getExplainCode_with_empty_content(self):
        content = ""
        operation = "explain_code"
        expected_result = {"error": "Content is empty."}
        expected_status_code = 400

        result, status_code = self.service.getExplainCode(content)
        
        self.assertEqual(result, expected_result)
        self.assertEqual(status_code, expected_status_code)
        self.queryDao.getByRequest.assert_called_once_with(operation, content)
        self.prompt.getTokenCount.assert_called_once_with(content)
        self.chatCompletion.create.assert_not_called()
        self.queryDao.addQuery.assert_not_called()

    def test_getExplainCode_with_existing_query(self):
        content = "Lorem ipsum dolor sit amet."
        operation = "explain_code"
        query = "Lorem ipsum"
        self.queryDao.getByRequest.return_value = query
        expected_result = {"result": query, "message": "Request exists in cache"}
        expected_status_code = 200

        result, status_code = self.service.getExplainCode(content)

        self.assertEqual(result, expected_result)
        self.assertEqual(status_code, expected_status_code)
        self.queryDao.getByRequest.assert_called_once_with(operation, content)
        self.prompt.getTokenCount.assert_called_once_with(content)
        self.chatCompletion.create.assert_not_called()
        self.queryDao.addQuery.assert_not_called()

    def test_getExplainCode_within_token_limit(self):
        content = "Lorem ipsum dolor sit amet."
        operation = "explain_code"
        token_count = 5
        result = "Lorem ispum"
        message = "Successfully sent a request to the OpenAI Api"

        expected_result = {"result": result, "message": message}
        expected_status_code = 200

        self.prompt.getExplainCodePrompt.return_value = {
            "messages": content
        }

        self.prompt.getTokenCount.return_value = token_count
        self.queryDao.getByRequest.return_value = None

        response = Mock()
        response.choices = [Mock()]
        response.choices[0].message.content = result
        self.chatCompletion.create.return_value = response

        result, status_code = self.service.getExplainCode(content)

        self.assertEqual(result, expected_result)
        self.assertEqual(status_code, expected_status_code)
        self.queryDao.getByRequest.assert_called_once_with(operation, content)
        self.prompt.getTokenCount.assert_called_once_with(content)
        self.chatCompletion.create.assert_called_once_with(**self.prompt.getExplainCodePrompt.return_value)
        self.queryDao.addQuery.assert_called()

    def test_getExplainCode_exceeding_token_limit(self):
        content = "Lorem ipsum dolor sit amet."
        operation = "explain_code"
        token_count = 1500
        self.prompt.getTokenCount.return_value = token_count
        expected_result = {"error": f"Your request {token_count} tokens exceeds the max token count of {self.maxToken}."}
        expected_status_code = 400
        self.queryDao.getByRequest.return_value = None

        result, status_code = self.service.getExplainCode(content)

        self.assertEqual(result, expected_result)
        self.assertEqual(status_code, expected_status_code)
        self.queryDao.getByRequest.assert_called_once_with(operation, content)
        self.prompt.getTokenCount.assert_called_once_with(content)
        self.chatCompletion.create.assert_not_called()
        self.queryDao.addQuery.assert_not_called()

if __name__ == "__main__":
    unittest.main()
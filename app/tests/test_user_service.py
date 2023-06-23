import unittest
from unittest.mock import Mock, patch
from app.main.dataAccess.userDao import UserDao
from app.main.service.userService import UserService

class TestUserService(unittest.TestCase):
    def setUp(self):
        self.userDao = Mock(spec=UserDao)

        self.service = UserService(
            userDao=self.userDao,
        )

    def tearDown(self):
        self.userDao = None
        self.service = None

    @patch("app.main.service.userService.generate_password_hash")
    @patch("app.main.service.userService.create_access_token")
    def test_signUp_success(self, mock_create_access_token, mock_generate_password_hash):
        email = "test@example.com"
        password = "password123"
        message = "Successfully registered"
        accessToken = "mocked_access_token"
        hashedPassword = "mocked_hashed_password"
        expected_result = {"access_token": accessToken, "message": message}
        expected_status_code = 200

        mock_generate_password_hash.return_value = hashedPassword
        mock_create_access_token.return_value = accessToken
        self.userDao.getByEmail.return_value = None

        result, status_code = self.service.signUp(email, password)

        self.assertEqual(result, expected_result)
        self.assertEqual(status_code, expected_status_code)
        self.userDao.getByEmail.assert_called_once_with(email)
        self.userDao.addUser.assert_called_once()

    def test_signUp_email_already_registered(self):
        email = "test@example.com"
        password = "password123"
        message = "The e-mail address is already registered."
        expected_result = {"error": message}
        expected_status_code = 400

        self.userDao.getByEmail.return_value = {"email": email, "password": password}

        result, status_code = self.service.signUp(email, password)

        self.assertEqual(result, expected_result)
        self.assertEqual(status_code, expected_status_code)
        self.userDao.getByEmail.assert_called_once_with(email)
        self.userDao.addUser.assert_not_called()

    def test_signUp_missing_fields(self):
        email = ""
        password = ""
        message = "Email and password fields are required."
        expected_result = {"error": message}
        expected_status_code = 400
    
        result, status_code = self.service.signUp(email, password)

        self.assertEqual(result, expected_result)
        self.assertEqual(status_code, expected_status_code)
        self.userDao.getByEmail.assert_not_called()
        self.userDao.addUser.assert_not_called()

    @patch("app.main.service.userService.check_password_hash")
    @patch("app.main.service.userService.create_access_token")
    def test_logIn_success(self, mock_create_access_token, mock_check_password_hash):
        email = "test@example.com"
        password = "123"
        message = "Successfully logged in"
        accessToken = "mocked_access_token"
        checkPasswordReturnValue = True

        self.userDao.getByEmail.return_value = {"email": email}        
        mock_check_password_hash.return_value = checkPasswordReturnValue
        mock_create_access_token.return_value = accessToken

        expected_result = {"access_token": accessToken, "message": message}
        expected_status_code = 200

        result, status_code = self.service.logIn(email, password)

        self.assertEqual(result, expected_result)
        self.assertEqual(status_code, expected_status_code)
        self.userDao.getByEmail.assert_called_once_with(email)
        mock_check_password_hash.assert_called_once()
        mock_create_access_token.assert_called_once()

    @patch("app.main.service.userService.check_password_hash")
    def test_logIn_invalid_credentials(self, mock_check_password_hash):
        email = "test@example.com"
        password = "password123"
        message = "Email or password is incorrect."
        checkPasswordReturnValue = False

        self.userDao.getByEmail.return_value = {"email": email}        
        mock_check_password_hash.return_value = checkPasswordReturnValue

        expected_result = {"error": message}
        expected_status_code = 401

        result, status_code = self.service.logIn(email, password)

        self.assertEqual(result, expected_result)
        self.assertEqual(status_code, expected_status_code)
        self.userDao.getByEmail.assert_called_once_with(email)
        mock_check_password_hash.assert_called_once()

    def test_logIn_missing_fields(self):
        email = ""
        password = ""
        message = "Email and password fields are required."
        expected_result = {"error": message}
        expected_status_code = 400
    
        result, status_code = self.service.logIn(email, password)

        self.assertEqual(result, expected_result)
        self.assertEqual(status_code, expected_status_code)
        self.userDao.getByEmail.assert_not_called()
        self.userDao.addUser.assert_not_called()

    @patch("app.main.service.userService.generate_password_hash")
    def test_updateUser_password_success(self, mock_generate_password_hash):
        user = {"_id": 1, "email": "test@example.com"}
        updated_data = {"password": "new_password"}
        message = "User updated."
        hashedPassword = "mocked_hashed_password"

        mock_generate_password_hash.return_value = hashedPassword

        expected_result = {"message": message}
        expected_status_code = 200
    
        result, status_code = self.service.updateUser(user, updated_data)

        self.assertEqual(result, expected_result)
        self.assertEqual(status_code, expected_status_code)
        self.userDao.updateUser.assert_called_once_with(user["_id"], user, updated_data)

    def test_updateUser_password_user_not_found(self):
        user = None
        updated_data = {"email": "new_email"}
        message = "User not found."
        hashedPassword = "mocked_hashed_password"

        expected_result = {"error": message}
        expected_status_code = 404
    
        result, status_code = self.service.updateUser(user, updated_data)

        self.assertEqual(result, expected_result)
        self.assertEqual(status_code, expected_status_code)
        self.userDao.updateUser.assert_not_called()

if __name__ == "__main__":
    unittest.main()

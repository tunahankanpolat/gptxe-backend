from app.main.model.user import User

def test_constructor_with_required_attributes():
    user = User("user@example.com", "password")
    assert user.email == "user@example.com"
    assert user.password == "password"
    assert user.apiKey is None
    assert user.subscription == False
    assert user.languagePreference is None

def test_constructor_with_all_attributes():
    user = User("user@example.com", "password", apiKey="123456789", languagePreference="English")
    assert user.email == "user@example.com"
    assert user.password == "password"
    assert user.apiKey == "123456789"
    assert user.subscription == False
    assert user.languagePreference == "English"

def test_toString():
    user = User("user@example.com", "password", apiKey="123456789", languagePreference="English")
    user_dict = user.toString()
    assert user_dict["email"] == "user@example.com"
    assert user_dict["password"] == "password"
    assert user_dict["api_key"] == "123456789"
    assert user_dict["subscription"] == False
    assert user_dict["language_preference"] == "English"

from app.main.utils.prompt import Prompt

def test_constructor():
    prompt = Prompt("Turkish")
    assert prompt.languagePreference == "Turkish"

def test_defaultConstructor():
    prompt = Prompt()
    assert prompt.languagePreference == "English"

def test_setContent():
    prompt = Prompt()
    prompt.setContent("This is the content.")
    assert prompt.content == "This is the content."

def test_getSummarizeContentPrompt():
    prompt = Prompt()
    prompt.setContent("This is the content.")
    result = prompt.getSummarizeContentPromt()
    assert result["model"] == "gpt-3.5-turbo"
    assert result["messages"][0]["role"] == "system"
    assert result["messages"][0]["content"] == "You are a helpful assistant that summarizes the content in the language of the user's content in the shortest way without losing its meaning."
    assert result["messages"][1]["role"] == "user"
    assert result["messages"][1]["content"] == "This is the content."
    assert result["temperature"] == 0

def test_getExplainCodePrompt():
    prompt = Prompt()
    prompt.setContent("This is the code.")
    result = prompt.getExplainCodePromt()
    assert result["model"] == "gpt-3.5-turbo"
    assert result["messages"][0]["role"] == "system"
    assert result["messages"][0]["content"] == "You are a helpful assistant who briefly explains the code in English."
    assert result["messages"][1]["role"] == "user"
    assert result["messages"][1]["content"] == "This is the code."
    assert result["temperature"] == 0

def test_getFixTyposPrompt():
    prompt = Prompt()
    prompt.setContent("This is the content with typos.")
    result = prompt.getFixTyposPromt()
    assert result["model"] == "gpt-3.5-turbo"
    assert result["messages"][0]["role"] == "system"
    assert result["messages"][0]["content"] == "You are a helpful assistant that corrects typos."
    assert result["messages"][1]["role"] == "user"
    assert result["messages"][1]["content"] == "This is the content with typos."
    assert result["temperature"] == 0
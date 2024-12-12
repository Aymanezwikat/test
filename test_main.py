from main import greet
def test_greet(capsys):
    greet("alice")
    captured =capsys.readouterr()
    assert captured.out =="bonjour,Alice!\n"
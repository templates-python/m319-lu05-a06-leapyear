from main import main


def test_oddyear(capsys, monkeypatch):
    inputs = iter([2023])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    captured = capsys.readouterr()
    assert captured.out == 'The year is not a leap year.\n'

def test_four(capsys, monkeypatch):
    inputs = iter([2024])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    captured = capsys.readouterr()
    assert captured.out == 'The year is a leap year.\n'

def test_hundered(capsys, monkeypatch):
    inputs = iter([1900])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    captured = capsys.readouterr()
    assert captured.out == 'The year is not a leap year.\n'

def test_fourhundered(capsys, monkeypatch):
    inputs = iter([2000])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    captured = capsys.readouterr()
    assert captured.out == 'The year is a leap year.\n'

from src.l01_input_output.es01_student import main

def test_adulto(monkeypatch, capsys):
    inputs = iter(['Mario', '25'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Ciao Mario!" in captured.out
    assert "Sei adulto." in captured.out

def test_minorenne(monkeypatch, capsys):
    inputs = iter(['Luca', '15'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Ciao Luca!" in captured.out
    assert "Sei minorenne." in captured.out

def test_anziano(monkeypatch, capsys):
    inputs = iter(['Giuseppe', '70'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Ciao Giuseppe!" in captured.out
    assert "Sei anziano." in captured.out
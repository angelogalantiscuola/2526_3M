from src.l01_input_output.es02_student import main

def test_eta_calcolo(monkeypatch, capsys):
    inputs = iter(['Anna', '1990'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Ciao Anna! Quest'anno compi circa 35 anni." in captured.out

def test_eta_giovane(monkeypatch, capsys):
    inputs = iter(['Marco', '2000'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Ciao Marco! Quest'anno compi circa 25 anni." in captured.out
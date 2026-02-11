from src.l01_input_output.es03_student import main

def test_numero_10(monkeypatch, capsys):
    inputs = iter(['10'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Il numero precedente è 9 e il numero successivo è 11." in captured.out

def test_numero_0(monkeypatch, capsys):
    inputs = iter(['0'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Il numero precedente è -1 e il numero successivo è 1." in captured.out

def test_numero_negativo(monkeypatch, capsys):
    inputs = iter(['-5'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Il numero precedente è -6 e il numero successivo è -4." in captured.out
from projet.fonction import dire_bonjour
import builtins
import pytest

def test_dire_bonjour_prints_salut(monkeypatch):
    output = []

    def fake_print(*args, **kwargs):
        output.append(args[0])

    monkeypatch.setattr(builtins, "print", fake_print)
    
    dire_bonjour()
    
    assert "salut" in output

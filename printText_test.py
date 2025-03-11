import printText;
import io;

def test_hello(capsys):
    printText.main()
    captured = capsys.readouterr()
    expected_output = "Die Tasten klappern, Ideen sprühen,\nProbleme lösen, Fehler mühen.\nDoch am Ende, wenn es läuft,\nIst es das, was uns erfreut."
    expected_output = expected_output.replace('\r\n', '\n').strip()
    output = '\n'.join(line.strip() for line in captured.out.splitlines()).replace('\r\n', '\n').strip()

    assert  output == expected_output

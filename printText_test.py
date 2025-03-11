import hello;

def test_hello():
    expected_output = "Die Tasten klappern, Ideen sprühen,\nProbleme lösen, Fehler mühen.\nDoch am Ende, wenn es läuft,\nIst es das, was uns erfreut."
    actual_output = hello.hello_world()
    
    # Normalize line endings and remove trailing spaces at line endings
    normalized_actual = actual_output.replace('\r\n', '\n').strip()
    # Großbuchstaben zu Kleinbuchstaben umwandeln


    normalized_expected = expected_output.replace('\r\n', '\n').strip()
    
    assert normalized_actual == normalized_expected

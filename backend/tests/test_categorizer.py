from app.services.categorizer import detect_case_type

def test_theft():
    assert detect_case_type("The accused was charged with theft of gold")[0] == "Criminal Law"

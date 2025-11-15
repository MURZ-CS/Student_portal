import pytest
from marks import add_marks,marks,validate_mark_input

def test_add_marks_boundaries():
    marks.clear()

    assert add_marks("S1","Math","midterm",-1)=="Below minimum (invalid)"

    assert add_marks("S1","Maths","midterm",0)=="Success"

    assert add_marks("S1","Maths","final",1)=="Success"

    assert add_marks("S1","Math","final",50)=="Success"

    assert add_marks("S1","Math","final",100)=="Success"

    assert add_marks("S1","Math","midterm",101)=="Above Maximum (invalid)"

    #now checking if they are actually stored#
def test_if_element_added():
    add_marks("S1","Math","final")
    assert marks["S1"]["Math"]["final"]==100

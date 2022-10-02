from Lab1.exception.TAPException import TAPException
from Lab1.exception.TapCourse import TapCourse

class TAPMain:
    try:
        print(TapCourse.passCourse(False))
    except TAPException as e:
        print(e)

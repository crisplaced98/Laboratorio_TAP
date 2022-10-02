from Lab1.exception.TAPException import TAPException
class TapCourse:
    def passCourse(hasStudied):
        if (hasStudied):
            return "You pass the course"
        else:
            raise TAPException("You failed, better study next time")
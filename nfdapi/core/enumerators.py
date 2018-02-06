from enum import Enum


class Gender(Enum):
    FEMALE = "female"
    FEMALE_PARTHENOGENIC = "female (parthenogenic)"
    GYNANDROMORPHIC = "gynandromorphic"
    HERMAPHRODITIC = "hermaphroditic"
    HERMAPHRODITIC_PARTHENOGENIC = "hermaphroditic (parthenogenic)"
    MALE = "male"
    N_A = "n/a"
    UNKNOWN = "unknown"


# This can be calculated from the solar time
class Daytime(Enum):
    DAWN = "Dawn"
    EARLY_MORNING = "Early morning"
    MORNING = "Morning"
    LATE_MORNING = "Late morning"
    NOON = "Noon"
    EARLY_AFTERNOON = "Early afternoon"
    AFTERNOON = "Afternoon"
    LATE_AFTERNOON = "Late afternoon"
    DUSK = "Dusk"
    EARLY_EVENING = "Early"
    EVENING = "Evening"
    LATE_EVENING = "Late evening"
    LATE_NIGHT = "Late night/after midnight"
    UNKNOWN = "Unknown"


# This can be calculated from the date time
class Season(Enum):
    EARLY_SPRING = "Early spring"
    MID_SPRING = "Mid spring"
    LATE_SPRING = "Late spring"
    EARLY_SUMMER = "Early summer"
    MID_SUMMER = "Mid summer"
    LATE_SUMMER = "Late summer"
    EARLY_FALL = "Early fall"
    MID_FALL = "Mid fall"
    LATE_FALL = "Late fall"
    EARLY_WINTER = "Early winter"
    MID_WINTER = "Mid winter"
    LATE_WINTER = "Late winter"


class RecordOrigin(Enum):
    BIOBLITZ = "bioblitz"
    CAMERA_TRAP = "camera trap"
    CHECKING_CASUAL = "checking casual observer report"
    CHECKING_HISTORICAL = "checking historical record"
    INCIDENTAL = "incidental"
    MONITORING_CENSUS = "monitoring, census"
    MONITORING_INITIAL = "monitoring, initial"
    MONITORING_LONG_TERM = "monitoring, long term"
    MONITORING_PROPERTY = "monitoring, property assessment"
    SEARCHING = "searching"


class RecordingStation(Enum):
    pass


class Reservation(Enum):
    ACACIA = "Acacia"
    BEDFORD = "Bedford"


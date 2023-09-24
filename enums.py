from enum import Enum


class STATUS(Enum):
    NONE = 0,
    FROZEN = 1,
    ASLEEP = 2,
    PARALYZED = 3,
    BURNED = 4,
    POISONED = 5


class BALL_TYPES(Enum):
    POKEBALL = 6,
    GREATBALL = 7,
    ULTRABALL = 8,
    SAFARIBALL = 9,
    MASTERBALL = 10


class GENDERS(Enum):
    MALE = 11,
    FEMALE = 12,
    UNKNOWN = 13

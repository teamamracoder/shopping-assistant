from enum import Enum

class Gender(Enum):
    MALE = 1
    FEMALE = 2
    OTHER = 3

class Role(Enum):
    END_USER = 1
    SELLER = 2
    SERVICE_PROVIDER = 3
    ADMIN = 4

class RELATIONSHIP_TYPE(Enum):
    SELLER = 1
    SERVICE_PROVIDER = 2


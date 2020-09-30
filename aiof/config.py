import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    DefaultRoundingDigit: int = os.getenv("DefaultRoundingDigit", 2)
    DefaultFrequency: int = os.getenv("DefaultFrequency", 12)
    DefaultInterest: float = os.getenv("DefaultInterest", 7)
    DefaultHysInterest: float = os.getenv("DefaultHysInterest", 1.75)
    DefaultInvestmentFee: float = os.getenv("DefaultFee", 0.50)
    DefaultTaxDrag: float = os.getenv("DefaultTaxDrag", 0.50)
    DefaultChild: int = os.getenv("DefaultChild", 2)

    DefaultInterests: list = [ 
        2,
        4,
        6,
        8
    ]
    DefaultFrequencies: list = [
        365,
        12,
        1        
    ]
    DefaultFees: list = [
        0.10,
        0.50,
        1.00,
        1.50,
        2.00,
        2.50,
        3.00,
    ]
    DefaultChildren: list = [
        1,
        2,
        3,
        4
    ]

    # FI specific
    DefaultTenMillion: list = [
        1000000,
        2000000,
        3000000,
        4000000,
        5000000,
        6000000,
        7000000,
        8000000,
        9000000,
        10000000,
        100000000,
    ]
    DefaultTenMillionInterests: list = [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10
    ]
    # End FI specific

    cors_origins: list = [
        "http://localhost:4100",
        "http://localhost:1337"
    ]
    cors_allowed_methods: list = [
        "*"
    ]
    cors_allowed_headers: list = [
        "*"
    ]

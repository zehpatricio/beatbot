from dataclasses import dataclass


@dataclass
class User:
    id: str
    display_name: str
    country: str
    email: str
    href: str
    uri: str

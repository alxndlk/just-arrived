from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional


class Currency(BaseModel):
    name: str
    code: str
    symbol: str


class Terminal(BaseModel):
    name: str
    description: str


class WifiInfo(BaseModel):
    available: bool
    network_name: Optional[str]
    note: Optional[str]


class Airport(BaseModel):
    airport_name: str
    iata_code: str
    icao_code: str
    distance_km: float
    gmt: str
    country: str
    timezone: str
    terminals: List[Terminal]
    website: HttpUrl
    wifi: WifiInfo


class Hospital(BaseModel):
    name: str
    website: HttpUrl
    lat: float
    lon: float
    hours: List[str]


class Hospitals(BaseModel):
    emergency: str
    hospitals: List[Hospital]


class EmergencyNumbers(BaseModel):
    ambulance: str
    fire: str
    police: str


class AvgPriceData(BaseModel):
    city: str
    currency: str
    avg_price_index: float
    prices: dict


class Meta(BaseModel):
    generated_at: str
    env: str
    source: str


class CityData(BaseModel):
    json_language: str
    country_code: str
    country_name: str
    city_name: str
    language: Optional[List[str]]
    lat: float
    lon: float
    timezone: str
    currency: List[Currency]
    population: Optional[int]
    welcome_message_title: str
    welcome_message_text: str
    welcome_message_image: HttpUrl
    airports: List[Airport]
    hospitals: Hospitals
    emergency_numbers: EmergencyNumbers
    avg_prices: AvgPriceData
    _meta: Meta

class DevCityData(BaseModel):
    json_language: str
    country_code: str
    country_name: str
    city_name: str
    language: Optional[List[str]] = None
    lat: float
    lon: float
    timezone: Optional[str] = None
    currency: Optional[List[Currency]] = None
    population: Optional[int] = None
    welcome_message_title: Optional[str] = None
    welcome_message_text: Optional[str] = None
    welcome_message_image: Optional[HttpUrl] = None
    airports: Optional[List[Airport]] = None
    hospitals: Optional[Hospitals] = None
    emergency_numbers: Optional[EmergencyNumbers] = None
    avg_prices: Optional[AvgPriceData] = None
    _meta: Optional[Meta] = None

from datetime import datetime

from sqlmodel import Field, SQLModel

# Tri,Perimètre juridique,Perimètre spatial,Spatial perimeter,Filière,Sector,Centrale,Tranche,Combustible,Fuel,Sous-filière,Sub-sector,Contrat programme,Date de mise en service industrielle,Puissance installée ,Puissance minimum de conception,Unité,Point gps (wsg84),Région,Code Insee région,Département,Code Insee département,EPCI,Code Insee EPCI,Commune,Code Insee commune

# 1,EDF SA,"France métropolitaine, sans la Corse ni les iles du ponant","Metropolitan France, excluding Corsica and the Ponant Islands",Nucléaire,Nuclear,BELLEVILLE,BELLEVILLE 1,Uranium Enrichi,Enriched Uranium,Réacteur à eau pressurisée (REP) 1300,Pressurised water reactor 1300,P'4,1988-06-01,1310,260,MW,"47.508946, 2.875676",CENTRE-VAL DE LOIRE,24,CHER,18,CC Pays Fort Sancerrois Val de Loire,200069227,Belleville-sur-Loire,18026

# Plant: Sector ; Date de mise en service ; Puissance installée ; Code Insee commune ; Point gps (wsg84) ; Commune ; Département ; Région ; Sub-sector; Central


class Plant(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    sector: str
    sub_sector: str
    commissioning_date: datetime
    power: float
    gps: str
    city: str
    departement: int
    region: str

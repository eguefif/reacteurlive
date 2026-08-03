export interface Plant {
  name: string
  sector: string
  subSector: string
  gps: string
  city: string
  departement: number
  region: string
  reactors: Reactor[]
}

export interface Reactor {
  id: number
  name: string
  sector: string
  subSector: string
  gps: string
  city: string
  departement: number
  region: string
  reactors: Reactor[]
  commissioningDate: string
  powerMW: number
}

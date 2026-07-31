# ReacteurLive

ReacteurLive is a small learning project for Fast/Api. It get some data from EDF to display status of nuclecar PowerPlant.

## Commands

```bash
$ just backend
$ just frontend
```

### Ingesting data from csv files manually

```bash
$ cd backend
$ uvr ingest.py
```

## TODO

### Backend
- [ ] Create a Plant table with information and coordinate: use both the Plant dataset + and City dataset + PlantState.
- [ ] Refactor plant state to only have a association with Plant
- [ ] Ingest CSV into a sqlite database

### Frontend

- [ ] Several reactor are in the same spot. We need to gather by location
- [ ] Display plant information in a Vue component instead of popup: find picture
- [ ] Display global information: power max

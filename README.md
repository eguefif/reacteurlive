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
- [ ] Add status information to plant using the CSV that contains stopped plant.
- [ ] Add a pictures

### Frontend

- [ ] Display plant information in a Vue component instead of popup: find picture
    - [ ] Add picture
- [ ] Display global information: power max

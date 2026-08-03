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
- [ ] Improve reactor table to add state information
    - [ ] status
    - [ ] start date
    - [ ] end_date
    - [ ] stop_reason
    - [ ] type_reason
    - [ ] Information
    - [ ] Power available
- [ ] Ingestion should only update reactor using Tranche

- [ ] Add status information to plant using the CSV that contains stopped plant.
- [ ] Add a pictures

### Frontend

- [ ] Display plant information in a Vue component instead of popup: find picture
    - [ ] Add picture
- [ ] Display global information: power max
- [ ] Move plant card on the opposite side
- [ ] Find a way to camel case Axios return
- [ ] Improve plant card


## DB Architecture

Reactors are grouped by plant.


We have two datasets from EDF open data:
* A list of reactors
* A list of power plant states

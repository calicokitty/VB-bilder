# VB-bilder

Required libraries: 

```bash
pip install -r requirements.txt
```

Henter omslagsbilde for fullkatalogiserte poster fra VB og datterforlag, som mangler omslagsbilde i Ája (sjekkes via SRU).

Destinasjon for filene kan konfigureres gjennom miljøvariabelen `AJA_DESTINATION_PATH`.
Denne kan for eksempel defineres gjennom å opprette en `.env`-fil i samme mappe med innhold:

    AJA_DESTINATION_PATH=/sti/til/lagringssted/

# VA Facility Finder

A browser-based tool that queries the VA Facilities API to find VA health, benefits, cemetery, and vet center locations by state.

## What it does
- Select a state and facility type
- Hits the VA Lighthouse Facilities API in real time
- Displays facility name, address, phone, and available services

## How to run

1. Get a free VA API sandbox key at https://developer.va.gov/apply
2. Open `config.js` and replace `YOUR_API_KEY_HERE` with your key
3. Open `index.html` in a browser

## Files
- `index.html` — front-end search UI
- `config.js` — API key configuration (do not commit your real key to GitHub)

## API Used
- [VA Facilities API](https://developer.va.gov/explore/api/va-facilities) — free, sandbox access available

## Tech
- HTML / CSS / JavaScript
- VA Lighthouse API (REST/JSON)

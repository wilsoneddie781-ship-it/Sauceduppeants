from fastapi_poe import PoeApp, ProtocolRequest, PartialResponse from square.client import Client
app = PoeApp()
⁠@app.router.post("/query")⁠
async def get_response(request: ProtocolRequest):⁠
        result = client.locations.list_locations()
    if result.is_success():
        locations = result.body.get("locations", [])
        location_name = locations[0]["name"] if locations else "No locations found"
    else:
        location_name = "Could not connect to Square"

    yield PartialResponse(text=f"Hello! Your Square location is: {location_name}")

# CrossCompute Examples

Here are example automations and tools made using the CrossCompute framework.

```
pip install -U crosscompute

cd ~/Documents
git clone https://github.com/crosscompute/crosscompute-examples
```

## Count Words

## Find Primes

## Add Numbers

This example illustrates a result automation.

```
cd ~/Documents/crosscompute-examples/add-numbers
crosscompute tools add . --mock

export CROSSCOMPUTE_TOKEN=YOUR-TOKEN
crosscompute automations run
```

## Add Columns

## Count Assets

## Compare Datestamps

This example generates markdown as one of its output variables, where the text of the markdown varies depending on the result.

## Convert Timestamps

## Flip WKT

## Transform Coordinates

## Map Addresses

Convert an address table into a map.

- Input Variable Views: table
- Output Variable Views: map, table
- Script Command: bash
- Operating System: linux
- Environment Variables
- Python Dependencies
- Geospatial Environment Image

## Measure Geometries

Compute geometric statistics.

- Input Variable Views: map
- Output Variable Views: number
- Script Command: jupyter
- Operating System: linux
- Python Dependencies
- Geospatial Environment Image

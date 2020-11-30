# CrossCompute Examples

Here are example automations and tools made using the CrossCompute framework.

```
pip install -U crosscompute

cd ~/Documents
git clone https://github.com/crosscompute/crosscompute-examples
```

## Add Numbers

This example illustrates a result automation.

```
cd ~/Documents/crosscompute-examples/add-numbers
crosscompute tools add . --mock

export CROSSCOMPUTE_TOKEN=YOUR-TOKEN
crosscompute automations run
```

## Compare Datestamps

This example generates markdown as one of its output variables, where the text of the markdown varies depending on the result.

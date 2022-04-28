---
# version of crosscompute
crosscompute: 0.9.2

# name of your automation
name: Make QR Code

# version of your automation
version: 0.0.1

# input configuration
input:

  # input variables
  # - id to use when referencing your variable in the template
  # - view to use when rendering your variable on the display
  # - path where your script loads the variable,
  #   relative to the input folder
  variables:
    - id: a
      view: number
      path: variables.dictionary
    - id: b
      view: number
      path: variables.dictionary

# output configuration
output:

  # output variables
  # - id to use when referencing your variable in the template
  # - view to use when rendering your variable on the display
  # - path where your script saves the variable,
  #   relative to the output folder
  variables:
    - id: c
      view: number
      path: variables.dictionary

# tests configuration
# - folder that contains an input subfolder with paths for
#   input variables that define a specific test
tests:
  - folder: tests/integers
  - folder: tests/floats

# batches configuration
# - name of the batch; can include variable ids for batch template
# - folder that contains an input subfolder with paths for
#   input variables that define a specific batch
# - configuration for batch template
#   - path containing different values for the input variables
batches:
  - name: '{a} + {b}'
    folder: batches/{a}-{b}
    configuration:
      path: datasets/batches.csv

# scripts configuration
# - command to use to run your script
scripts:
  - command: python run.py {input_folder} {output_folder}

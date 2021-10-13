# A toggle switch widget for Streamlit

![Toggle Switch](screenshot.png?raw=true "Streamlit Toggle Switch")

## Installation

To build the library Node.js has to be installed. If you are using Anaconda/Miniconda you
can install it with the following command:
```bash
conda install -c conda-forge nodejs=16
```
The `npm` executable has to be in your `PATH`.

You can finally build and install streamlit-toggle automatically by pip with the command:
```bash
pip install .
```
For this you have to be in the root directory of this repository.

## Usage

```python
import streamlit as st
from streamlit_toggle import st_toggleswitch

awesomeness_enabled = st_toggleswitch("Enable awesomeness")
if awesomeness_enabled:
    st.write("Awesomeness has been enabled!")
```

## Copyright notice

This is a fork of the project [samdobson/streamlit-toggle](https://github.com/samdobson/streamlit-toggle) 
by [Sam Dobson](https://github.com/samdobson).

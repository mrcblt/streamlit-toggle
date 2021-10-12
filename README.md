# A toggle switch widget for Streamlit

![Toggle Switch](screenshot.png?raw=true "Streamlit Toggle Switch")

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
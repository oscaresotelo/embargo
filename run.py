## Add all required imports here ##
## Eg. 
# import cv2
# import streamlit as st
# import pandas
##
import streamlit as st
import sqlite3
from sqlite3 import Error
from st_pages import Page, show_pages, add_page_title
import re
from freeGPT import gpt3
import subprocess

if __name__ == '__main__':
    subprocess.run("streamlit run carga.py")
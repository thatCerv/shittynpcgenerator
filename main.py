import streamlit as st
import random
import json

with open('table.json') as file:
    tables = json.load(file)

def generate():
    gender = random.choice(['Male', 'Female'])
    surnameType = random.choice(['Surname', 'Title', 'None'])
    surname = random.choice(tables[surnameType]) if surnameType != 'None' else None
    return f'{random.choice(tables["Firstname"][gender])} {surname + " " if surnameType != "None" else ""} is a {random.randint(16, 99)} year old {random.choice(tables["Career"])} from {random.choice(tables["Place"])}.\n {"His" if gender == "Male" else "Her"} Father {random.choice(tables["Firstname"]["Male"])} {surname if surnameType == "Surname" else "" if surnameType == "None" else random.choice(tables["Title"])} is a {random.choice(tables["Career"])}, and {"his" if gender == "Male" else "her"} mother {random.choice(tables["Firstname"]["Female"])} {random.choice(tables[random.choice(["Surname", "Title"])]) if random.randint(0, 2) else ""} is a {random.choice(tables["Career"])}.'

if st.button('Generate'):
    st.write(generate())

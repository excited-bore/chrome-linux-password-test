Google Chrome on linux password check
===========

Small claude generated python script to check whether passwords in google chrome based browsers are properly encrypted or not  
If not, it will paste every entry in the password manager inside the shell  

## How to use

Install google chrome and add an entry to the password manager  

Clone repository, install python if not installed already.  
Then, change directory into project and create and activate a virtual environment with:  

```
python3 -m venv .venv
source venv/bin/activate
```

Then, install dependency with  
```
pip install pycryptodome
```
or  
```
pip install -r requirements.txt
```

Then run it with:  
```
python test.py
```
If password entry shows up: 😬  

import json
import logging

from iotfunctions.db import Database
from iotfunctions.enginelog import EngineLogging

EngineLogging.configure_console_logging(logging.DEBUG)

'''
You can test functions locally before registering them on the server to
understand how they work.

Supply credentials by pasting them from the usage section into the UI.
Place your credentials in a separate file that you don't check into the repo.

'''

with open('credentials_as_dev.json', encoding='utf-8') as F:
    credentials = json.loads(F.read())
db_schema = None
db = Database(credentials=credentials)

'''
Import and instantiate the functions to be tested

The local test will generate data instead of using server data.
By default it will assume that the input data items are numeric.

Required data items will be inferred from the function inputs.

The function below executes an expression involving a column called x1
The local test function will generate data dataframe containing the column x1

By default test results are written to a file named df_test_entity_for_<function_name>
This file will be written to the working directory.

'''
from AIModelDesign import AIDesignModel
'''from custom.functions import AIDesignModel'''

fn = AIDesignModel(BPT1=30,BPT2=40,BPT3=50,BPT4=60,BPT5=55,BPT6=66,BPT7=77,BPT8=88, Powerup_Steam_Flow_Rate=10,
Ratio_outlet_inlet_temp=20,Steam_Supply_Pressure=42.9,Turbine_Inlet_Temperature=30,Turbine_Outlet_Temperature=40,Vibration=50,prediction=0)

fn.execute_local_test(db=db, db_schema=db_schema)

'''
Register function so that you can see it in the UI
'''

db.register_functions([AIDesignModel])
'''db.unregister_functions([AIModelDesign])'''

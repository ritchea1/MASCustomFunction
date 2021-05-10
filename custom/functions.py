import logging

from iotfunctions import ui
from iotfunctions.base import BaseTransformer

logger = logging.getLogger(__name__)

# Specify the URL to your package here.
# This URL must be accessible via pip install

PACKAGE_URL = 'https://github.com/ritchea1/MASCustomFunction.git'


class AIPredictionModel(BaseTransformer):
    '''
    The docstring of the function will show as the function description in the UI.
    '''

    def __init__(self,BPT1,BPT2,BPT3,BPT4,BPT5,BPT6,BPT7,BPT8, Powerup_Steam_Flow_Rate,
    Ratio_outlet_inlet_temp,Turbine_Inlet_Temperature,Turbine_Outlet_Temperature,Vibration,prediction):
        # a function is expected to have at least one parameter that acts
        # as an input argument, e.g. "name" is an argument that represents the
        # name to be used in the greeting. It is an "input" as it is something
        # that the function needs to execute.

        # a function is expected to have at lease one parameter that describes
        # the output data items produced by the function, e.g. "greeting_col"
        # is the argument that asks what data item name should be used to
        # deliver the functions outputs

        # always create an instance variable with the same name as your arguments

        self.BPT1 = BPT1
        self.BPT2 = BPT2
        self.BPT3 = BPT3
        self.BPT4 = BPT4
        self.BPT5 = BPT5
        self.BPT6 = BPT6
        self.BPT7 = BPT7
        self.BPT8 = BPT8
        self.Powerup_Steam_Flow_Rate = Powerup_Steam_Flow_Rate
        self.Ratio_outlet_inlet_temp = Ratio_outlet_inlet_temp
        self.Turbine_Inlet_Temperature = Turbine_Inlet_Temperature
        self.Turbine_Outlet_Temperature = Turbine_Outlet_Temperature
        self.Vibration = Vibration
        self.prediction = prediction
        super().__init__()

        # do not place any business logic in the __init__ method
        # All business logic goes into the execute() method or methods called by the
        # execute() method

    def execute(self, df):
        # the execute() method accepts a dataframe as input and returns a dataframe as output
        # the output dataframe is expected to produce at least one new output column
        '''df = df.copy()'''
        header = {'Content-Type': 'application/json', 'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwicm9sZSI6IkFkbWluIiwicGVybWlzc2lvbnMiOlsiYWRtaW5pc3RyYXRvciIsImNhbl9wcm92aXNpb24iLCJtYW5hZ2VfY2F0YWxvZyIsImF1dGhvcl9nb3Zlcm5hbmNlX2FydGlmYWN0cyIsIm1hbmFnZV9nb3Zlcm5hbmNlX3dvcmtmbG93Iiwidmlld19nb3Zlcm5hbmNlX2FydGlmYWN0cyIsIm1hbmFnZV9jYXRlZ29yaWVzIiwibWFuYWdlX3F1YWxpdHkiLCJtYW5hZ2VfaW5mb3JtYXRpb25fYXNzZXRzIiwibWFuYWdlX2Rpc2NvdmVyeSIsIm1hbmFnZV9tZXRhZGF0YV9pbXBvcnQiLCJhY2Nlc3NfY2F0YWxvZyIsInZpZXdfcXVhbGl0eSIsImFjY2Vzc19pbmZvcm1hdGlvbl9hc3NldHMiXSwiZ3JvdXBzIjpbMTAwMDBdLCJzdWIiOiJhZG1pbiIsImlzcyI6IktOT1hTU08iLCJhdWQiOiJEU1giLCJ1aWQiOiIxMDAwMzMwOTk5IiwiYXV0aGVudGljYXRvciI6ImRlZmF1bHQiLCJpYXQiOjE2MjA2MjIwMTQsImV4cCI6MTYyMDY2NTE3OH0.lebJTpD-rGTNAbgpai8fT559wH9_DwmvUJ6aDUCMZEJbyx0IkGiMSKqr2sWPyK5PsuEOszcMZgu-lv6F13a5z2cfQRk33X2AJoDJRJtwltOikbCjHwgmeXnSlHfaZI2XMQYLF7PDjxis1mG6-KSExcvVwW-hnwPQn3a29oErnXcUKBCMPC8pQqQ7MatVCqWjH45lHSF1P-We40OGs5_znlTTBWEcg-PDqLxWaV7CivyYu83gOREsUc0nXnkGc31RaxTXkI437wWZIk-z7ykoH5iyivvuLca-kkDuedL-C-FNDrHAV_Hz4PXWqSl0y2Nz-UhiojqfoQt3gwhVjRYaIQ'}
        # NOTE: manually define and pass the array(s) of values to be scored in the next line
        val="["+df[BPT1]+","+df[BPT2]+","+df[BPT3]+","+df[BPT4]+","+df[BPT5]+","+df[BPT6]+","+df[BPT7]+","+df[BPT8]+","+df[Powerup_Steam_Flow_Rate]+","+df[Ratio_outlet_inlet_temp]+","+df[Turbine_Inlet_Temperature]+","+df[Turbine_Outlet_Temperature]+","+df[Vibration]+"]"
        vector="{\"input_data\":[{\"fields\":[\"BPT1\",\"BPT2\",\"BPT3\",\"BPT4\",\"BPT5\",\"BPT6\",\"BPT7\",\"BPT8\",\"Powerup Steam Flow Rate\",\"Ratio of outlet inlet temp\",\"Steam Supply Pressure\",\"Turbine Inlet Temperature\",\"Turbine Outlet Temperature\",\"Vibration\"],\"values\":["+val+"]}]}"
        payload_scoring=json.loads(vector)
        response_scoring = requests.post('https://mas-maslab2-cp4d-cpd-mas-maslab2-cp4d.maslab-wdc07-b3c-16x64-18312db33a3427c911e9adf447e95207-0000.us-east.containers.appdomain.cloud/ml/v4/deployments/bbd9238a-3cff-459e-9aed-3b14c3b9449f/predictions?version=2021-05-03', json=payload_scoring, headers=header)
        print("Scoring response")
        print(json.loads(response_scoring.text))
        response_data=json.loads(response_scoring.text)
        for i in response_data['predictions']:
            print(i)
            fieldsData=i
            for j in fieldsData['values']:
                df[self.prediction] = j[0]

        print("-----prediction----"+df[self.prediction])
        # If the function has no new output data, output a status_flag instead
        # e.g. df[<self.output_col_arg>> = True

        return df

    @classmethod
    def build_ui(cls):
        # Your function will UI built automatically for configuring it
        # This method describes the contents of the dialog that will be built
        # Account for each argument - specifying it as a ui object in the "inputs" or "outputs" list

        inputs=[]
        '''inputs.append(ui.UISingle(name='BPT1', datatype=float, description='BPT1'))'''
        inputs.append(ui.UIMultiItem(name='BPT1', datatype=float, description='BPT1'))
        inputs.append(ui.UIMultiItem(name='BPT2', datatype=float, description='BPT2'))
        inputs.append(ui.UIMultiItem(name='BPT3', datatype=float, description='BPT3'))
        inputs.append(ui.UIMultiItem(name='BPT4', datatype=float, description='BPT4'))
        inputs.append(ui.UIMultiItem(name='BPT5', datatype=float, description='BPT5'))
        inputs.append(ui.UIMultiItem(name='BPT6', datatype=float, description='BPT6'))
        inputs.append(ui.UIMultiItem(name='BPT7', datatype=float, description='BPT7'))
        inputs.append(ui.UIMultiItem(name='BPT8', datatype=float, description='BPT8'))
        inputs.append(ui.UIMultiItem(name='Powerup_Steam_Flow_Rate', datatype=float, description='Powerup Steam Flow Rate'))
        inputs.append(ui.UIMultiItem(name='Ratio_outlet_inlet_temp', datatype=float, description='Ratio of outlet inlet temp'))
        inputs.append(ui.UIMultiItem(name='Turbine_Inlet_Temperature', datatype=float, description='Turbine Inlet Temperature'))
        inputs.append(ui.UIMultiItem(name='Turbine_Outlet_Temperature', datatype=float, description='Turbine Outlet Temperature'))
        inputs.append(ui.UIMultiItem(name='Vibration', datatype=float, description='Vibration'))
        outputs = [
            ui.UIFunctionOutSingle(name='prediction', datatype=float, description='Output item produced by function')]
        return inputs, outputs

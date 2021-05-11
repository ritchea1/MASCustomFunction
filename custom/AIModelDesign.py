import logging
import urllib3, requests, json

from iotfunctions import ui
from iotfunctions.base import BaseTransformer

logger = logging.getLogger(__name__)

# Specify the URL to your package here.
# This URL must be accessible via pip install

PACKAGE_URL = 'https://github.com/ritchea1/MASCustomFunction.git'


class AIDesignModel(BaseTransformer):
    '''
    The docstring of the function will show as the function description in the UI.
    '''

    def __init__(self,BPT1,BPT2,BPT3,BPT4,BPT5,BPT6,BPT7,BPT8, Powerup_Steam_Flow_Rate,
    Ratio_outlet_inlet_temp,Steam_Supply_Pressure,Turbine_Inlet_Temperature,Turbine_Outlet_Temperature,Vibration,prediction):
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
        self.Steam_Supply_Pressure=Steam_Supply_Pressure
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
        cpdheader = {'Content-Type': 'application/json'}
        payload_scoringcpd=json.loads("{\"username\": \"admin\",\"password\":\"password\"}")
        response_scoringcpd = requests.post('https://mas-maslab2-cp4d-cpd-mas-maslab2-cp4d.maslab-wdc07-b3c-16x64-18312db33a3427c911e9adf447e95207-0000.us-east.containers.appdomain.cloud/icp4d-api/v1/authorize', json=payload_scoringcpd, headers=cpdheader)
        response_datacpd=json.loads(response_scoringcpd.text)
        mltoken='Bearer '+ str(response_datacpd["token"])

        header = {'Content-Type': 'application/json', 'Authorization': mltoken}
        # NOTE: manually define and pass the array(s) of values to be scored in the next line
        val="["+str(self.BPT1)+","+str(self.BPT2)+","+str(self.BPT3)+","+str(self.BPT4)+","+str(self.BPT5)+","+str(self.BPT6)+","+str(self.BPT7)+","+str(self.BPT8)+","+str(self.Powerup_Steam_Flow_Rate)+","+str(self.Ratio_outlet_inlet_temp)+","+str(self.Steam_Supply_Pressure)+","+str(self.Turbine_Inlet_Temperature)+","+str(self.Turbine_Outlet_Temperature)+","+str(self.Vibration)+"]"
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
                self.prediction= j[0]

        print("-----prediction----"+str(self.prediction))

        # If the function has no new output data, output a status_flag instead
        # e.g. df[<self.output_col_arg>> = True

        return df

    @classmethod
    def build_ui(cls):
        # Your function will UI built automatically for configuring it
        # This method describes the contents of the dialog that will be built
        # Account for each argument - specifying it as a ui object in the "inputs" or "outputs" list
        inputs=[]
        inputs.append(ui.UISingleItem(name='BPT1', datatype=float, description='BPT1'))
        inputs.append(ui.UISingleItem(name='BPT2', datatype=float, description='BPT2'))
        inputs.append(ui.UISingleItem(name='BPT3', datatype=float, description='BPT3'))
        inputs.append(ui.UISingleItem(name='BPT4', datatype=float, description='BPT4'))
        inputs.append(ui.UISingleItem(name='BPT5', datatype=float, description='BPT5'))
        inputs.append(ui.UISingleItem(name='BPT6', datatype=float, description='BPT6'))
        inputs.append(ui.UISingleItem(name='BPT7', datatype=float, description='BPT7'))
        inputs.append(ui.UISingleItem(name='BPT8', datatype=float, description='BPT8'))
        inputs.append(ui.UISingleItem(name='Powerup_Steam_Flow_Rate', datatype=float, description='Powerup Steam Flow Rate'))
        inputs.append(ui.UISingleItem(name='Ratio_outlet_inlet_temp', datatype=float, description='Ratio of outlet inlet temp'))
        inputs.append(ui.UISingleItem(name='Turbine_Inlet_Temperature', datatype=float, description='Turbine Inlet Temperature'))
        inputs.append(ui.UISingleItem(name='Turbine_Outlet_Temperature', datatype=float, description='Turbine Outlet Temperature'))
        inputs.append(ui.UISingleItem(name='Vibration', datatype=float, description='Vibration'))
        outputs = [
            ui.UIFunctionOutSingle(name='prediction', datatype=float, description='Output item produced by function')]
        return inputs, outputs

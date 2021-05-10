import logging

from iotfunctions import ui
from iotfunctions.base import BaseTransformer

logger = logging.getLogger(__name__)

# Specify the URL to your package here.
# This URL must be accessible via pip install

PACKAGE_URL = 'https://github.com/ritchea1/MASCustomFunction.git'


class AIModelDesign(BaseTransformer):
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

        df[self.prediction] = self.BPT1

        # If the function has no new output data, output a status_flag instead
        # e.g. df[<self.output_col_arg>> = True

        return df

    @classmethod
    def build_ui(cls):
        # Your function will UI built automatically for configuring it
        # This method describes the contents of the dialog that will be built
        # Account for each argument - specifying it as a ui object in the "inputs" or "outputs" list
        inputs=[]
        inputs.append(ui.UISingle(name='BPT1', datatype=float, description='BPT1'))
        inputs.append(ui.UISingle(name='BPT2', datatype=float, description='BPT2'))
        inputs.append(ui.UISingle(name='BPT3', datatype=float, description='BPT3'))
        inputs.append(ui.UISingle(name='BPT4', datatype=float, description='BPT4'))
        inputs.append(ui.UISingle(name='BPT5', datatype=float, description='BPT5'))
        inputs.append(ui.UISingle(name='BPT6', datatype=float, description='BPT6'))
        inputs.append(ui.UISingle(name='BPT7', datatype=float, description='BPT7'))
        inputs.append(ui.UISingle(name='BPT8', datatype=float, description='BPT8'))
        inputs.append(ui.UISingle(name='Powerup_Steam_Flow_Rate', datatype=float, description='Powerup Steam Flow Rate'))
        inputs.append(ui.UISingle(name='Ratio_outlet_inlet_temp', datatype=float, description='Ratio of outlet inlet temp'))
        inputs.append(ui.UISingle(name='Turbine_Inlet_Temperature', datatype=float, description='Turbine Inlet Temperature'))
        inputs.append(ui.UISingle(name='Turbine_Outlet_Temperature', datatype=float, description='Turbine Outlet Temperature'))
        inputs.append(ui.UISingle(name='Vibration', datatype=float, description='Vibration'))
        outputs = [
            ui.UIFunctionOutSingle(name='prediction', datatype=float, description='Output item produced by function')]
        return inputs, outputs

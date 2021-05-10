import urllib3, requests, json
# NOTE: you must construct mltoken based on provided documentation
header = {'Content-Type': 'application/json', 'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwicm9sZSI6IkFkbWluIiwicGVybWlzc2lvbnMiOlsiYWRtaW5pc3RyYXRvciIsImNhbl9wcm92aXNpb24iLCJtYW5hZ2VfY2F0YWxvZyIsImF1dGhvcl9nb3Zlcm5hbmNlX2FydGlmYWN0cyIsIm1hbmFnZV9nb3Zlcm5hbmNlX3dvcmtmbG93Iiwidmlld19nb3Zlcm5hbmNlX2FydGlmYWN0cyIsIm1hbmFnZV9jYXRlZ29yaWVzIiwibWFuYWdlX3F1YWxpdHkiLCJtYW5hZ2VfaW5mb3JtYXRpb25fYXNzZXRzIiwibWFuYWdlX2Rpc2NvdmVyeSIsIm1hbmFnZV9tZXRhZGF0YV9pbXBvcnQiLCJhY2Nlc3NfY2F0YWxvZyIsInZpZXdfcXVhbGl0eSIsImFjY2Vzc19pbmZvcm1hdGlvbl9hc3NldHMiXSwiZ3JvdXBzIjpbMTAwMDBdLCJzdWIiOiJhZG1pbiIsImlzcyI6IktOT1hTU08iLCJhdWQiOiJEU1giLCJ1aWQiOiIxMDAwMzMwOTk5IiwiYXV0aGVudGljYXRvciI6ImRlZmF1bHQiLCJpYXQiOjE2MjA2MjIwMTQsImV4cCI6MTYyMDY2NTE3OH0.lebJTpD-rGTNAbgpai8fT559wH9_DwmvUJ6aDUCMZEJbyx0IkGiMSKqr2sWPyK5PsuEOszcMZgu-lv6F13a5z2cfQRk33X2AJoDJRJtwltOikbCjHwgmeXnSlHfaZI2XMQYLF7PDjxis1mG6-KSExcvVwW-hnwPQn3a29oErnXcUKBCMPC8pQqQ7MatVCqWjH45lHSF1P-We40OGs5_znlTTBWEcg-PDqLxWaV7CivyYu83gOREsUc0nXnkGc31RaxTXkI437wWZIk-z7ykoH5iyivvuLca-kkDuedL-C-FNDrHAV_Hz4PXWqSl0y2Nz-UhiojqfoQt3gwhVjRYaIQ'}
# NOTE: manually define and pass the array(s) of values to be scored in the next line
val="[300,310,369,350,390,380,370,398,4.04,0.48,1574,1199,585,22.44]"
vector="{\"input_data\":[{\"fields\":[\"BPT1\",\"BPT2\",\"BPT3\",\"BPT4\",\"BPT5\",\"BPT6\",\"BPT7\",\"BPT8\",\"Powerup Steam Flow Rate\",\"Ratio of outlet inlet temp\",\"Steam Supply Pressure\",\"Turbine Inlet Temperature\",\"Turbine Outlet Temperature\",\"Vibration\"],\"values\":["+val+"]}]}"
payload_scoring=json.loads(vector)
payload_scoringOld = {"input_data": [{"fields": ['BPT1','BPT2','BPT3','BPT4','BPT5','BPT6','BPT7','BPT8','Powerup Steam Flow Rate','Ratio of outlet inlet temp','Steam Supply Pressure','Turbine Inlet Temperature','Turbine Outlet Temperature','Vibration'], "values": [[300.0,310.0,369,350,390,380,370,398,4.04,.48,1574,1199,585,22.44]]}]}
response_scoring = requests.post('https://mas-maslab2-cp4d-cpd-mas-maslab2-cp4d.maslab-wdc07-b3c-16x64-18312db33a3427c911e9adf447e95207-0000.us-east.containers.appdomain.cloud/ml/v4/deployments/bbd9238a-3cff-459e-9aed-3b14c3b9449f/predictions?version=2021-05-03', json=payload_scoring, headers=header)
print("Scoring response")
print(json.loads(response_scoring.text))
response_data=json.loads(response_scoring.text)
for i in response_data['predictions']:
    print(i)
    fieldsData=i
    for j in fieldsData['values']:
        print('----final---'+str(j[0]))

'''header = {'Content-Type': 'application/json', 'username': 'admin','password':'password'}
response_scoring = requests.post('https://mas-maslab2-cp4d-cpd-mas-maslab2-cp4d.maslab-wdc07-b3c-16x64-18312db33a3427c911e9adf447e95207-0000.us-east.containers.appdomain.cloud/icp4d-api/v1/authorize', headers=header)
print("Scoring response")
print(json.loads(response_scoring.text))'''

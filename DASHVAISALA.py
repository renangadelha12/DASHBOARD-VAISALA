import re
import xml.etree.ElementTree as ET
import pandas as pd
mport folium
from folium.plugins import MousePosition
arquivo_CalculatedOzone = 'c:/Cod vaisala v2/arquivos/CalculatedOzone.xml'
arquivo_SoundingMetadata = 'c:/Cod vaisala v2/arquivos/SoundingMetadata.xml'
arquivo_OifParameters = 'c:/Cod vaisala v2/arquivos/OifParameters.xml'
arquivo_SurfaceObservations = 'c:/Cod vaisala v2/arquivos/SurfaceObservations.xml'
arquivo_SynchronizedSoundingData='c:/Cod vaisala v2/arquivos/SynchronizedSoundingData.xml'
arquivo_PtuResults = 'c:/Cod vaisala v2/arquivos/PtuResults.xml'
arquivo_GpsResults='c:/Cod vaisala v2/arquivos/GpsResults.xml'



def infos_CalculatedOzone(arquivo_CalculatedOzone):
    tree = ET.parse(arquivo_CalculatedOzone)
    root = tree.getroot()
    Row_SoundingIdPk = []
    RadioRxTimePk=[]
    DataSrvTime=[]
    PartialPressure=[]
    BoxTemperature=[]
    O3Current=[] 
    IntegratedOzone=[] 
    ResidualOzone=[]
    for child in root:
        Row = str(child.attrib.get('Row_SoundingIdPk'))
        Radio = str(child.attrib.get('RadioRxTimePk'))
        Data=str(child.attrib.get('DataSrvTime'))
        PartialPressure_=float(child.attrib.get('PartialPressure'))
        BoxTemperature_=float(child.attrib.get('BoxTemperature'))-273.15
        O3Current_=float(child.attrib.get('O3Current'))
        IntegratedOzone_=float(child.attrib.get('IntegratedOzone'))
        ResidualOzone_=float(child.attrib.get('ResidualOzone'))

        if 1!=0:
            Row_SoundingIdPk.append(Row)
            RadioRxTimePk.append(Radio)
            DataSrvTime.append(Data)
            PartialPressure.append(PartialPressure_)
            BoxTemperature.append(BoxTemperature_)
            O3Current.append(O3Current_)
            IntegratedOzone.append(IntegratedOzone_)
            ResidualOzone.append(ResidualOzone_)
    df_CalculatedOzone = pd.DataFrame({
    'DataSrvTime': DataSrvTime,
    'PartialPressure': PartialPressure,
     'PartialPressure':PartialPressure,
     'BoxTemperature':BoxTemperature,
     'O3Current':O3Current,
     'IntegratedOzone':IntegratedOzone,
     'ResidualOzone':ResidualOzone

})
            
    return df_CalculatedOzone
 
def infos_SoundingMetadata(arquivo_SoundingMetadata):
    tree = ET.parse(arquivo_SoundingMetadata)
    root = tree.getroot()
    for child in root:
        if child.attrib.get('MetadataKeyPk') == 'GAS_TYPE':
            gas_type = child.attrib.get('MetadataValue')
        if child.attrib.get('MetadataKeyPk') == 'FREE_TEXT':
           free_text = child.attrib.get('MetadataValue')
        if child.attrib.get('MetadataKeyPk') == 'SOUNDING_DATE':
           date = child.attrib.get('MetadataValue')
        if child.attrib.get('MetadataKeyPk') == 'SONDE_SERIAL_NUMBER':
           rs_number = child.attrib.get('MetadataValue')
           

    return gas_type,free_text,date,rs_number

def infos_OifParameters(arquivo_OifParameters):
    tree = ET.parse(arquivo_OifParameters)
    root = tree.getroot()
    SzSerialNumber='c'
    CalibrationPressure='c'
    FlowRate='c'
    BgCurrent='c'
    for child in root:
        SzSerialNumber=str(child.attrib.get('SzSerialNumber'))
        CalibrationPressure=str(child.attrib.get('CalibrationPressure'))
        FlowRate=float(child.attrib.get('FlowRate'))
        BgCurrent=float(child.attrib.get('BgCurrent'))
        
            
    return SzSerialNumber,CalibrationPressure,FlowRate,BgCurrent
    
def infos_SurfaceObservations(arquivo_SurfaceObservations):
    tree = ET.parse(arquivo_SurfaceObservations)
    root = tree.getroot()
    DataSrvTime='a' 
    Pressure='a' 
    LaunchSitePressure='a' 
    Temperature='a' 
    Humidity='a' 
    WindDirection='a' 
    WindSpeed='a' 
    PreviousTemperature='a'  
    DewpointTemperature='a'  
    WetBulbTemperature='a' 
    DryBulbTemperature='a' 

    for child in root:
        DataSrvTime=str(child.attrib.get('DataSrvTime')) 
        Pressure=str(child.attrib.get('Pressure'))  
        LaunchSitePressure=str(child.attrib.get('LaunchSitePressure')) 
        Temperature=float(child.attrib.get('Temperature')) 
        Humidity=float(child.attrib.get('Humidity'))  
        WindDirection=float(child.attrib.get('WindDirection')) 
        WindSpeed=float(child.attrib.get('WindSpeed')) 
        PreviousTemperature=float(child.attrib.get('PreviousTemperature')) 
        DewpointTemperature=float(child.attrib.get('DewpointTemperature')) 
        WetBulbTemperature=float(child.attrib.get('WetBulbTemperature')) 
        DryBulbTemperature=float(child.attrib.get('DryBulbTemperature')) 

    
        
        
            
    return DataSrvTime,Pressure,LaunchSitePressure,Temperature-273.15,Humidity,WindDirection,WindSpeed, PreviousTemperature-273.15,DewpointTemperature-273.15,WetBulbTemperature-273.15,DryBulbTemperature-273.15     

def infos_PtuResults(arquivo_PtuResults):
    tree = ET.parse(arquivo_PtuResults)
    root = tree.getroot()
    Row_SoundingIdPk = []
    RadioRxTimePk=[]
    DataSrvTime=[]
    SensorPressure=[]
    PressureFromHeight=[]
    Temperature=[] 
    Humidity=[] 
    Height=[]
    for child in root:
        Row = str(child.attrib.get('Row_SoundingIdPk'))
        Radio = str(child.attrib.get('RadioRxTimePk'))
        Data=str(child.attrib.get('DataSrvTime'))
        SensorPressure_=float(child.attrib.get('SensorPressure'))
        PressureFromHeight_=float(child.attrib.get('PressureFromHeight'))
        Temperature_=float(child.attrib.get('Temperature'))-273.15
        Humidity_=float(child.attrib.get('Humidity'))
        Height_=float(child.attrib.get('HeightFromGps'))

        if 1!=0:
            Row_SoundingIdPk.append(Row)
            RadioRxTimePk.append(Radio)
            DataSrvTime.append(Data)
            SensorPressure.append(SensorPressure_)
            PressureFromHeight.append(PressureFromHeight_)
            Temperature.append(Temperature_)
            Humidity.append(Humidity_)
            Height.append(Height_)
    df_PtuResults = pd.DataFrame({
     'PressureFromHeight':PressureFromHeight,
     'Temperature':Temperature,
     'Humidity':Humidity,
     'Height':Height

})
            
    return df_PtuResults
 
def infos_GpsResults(arquivo_GpsResults):
    tree = ET.parse(arquivo_GpsResults)
    root = tree.getroot()
    latitudes=[]
    longitudes=[]
    VelocityNorth=[]
    VelocityEast=[]
    for child in root:
        latitude = float(child.attrib.get('Wgs84Latitude', 0))
        longitude = float(child.attrib.get('Wgs84Longitude', 0))
        VelocityNorths=float(child.attrib.get('VelocityNorth', 0))
        VelocityEasts=float(child.attrib.get('VelocityEast', 0))
        if latitude != 0 and longitude != 0:
            latitudes.append(latitude)
            longitudes.append(longitude)
            VelocityNorth.append(VelocityNorths)
            VelocityEast.append(VelocityEasts)
    df_GpsResults = pd.DataFrame({
     'Latitude':latitudes,
     'Longitude':longitudes,
     'VelocityNorth':VelocityNorth,
     'VelocityEast':VelocityEast

})  
    return df_GpsResults

def infos_WindResults(arquivo_windresults):
    tree = ET.parse(arquivo_windresults)
    root = tree.getroot()
    WindDir=[]
    WindSpeed=[]
    WindNorth=[]
    WindEast=[]


    for child in root:
        wd = float(child.attrib.get('WindDir', 0))
        ws = float(child.attrib.get('WindSpeed', 0))
        wn=float(child.attrib.get('WindNorth', 0))
        we=float(child.attrib.get('WindEast', 0))
        if 1 != 'br' and 1 != 'alemanha':
            WindDir.append(wd)
            WindSpeed.append(ws)
            WindNorth.append(wn)
            WindEast.append(we)
    df_WindResults = pd.DataFrame({
     'WindDir':WindDir,
     'WindSpeed':WindSpeed,
     'WindNorth':WindNorth,
     'WindEast':WindEast

})        
    return df_WindResults

#<Row SoundingIdPk="c56e2de5-9083-47ab-a625-05836cd1a521" RadioRxTimePk="1135.624" DataSrvTime="2024-03-14T14:50:28.0643447" Pressure="1004.2" Temperature="305.65" Humidity="82.4" WindDir="125" WindSpeed="1" WindNorth="0.57357643635104616" WindEast="-0.8191520442889918" Height="41.889267581029621" GeometricHeight="42" PtuStatus="0" WindInterpolated="False" Latitude="-5.83672" Longitude="-35.20652" North="0" East="0" Up="0" Altitude="36.898211816474472" Dropping="0"/>



#base de dados para o DASHBOARD
SoundingMetadata=infos_SoundingMetadata(arquivo_SoundingMetadata)
CalculatedOzone=infos_CalculatedOzone(arquivo_CalculatedOzone)
PtuResults=infos_PtuResults(arquivo_PtuResults)
OifParameters=infos_OifParameters(arquivo_OifParameters)
SurfaceObservations=infos_SurfaceObservations(arquivo_SurfaceObservations)
GpsResults=infos_GpsResults(arquivo_GpsResults)
SynchronizedSoundingData=infos_WindResults(arquivo_SynchronizedSoundingData)

#print(len(SynchronizedSoundingData))
df_dash = pd.concat([CalculatedOzone, PtuResults,GpsResults,SynchronizedSoundingData], axis=1)
df_dash["TIME"] = pd.to_datetime(df_dash["DataSrvTime"])
df_dash['Hour']=df_dash['TIME'].dt.time

altura_max=max(df_dash['Height'])/1000
altura_max=f'{altura_max:.2f}'

df_dash['TotalOzone']=df_dash['IntegratedOzone']+df_dash['ResidualOzone']

critico=df_dash['Height'].idxmax()
df_dash=df_dash[:critico]
df_dash.head(critico)
print(SurfaceObservations)
#DataSrvTime,Pressure,LaunchSitePressure,Temperature,Humidity,WindDirection,WindSpeed, PreviousTemperature-273.15,DewpointTemperature-273.15,WetBulbTemperature-273.15,DryBulbTemperature-273.15
pressure_solo=SurfaceObservations[1]
Temperatura=SurfaceObservations[3]
umidade=SurfaceObservations[4]
Vel_vent=SurfaceObservations[6]
Vel_dir=SurfaceObservations[5]


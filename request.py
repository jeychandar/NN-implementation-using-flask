import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Unnamed: 0':82590,'ID':82591,'Nationality':57,'Age':47,'DaysSinceCreation':11,'AverageLeadTime':0,'LodgingRevenue':0,'OtherRevenue':0,'BookingsCanceled':0,'BookingsNoShowed':0,'PersonsNights':0,'RoomNights':0,'DaysSinceLastStay':-1,'DaysSinceFirstStay':-1,'DistributionChannel':3,'MarketSegment':6,'SRHighFloor':0,'SRLowFloor':0,'SRAccessibleRoom':0,'SRMediumFloor':0,'SRBathtub':0,'SRShower':0,'SRCrib':0,'SRKingSizeBed':0,'SRTwinBed':0,'SRNearElevator':0,'SRAwayFromElevator':0,'SRNoAlcoholInMiniBar':0,'SRQuietRoom':0})

print(r.json())
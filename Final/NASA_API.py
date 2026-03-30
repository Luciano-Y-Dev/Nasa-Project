from dotenv import load_dotenv
import os
import requests as rq
import pandas as pd
import reflex as rx 

load_dotenv()

exoPlanetsURL = "https://api.nasa.gov/planetary/apod"


def imageToBirthDay(birthDayDate):
    
    query_params = {
        "api_key" : os.getenv("NASA_API_KEY"),
        "date" : birthDayDate
        }
    
    dataSet = rq.get(exoPlanetsURL, params = query_params)
    dataBase = dataSet.json()
    if isinstance(dataBase, dict):
        dataBase = [dataBase]
        dataFrame = pd.DataFrame(dataBase)
    return dataFrame



def img_title_info(dataFrame):
    
    def Img_API_URL():
        url_imagen = dataFrame['url'].iloc[0]
        return url_imagen

    def Info_API():
        infoText = dataFrame['explanation'].iloc[0]
        return infoText

    def Title_API():
        titleText = dataFrame['title'].iloc[0]
        return titleText
    
    return Title_API(), Info_API(), Img_API_URL()

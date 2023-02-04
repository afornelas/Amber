import requests
import json
import pprint
import utils.time_tools

def weather_condition_code(code):
    '''Translates openweatherapi.org weather condition codes to a string to be used in a human readable forecast'''
    if code == 800:
        return "clear"
    elif code == 801:
        return "partly cloudy"
    elif code == 802:
        return "cloudy"
    elif code == 803:
        return "very cloudy"
    elif code == 804:
        return "overcast"
    elif code >= 200 and code <= 232:
        return "stormy"
    elif code == 300:
        return "a light intensity drizzle"
    elif code == 301:    
        return "a drizzle"
    elif code == 302:
        return "a heavy intensity drizzle"
    elif code == 310:
        return "a light intensity drizzle with light rain"
    elif code == 311:
        return "rainy"
    elif code == 312:
        return "high intensity drizzle rain"
    elif code == 313:
        return "varying between rain and drizzle"
    elif code == 314:
        return "varying between heavy shower rain and drizzle"
    elif code == 321:
        return "a mix of shower and drizzle"
    elif code == 500:
        return "light rain"
    elif code == 501:
        return "moderate rain"
    elif code == 502:
        return "heavy intensity rain"
    elif code == 503:
        return "very heavy rain"
    elif code == 504:
        return "extreme rain"
    elif code == 511:
        return "freezing rain"
    elif code == 520:
        return "light intensity shower rain"
    elif code == 521:
        return "shower rain"
    elif code == 522:
        return "heavy intensity shower rain"
    elif code == 531:
        return "ragged shower rain"
    elif code == 600:
        return "light snow"
    elif code == 601:
        return "snowy"
    elif code == 602:
        return "heavy snow"
    elif code == 611:
        return "sleet"
    elif code == 612:
        return "shower sleet"
    elif code == 615:
        return "light rain and snow"
    elif code == 616:
        return "rain and snow"
    elif code == 620:
        return "light shower snow"
    elif code == 621:
        return "shower snow"
    elif code == 622:
        return "heavy shower snow"
    elif code == 701:
        return "misty"
    elif code == 711:
        return "smoky"
    elif code == 721:
        return "hazy"
    elif code == 731:
        return "dusty"
    elif code == 741:
        return "foggy"
    elif code == 751:
        return "sandy"
    elif code == 761:
        return "dusty"
    elif code == 762:
        return "filled with volcanic ash"
    elif code == 771:
        return "squalls"
    elif code == 781:
        return "including a tornado"

def human_readable_forecast(day_id,flags):
    '''Returns information from weather json file pulled from openweatherapi.org as a 
    string to be used in a human readable forecast that is recited to the user'''

    current_temp = weather_raw['current']['temp']
    current_condition = weather_raw['current']['weather'][0]['description']

    weather_day = weather_raw['daily'][day_id]
    condition = weather_condition_code(weather_day['weather'][0]['id'])

    weather_str = ""



    if day_id == 0:
        weather_str += f'The weather outside is currently {current_condition} and the temperature is {current_temp} degrees.'
    weather_str += f'On {('Today,' if day_id == 0 else day_to_str)}, the weather outside will be {condition} with a high of {temp_max} and a low of {temp_min} degrees.'

    return weather_str

weatherOffset = 0.96 #OpenWeather is far less unreliable than darksky and as such, all weather events are multiplied by this number to reflect other sources
openWeatherApiKey = ""
location = [33.643242,-117.842006]

weather_json = requests.get("http://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=minutely&units=imperial&appid={}".format(location[0],location[1],openWeatherApiKey))
weather_raw = json.loads(weather_json.text)

units = {
    "Imperial":{
        "Temperature":'degrees fahrenheit',
        "Pressure":'hPa',
        "Percent":'%',
        "Visibilty":'meters',
        "Speed":'miles per hour',
        "time":'Unit UTC'
    }
}

weather = {
    'metadata':{
        'lat':weather_raw['lat'],
        'lon':weather_raw['lon'],
        'polled':weather_raw['current']['dt'],
        'TZ':[weather_raw['timezone'],weather_raw['timezone_offset']]
    },
    'current': {
        'sunrise':'The sunrise is at {}'.format(utils.time_tools.to_hour(weather_raw['current']['sunrise'])),
        'sunset':'The sunset is at {}'.format(utils.time_tools.to_hour(seconds=weather_raw['current']['sunset'])),
        'temperature':'The current temperature is {:.0f} {}'.format(weather_raw['current']['temp'],units['Imperial']['Temperature']),
        'feels-like':'The current weather feels like {:.0f} {}'.format(weather_raw['current']['feels_like'],units['Imperial']['Temperature']),
        'pressure':'The current pressure is {:.0f} {}'.format(weather_raw['current']['pressure'],units['Imperial']['Pressure']),
        'humidity':'The current humidity is {:.0f} {}'.format(weather_raw['current']['humidity'],units['Imperial']['Percent']),
        'wind-speed':'The current wind speed is {:.0f} {} with a direction of {} degrees'.format(weather_raw['current']['wind_speed'],units['Imperial']['Speed'],weather_raw['current']['wind_deg']),
        'clouds':'The current cloud coverage is {:.0f} {}'.format(weather_raw['current']['clouds'],units['Imperial']['Percent']),
        'uv-index':'The current UV index is {:.0f} {}'.format(weather_raw['current']['uvi'],units['Imperial']['Percent']),
        # 'weather':'The current weather is {weather code} and {temp} {unit} with a high of {temp} {unit} and a low of {temp} {unit}'.format()
    }
}

# print("http://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=minutely&units=imperial&appid={}".format(location[0],location[1],openWeatherApiKey))

human_readable_forecast(0)
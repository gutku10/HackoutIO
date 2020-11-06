import pyrebase
import json
import pprint
import random

config = {
    'apiKey': "AIzaSyBV4BEC6qhTZsl9CbIOZTPEs1U2EAN16bQ",
    'authDomain': "hackoutio.firebaseapp.com",
    'databaseURL': "https://hackoutio.firebaseio.com",
    'projectId': "hackoutio",
    'storageBucket': "hackoutio.appspot.com",
    'messagingSenderId': "601372943342",
    'appId': "1:601372943342:web:b84657cea082f9751da4ff"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

x = {
    "Admin": {
        "Utkrisht Agrawal": {
            "Phone Number": "9811830165",
            "Email": "utkrisht@gmail.com",
            "Name": "Utkrisht Agrawal",
            "Password": "clashlone"
        },
        "Agam Pal Singh Bhatia": {
            "Phone Number": "9811830165",
            "Email": "agam@gmail.com",
            "Name": "Agam Pal Singh Bhatia",
            "Password": "clashlone"
        }
    },
    "Animals": {
        "Cows": {
            "Cow 1": {
                "Category": "Cow",
                "ID": "Cow 1",
                "Status": "Healthy",
                "Sensors": {
                    "Acc X": {
                        "Status": True,
                        "Value": 0
                    },
                    "Acc Y": {
                        "Status": True,
                        "Value": 0
                    },
                    "Acc Z": {
                        "Status": True,
                        "Value": 0
                    },
                    "Gyro X": {
                        "Status": True,
                        "Value": 0
                    },
                    "Gyro Y": {
                        "Status": True,
                        "Value": 0
                    },
                    "Gyro Z": {
                        "Status": True,
                        "Value": 0
                    },
                    "Daily Steps": {
                        "Status": True,
                        "Value": 0
                    },
                    "Body Temperature": {
                        "Status": True,
                        "Value": 0
                    },
                    "Outside Temperature": {
                        "Status": True,
                        "Value": 0
                    },
                    "Humidity": {
                        "Status": True,
                        "Value": 0
                    },
                    "Microphone": {
                        "Status": True,
                        "Value": 0
                    }
                },
                "Location": {
                    "Latitude": {
                        "Status": True,
                        "Value": 0
                    },
                    "Longitude": {
                        "Status": True,
                        "Value": 0
                    }
                }
            },
            "Cow 2": {
                "Category": "Cow",
                "ID": "Cow 2",
                "Status": "Not Healthy",
                "Sensors": {
                    "Acc X": {
                        "Status": True,
                        "Value": 0
                    },
                    "Acc Y": {
                        "Status": True,
                        "Value": 0
                    },
                    "Acc Z": {
                        "Status": True,
                        "Value": 0
                    },
                    "Gyro X": {
                        "Status": True,
                        "Value": 0
                    },
                    "Gyro Y": {
                        "Status": True,
                        "Value": 0
                    },
                    "Gyro Z": {
                        "Status": True,
                        "Value": 0
                    },
                    "Daily Steps": {
                        "Status": True,
                        "Value": 0
                    },
                    "Body Temperature": {
                        "Status": True,
                        "Value": 0
                    },
                    "Outside Temperature": {
                        "Status": True,
                        "Value": 0
                    },
                    "Humidity": {
                        "Status": True,
                        "Value": 0
                    },
                    "Microphone": {
                        "Status": True,
                        "Value": 0
                    }
                },
                "Location": {
                    "Latitude": {
                        "Status": True,
                        "Value": 0
                    },
                    "Longitude": {
                        "Status": True,
                        "Value": 0
                    }
                }
            }
        },
        "Buffalo": {
            "Buffalo 1": {
                "Category": "Buffalo",
                "ID": "Buffalo 1",
                "Status": "Healthy",
                "Sensors": {
                    "Acc X": {
                        "Status": True,
                        "Value": 0
                    },
                    "Acc Y": {
                        "Status": True,
                        "Value": 0
                    },
                    "Acc Z": {
                        "Status": True,
                        "Value": 0
                    },
                    "Gyro X": {
                        "Status": True,
                        "Value": 0
                    },
                    "Gyro Y": {
                        "Status": True,
                        "Value": 0
                    },
                    "Gyro Z": {
                        "Status": True,
                        "Value": 0
                    },
                    "Daily Steps": {
                        "Status": True,
                        "Value": 0
                    },
                    "Body Temperature": {
                        "Status": True,
                        "Value": 0
                    },
                    "Outside Temperature": {
                        "Status": True,
                        "Value": 0
                    },
                    "Humidity": {
                        "Status": True,
                        "Value": 0
                    },
                    "Microphone": {
                        "Status": True,
                        "Value": 0
                    }
                },
                "Location": {
                    "Latitude": {
                        "Status": True,
                        "Value": 0
                    },
                    "Longitude": {
                        "Status": True,
                        "Value": 0
                    }
                }
            },
            "Buffalo 2": {
                "Category": "Buffalo",
                "ID": "Buffalo 2",
                "Status": "Healthy",
                "Sensors": {
                    "Acc X": {
                        "Status": True,
                        "Value": 0
                    },
                    "Acc Y": {
                        "Status": True,
                        "Value": 0
                    },
                    "Acc Z": {
                        "Status": True,
                        "Value": 0
                    },
                    "Gyro X": {
                        "Status": True,
                        "Value": 0
                    },
                    "Gyro Y": {
                        "Status": True,
                        "Value": 0
                    },
                    "Gyro Z": {
                        "Status": True,
                        "Value": 0
                    },
                    "Daily Steps": {
                        "Status": True,
                        "Value": 0
                    },
                    "Body Temperature": {
                        "Status": True,
                        "Value": 0
                    },
                    "Outside Temperature": {
                        "Status": True,
                        "Value": 0
                    },
                    "Humidity": {
                        "Status": True,
                        "Value": 0
                    },
                    "Microphone": {
                        "Status": True,
                        "Value": 0
                    }
                },
                "Location": {
                    "Latitude": {
                        "Status": True,
                        "Value": 0
                    },
                    "Longitude": {
                        "Status": True,
                        "Value": 0
                    }
                }
            }
        }
    },
        "Total": {
            "Admin": 2,
            "Animals": 2,
            "Cows": 2,
            "Buffalos": 2,
            "Devices": 18
        }
    }
db.set(x)

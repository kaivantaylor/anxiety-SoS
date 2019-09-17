# Anxiety SoS
Using the fitbit API, we are able to make request to the fitbit server and receive biometrics in JSON format. From the JSON format, the data was parsed for specific categories such as heart rate, calorie intake, and sleep levels. This was converted into a CSV files and was able to request for updates every 30 seconds. Using data, we created an algorithm that detected high levels of anxiety. Once detected, a text message was sent to the user's friends and family notifying them to reach out to the user using Twillo API.

# What challenges did we face?
We lacked the amount of variables we could use to determine anxiety. The fitbit API only allows so much information that is publicly available and other data such as blood pressure would have been helpful. The fitbit only received data for 1 1/2 days which may have not been enough data to create an accurate algorithm for the user since not all user's experience the same symptoms for anxiety attacks.

# Test Subject
Rendell was used as the test subject for this project. We wanted to have a single person use the fitbit in order to maintain consistency with our data. His body mass index was calculated to estimate the average amount of calorie intake he should be receiving. He experienced little to no sleep due to the environment which was extremely cold during the nights. On top of that, the rooms were always lit which could be a correlation to his poor sleep quality as determined by the fitbit. His minutes in deep sleep for the two nights were 51 and 83 minutes with a total of 176 and 219 total minutes of sleep respectively.

# Collaborators
[Elijsha](https://github.com/IAmYew)

[Marty](https://github.com/martyjapilado)

[Rendell](https://github.com/IntenseMarrow9)

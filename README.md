# API-Integration-Data-Visualization

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: KOLLURI BHANUTEJA

*INTERN ID*: CT08DF855

*DOMAIN*: PYTHON

*DURATION*: 8 WEEKS

*MENTOR*: NEELA SANTOSH

##This project demonstrates the integration of a real-time weather API with Python for the purpose of extracting and visualizing weather forecast data. The main objective was to build a simple but effective tool that fetches weather data from the OpenWeatherMap API, processes it using Python libraries, and visually represents temperature trends over several days. This task allowed me to explore key areas in programming such as API integration, JSON data parsing, and data visualization using industry-standard Python tools.

The OpenWeatherMap API (https://openweathermap.org/) was used to retrieve a 5-day weather forecast for the city of Vijayawada. The API returns data in JSON format, where each forecast entry corresponds to a 3-hour interval. By accessing this structured data, I was able to extract essential weather metrics such as temperature and timestamps. The integration process involved constructing a properly formatted URL containing the API key and city name, sending an HTTP request using the requests library, and handling the response in JSON format. This taught me how APIs work under the hood and how to communicate with external services programmatically.

The raw weather data was then organized using the pandas library. Pandas allowed me to convert the JSON data into a DataFrame for easier manipulation and analysis. I parsed the datetime values and grouped the data by individual dates to calculate the average temperature per day. This transformation helped reduce data noise and made the final output more readable and insightful. It also introduced me to important concepts such as data grouping, aggregation, and datetime handling—all of which are foundational in data analysis workflows.

For data visualization, I used both matplotlib and seaborn. While matplotlib provided the basic plotting functionality, Seaborn added aesthetic styling and clarity to the graphs. The final output was a line chart that showed the daily average temperatures over the forecast period. The chart used labeled axes, gridlines, rotated date labels, and a title for context. This aspect of the project helped me understand how raw numerical data can be converted into an intuitive and visually appealing format, which is a critical skill in fields like data science and analytics.

I developed the entire project using Visual Studio Code (VS Code) as my primary code editor. VS Code provided a streamlined development environment with useful features like syntax highlighting, auto-completion, and integrated terminal access. I found it particularly effective for running and debugging Python scripts, managing virtual environments, and installing necessary libraries. It also supported version control through Git integration, making it easier to maintain code history and manage updates.

This type of task has several real-world applications. Weather-based visualization tools are vital in domains such as agriculture, logistics, transportation, and environmental monitoring. For example, farmers can use forecast insights to plan irrigation schedules, while delivery companies can use weather trends to optimize routes. Furthermore, this project can be extended into a weather dashboard, a mobile app, or even integrated into IoT-based home automation systems that respond to weather changes.

In conclusion, this project combined practical programming, real-time data usage, and data visualization into a cohesive application. It helped me gain confidence in working with APIs, manipulating datasets using pandas, and creating visual outputs using Seaborn. Most importantly, it demonstrated how even a beginner-level Python script can connect with powerful external systems and produce meaningful, real-world insights. This exercise is an excellent stepping stone for deeper learning in data science, full-stack development, or machine learning workflows.


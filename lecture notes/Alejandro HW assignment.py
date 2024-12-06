import matplotlib.pyplot as plt

# Links used:
# https://ifr.org/ifr-press-releases/news/wr-report-all-time-high-with-half-a-million-robots-installed
# https://ifr.org/wr-industrial-robots/

years2022Report = [2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021] #line plot
installation2022 = [166, 159, 178, 221, 254, 304, 400, 423, 391, 394, 517] #installation of industrial robots, per 1,000 units

years2023Report = [2017,2018,2019,2020,2021,2022,2023,2024,2025,2026] #scatter plot
installation2023 = [400, 423, 387, 390, 526, 553, 593,622, 662, 718] #installation of industrial robots, per 1,000 units

nations =  ["Republic of Korea", "Singapore", "Japan", "Germany", "China"] #pie chart of top 5 nations with most robots
roboticDensity = [1012, 730, 415, 397, 392] # robots installed per 10,000 employees

industries = ["Electronics", "Automotive", "Metal/Machinery", "Plastic/Chemicals", "Food"] #2023 data report on 2022
robotInstallation = [157, 136, 66, 24, 15] # Annual installations of industrial by customer industry. (1,000 units)

#line plot
plt.subplot(2,2,1)
plt.plot(years2022Report, installation2022, label = "2022 Report", color = "royalblue", linestyle = 'solid', marker = 'o')

plt.xlabel("Years")
plt.ylabel("Installation per 1,000 units")
plt.title("Annual Install of Industrial Robots")
plt.grid(True, linestyle = '--', alpha = 1)

#Scatter plot
plt.subplot(2,2,3)
plt.scatter(years2023Report, installation2023, label = "2023 Report", color = "steelblue", marker = 'o', s =70)

plt.xlabel("Years")
plt.ylabel("Installation per 1,000 units")
plt.title("Annual Install of Industrial Robots")
plt.grid(True, linestyle = '--', alpha = 1)

#Bar plot
plt.subplot(2,2,2)
plt.bar(industries, robotInstallation, color = 'cornflowerblue')
plt.xlabel('Industries')
plt.ylabel('Installation of Robots in 2022')
plt.title('Top Robotic Industries')

#Pie chart
plt.subplot(2,2,4)
plt.pie(roboticDensity, labels = nations, colors = ['steelblue','royalblue', 'cornflowerblue', 'lightsteelblue', "slategrey"] )
plt.title("Top 5 Nations with Highest Robotic Densities ")

plt.tight_layout()
plt.show()
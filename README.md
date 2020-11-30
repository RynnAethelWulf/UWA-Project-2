<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p>

<h3 align="center">ETL: Video Game Analysis Project</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center">  A report that breaks down the analysis of largest collection of video games library.
    <br> 
</p>

## 📝 Table of Contents

- [Team](#Team)
- [About](#about)
- [Getting Started](#getting_started)
- [Observable Trends](#trends)
- [Acknowledgments](#acknowledgement)

## 🧐 Team <a name = "Team"></a>
•	Ezra Tassone
•	Parastoo Razavi
•	Bimal Prabha


## 🧐 About <a name = "about"></a>
**Description:**
ELT stands for “extract, load, and transform” — the processes a data pipeline uses to reproduce data from a source system into a target system such as a cloud data warehouse.
Once we have identified our datasets, perform ETL on the data. Our plan and document followed:
- The sources of data that we will extract from.
- The type of transformation needed for this data (cleaning, joining, filtering, aggregating, etc).
- The type of final production database to load the data into (relational or non-relational).
- The final tables or collections that will be used in the production database.


## 🏁 Getting Started <a name = "getting_started"></a>

**Questions to Answer:** <br>
1.	What is the correlation of country happiness and 7 factors?
2.	What is determining factor look like comparing to bottom 10?
3.	Do the countries in top 10 and bottom 10 stay consistent over the year?
4.	What are the countries that making greatest changes?
5.	What are the counties did not make any changes?
6.	Can we do a prediction in year 2020?
7.	Which region has the happiest countries?


## ✍️ Observable Trends <a name = "trends"></a>

![Happiness Ranking 2015-2019](Output/ranking.png)
* The world’s happiest countries are primarily in North Western Europe, North America, and Australia & New Zealand. 

* Economy (GDP per capita) is the most important factor in evaluating a country’s happiness.

* Economy is also strongly positively correlated with other factors like Family and Health. 

* Another interesting observable trend, GDP and generosity has negative correlation factor. Reinforcing that,income does not relate to how generous you are.

![Correaltion_Heatmap](Output/2019_Heatmap.png)

*	Heatmap strongly suggest GDP and family with the score above 75%, has the highest cor-relationship with happiness score.

* In much lower ranked countries even though their score was low, their family score was almost on par with the top 10 countries. Yes, there is a noticeable dip in 2016 but it came back stronger than ever in the last 3 years.

![Top Bottom Analysis](Output/2019_TopBottom_Analysis.png)

* In 2015  australia,north America  , some of European  and Asian countries were dominated by GDP. And again in 2016 majority of world happiness was influenced by GDP.

* From 2017 to 2019 we have another interesting observation – it was not the income, but in fact it was family score which dominated the world happiness score.

### Future Prediction of Australia - Linear Regression
Based on our rankings from the 2015 to 2019, we’ve made some predictions on the happiness score of Australia along with the predicted happiness score of the top 10th country (meaning the minimum score to get into the top 10) to see if we will make it to the top 10. 

![Regression](Output/Australia_Happiness_Score.png)

### Bonus Part - Happiness Comparison with suicide Rate in the World

![Comparison](Output/happiness_suicide_2019.png)

We have already established that European countries are  happiest countries in the world. Simultaneously they have highest suicide rates among other countries.
But, there is no evidence which shows that the countries with higher happiness score will have high suicide rate. And Australia is not there, which is good.

![Suicid Rate Comparison Aus vs Finland](Output/Suice_Rate_of_Australia_vs_Finland.png)

Finland is an example of a country with a high happiness score and high suicide rate. Australia's suicide rate is lesser than, most of the European nations.  Though Australia's suicide rate is lesser than, most of the European nations, our genrosity is higher than the top country and family values are on par with rank no. 1 So give a pat on your back for being kind and give a hug to your family

### Conclusion 
This analysis illustrated that the world’s happiest countries are primarily in North Western Europe, North America, and Australia & New Zealand. It also revealed that Economy (GDP per capita) is the most important factor in evaluating a country’s happiness. Unsurprisingly, the happiest countries and world regions generally tended to be ones with strong and stable economies. 

The importance of Economy is also strongly positively correlated with those of Family and Health. This is expected, since more economic stability and higher GDP per capita generally encourages stable and comfortable family life as well as increases the availability of proper medical resources and healthcare. These factors then weigh more when determining overall happiness. 

## 🎉 Acknowledgements <a name = "acknowledgement"></a>
- UWA Data Science
- Data source: https://www.kaggle.com/mathurinache/world-happiness-report?select=2020.csv
- Data source: Gmap – geography of the region and country
- Institute of Health Metrics and Evaluation (IHME), Global Burden of Disease (GBD): http://ghdx.healthdata.org/gbd-results-tool
- Rest Countries API: https://restcountries.eu/rest/v2/


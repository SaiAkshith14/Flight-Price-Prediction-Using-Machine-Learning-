# ✈️ AirLine Analytics Using Machine Learning and Power BI

## 📌 Project Description
This project focuses on predicting the price of flight tickets based on various features such as airline, source, destination, duration, stops, and class.  
I performed data cleaning, preprocessing (including outlier handling and feature scaling), feature engineering, and applied multiple machine learning models to achieve high accuracy in predictions.  

After evaluating different models, **Random Forest Regressor** delivered the best performance with excellent accuracy and minimal error.

**Power BI** was implemented to create interactive dashboards and reports, enabling clear visualization of airline pricing trends, route-wise fare variations, demand patterns, and key factors influencing ticket prices. These dashboards enhance business understanding and decision-making by transforming historical data into actionable insights.

---

## 💼 Business Problem
In the airline industry, pricing strategy plays a crucial role in revenue optimization. Flight ticket prices vary significantly due to factors like demand, seasonality, travel class, and duration.  

The business problem here is:  
👉 *"How can airlines and travel agencies accurately predict flight prices to provide competitive fares while maximizing revenue?"*  

This predictive system helps:  
- Customers plan trips with fair price expectations.  
- optimize pricing strategies using predictive models and historical trend analysis.  
- Gain transparency and trust through clear visual reporting and data-backed insights.
- Power BI dashboards, built on cleaned and processed historical data, provide interactive insights into pricing trends, route-wise fare behavior, airline comparisons, and demand patterns.



---

## 🛠️ Tools and Technologies
- **Programming Language**: Python  
- **Libraries**: Pandas, NumPy, Scikit-learn  
- **Scaling Technique**: RobustScaler  
- **Model Used**: Random Forest Regressor  
- **Evaluation Metrics**:  
  - Mean Absolute Error (MAE): `0.0318`  
  - Mean Squared Error (MSE): `0.0034`  
  - R² Score: `0.9818`
- **Visualization Tool**: Power BI 

---

## 🔎 Insights

- Vistara operates the highest number of flights and also leads in pricing, indicating a strong market presence and premium positioning.
- The Bangalore → Mumbai route is the most profitable, driven by heavy corporate traffic and consistently higher fares.
- Business class contributes nearly 79% of the total revenue, even though more passengers travel in economy.
   - This is because business class tickets are priced significantly higher, especially on high-demand corporate routes like Bangalore–Mumbai.
   - As a result, business class generates a disproportionately large share of revenue despite lower passenger volume.
- Evening flights show higher demand from business travelers, reflecting common corporate travel patterns where professionals prefer evening departures after work hours.



---

## 📁 Project Structure
1. `flight_price_prediction.ipynb` → Main notebook  
2. `cleaned_flight_data.csv` → Processed dataset  
3. `business.csv` / `economy.csv` → Input datasets  
4. `model.zip` → Trained model  
5. `app.py` → Deployment script  
6. `requirements.txt` → Dependencies
7. `Airline Analytics pbix` → Power BI Dashboards 
8. `Power BI Images` → Dashboards/Reporting

---

## 🌍 Significance & Business Impact
- Enables airlines to set competitive and profitable pricing using ML predictions and Power BI insights.
- Helps travel agencies and customers understand price trends through interactive dashboards.
- Supports future dynamic pricing systems with ML models backed by BI-driven monitoring.

---

## 🚀 Deployment
This predictive model has been deployed as an **interactive web application using Streamlit**.  
Users can input details such as **airline, source, destination, stops, duration, and class**, and the app will instantly predict the **flight price**.  

👉 **Try it out here:** [Flight Price Predictor Web App](https://qx5hynvnar8scogr9kz84d.streamlit.app/)  

This makes the solution practical, user-friendly, and impactful for both **businesses and customers**.

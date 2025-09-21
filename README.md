# ✈️ Flight Price Prediction using Machine Learning

## 📌 Project Description
This project focuses on predicting the price of flight tickets based on various features such as airline, source, destination, duration, stops, and class.  
I performed data cleaning, preprocessing (including outlier handling and feature scaling), feature engineering, and applied multiple machine learning models to achieve high accuracy in predictions.  

After evaluating different models, **Random Forest Regressor** delivered the best performance with excellent accuracy and minimal error.

---

## 💼 Business Problem
In the airline industry, pricing strategy plays a crucial role in revenue optimization. Flight ticket prices vary significantly due to factors like demand, seasonality, travel class, and duration.  

The business problem here is:  
👉 *"How can airlines and travel agencies accurately predict flight prices to provide competitive fares while maximizing revenue?"*  

This predictive system helps:  
- Customers plan trips with fair price expectations.  
- Airlines and agencies optimize pricing strategies.  
- Enhances transparency and trust in ticket pricing.  

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

---

## 🔎 Insights
- Flight ticket prices are highly influenced by **airline type, number of stops, and travel class**.  
- **Duration** and **departure time slots** (Morning/Evening/Night) significantly impact ticket costs.  
- Premium classes (Business) have considerably higher prices than Economy.  
- Non-stop flights generally cost less compared to 1-stop or 2+ stop flights.  

---

## 📁 Project Structure
1. `flight_price_prediction.ipynb` → Main notebook  
2. `cleaned_flight_data.csv` → Processed dataset  
3. `business.csv` / `economy.csv` → Input datasets  
4. `model.zip` → Trained model  
5. `app.py` → Deployment script  
6. `requirements.txt` → Dependencies  

---

## 🌍 Significance & Business Impact
- Helps **airlines** set competitive yet profitable pricing strategies.  
- Provides **travel agencies** with predictive insights to enhance customer satisfaction.  
- Assists **customers** in planning trips with better awareness of price trends.  
- Can be extended to dynamic pricing systems for real-world airline businesses.  

---

## 🚀 Deployment
This predictive model has been deployed as an **interactive web application using Streamlit**.  
Users can input details such as **airline, source, destination, stops, duration, and class**, and the app will instantly predict the **flight price**.  

👉 **Try it out here:** [Flight Price Predictor Web App](https://qx5hynvnar8scogr9kz84d.streamlit.app/)  

This makes the solution practical, user-friendly, and impactful for both **businesses and customers**.

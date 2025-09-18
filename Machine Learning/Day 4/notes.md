# Day 4 – Machine Learning  

###  What I Learned Today  
- Learned how to **split data** into training and testing sets  
- Implemented my **first regression model** using `LinearRegression` from scikit-learn  
- Visualized predictions vs actual values with a scatter plot  

---

###  Steps Done  
1. **Splitting Data**  
   - Used `train_test_split` to divide dataset into training & testing sets  
   - Shape check: Training set (15480, 8), Testing set (5160, 8)  

2. **Training the Model**  
   - Created `LinearRegression()` object  
   - Trained (`fit`) the model with training data  

3. **Making Predictions**  
   - Predicted values with `predict()` on test set  
   - Compared predictions vs actual values  

4. **Visualization**  
   - Scatter plot of `y_test` vs `y_pred`  
   - Showed how well regression predictions align with actual house values  

---

###  Reflection  
- First hands-on ML model 
- Understood how a simple **linear regression** can model housing prices  
- Visualization helps in checking prediction accuracy visually  
- Next step: learn **evaluation metrics** like RMSE, R² score, MAE  


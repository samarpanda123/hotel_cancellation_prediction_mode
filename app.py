# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 00:22:07 2020

@author: Dell
"""
from flask import Flask, render_template, request
import jsonify
import requests
import pickle 
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler

app=Flask(__name__)
model=pickle.load(open('random_forest_regression_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')




standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
    #    is_canceled=int(request.form['is_canceled'])
        lead_time=int(request.form['lead_time'])
        arrival_date_year =int(request.form['arrival_date_year'])
        arrival_date_month=int(request.form['arrival_date_month'])
        arrival_date_day_of_month=int(request.form['arrival_date_day_of_month'])
        stays_in_weekend_nights=int(request.form['stays_in_weekend_nights'])
        stays_in_week_nights=int(request.form['stays_in_week_nights'])
        adults=int(request.form['adults'])
        children=int(request.form['children'])
        babies=int(request.form['babies'])
        is_repeated_guest=int(request.form['is_repeated_guest'])
        previous_cancellations=int(request.form['previous_cancellations'])
        previous_bookings_not_canceled=int(request.form['previous_bookings_not_canceled'])
        booking_changes=int(request.form['booking_changes'])
        days_in_waiting_list=int(request.form['days_in_waiting_list'])
        adr=float(request.form['adr'])
        required_car_parking_spaces=int(request.form['required_car_parking_spaces'])
        total_of_special_requests=int(request.form['total_of_special_requests'])
        
        hotel_Resort=request.form['hotel_Resort']
        if(hotel_Resort=='hotel_Resort'):
            hotel_Resort=1
        else:      
            hotel_Resort=0

        meal_FB=request.form['meal_FB']
        if(meal_FB=='meal_FB'):
            meal_FB=1
            meal_HB=0
            meal_SC=0
            meal_Undefined=0
            meal_BB=0
        elif(meal_FB=='meal_HB'):   
            meal_FB=0
            meal_HB=1
            meal_SC=0
            meal_Undefined=0
            meal_BB=0
        elif(meal_FB=='meal_SC'):   
            meal_FB=0
            meal_HB=0
            meal_SC=1
            meal_Undefined=0
            meal_BB=0 
        elif(meal_FB=='meal_Undefined'):   
            meal_FB=0
            meal_HB=0
            meal_SC=0
            meal_Undefined=1
            meal_BB=0
        else:
            meal_FB=0
            meal_HB=0
            meal_SC=0
            meal_Undefined=0
            meal_BB=1           

        market_segment_Complementary=request.form['market_segment_Complementary']
        if(market_segment_Complementary=='market_segment_Complementary'):
            market_segment_Complementary=1
            market_segment_Corporate=0
            market_segment_Direct=0
            market_segment_Groups=0
            market_segment_Offline=0
            market_segment_Online =0
            market_segment_Undefined=0
            market_segment_Aviation=0

        elif(market_segment_Complementary=='market_segment_Corporate'):
            market_segment_Complementary=0
            market_segment_Corporate=1
            market_segment_Direct=0
            market_segment_Groups=0
            market_segment_Offline=0
            market_segment_Online =0
            market_segment_Undefined=0
            market_segment_Aviation=0    

        elif(market_segment_Complementary=='market_segment_Direct'):
            market_segment_Complementary=0
            market_segment_Corporate=0
            market_segment_Direct=1
            market_segment_Groups=0
            market_segment_Offline=0
            market_segment_Online =0
            market_segment_Undefined=0
            market_segment_Aviation=0 

        elif(market_segment_Complementary=='market_segment_Groups'):
            market_segment_Complementary=0
            market_segment_Corporate=0
            market_segment_Direct=0
            market_segment_Groups=1
            market_segment_Offline=0
            market_segment_Online =0
            market_segment_Undefined=0
            market_segment_Aviation=0 

        elif(market_segment_Complementary=='market_segment_Offline'):
            market_segment_Complementary=0
            market_segment_Corporate=0
            market_segment_Direct=0
            market_segment_Groups=0
            market_segment_Offline=1
            market_segment_Online =0
            market_segment_Undefined=0
            market_segment_Aviation=0  

               
        elif(market_segment_Complementary=='market_segment_Online'):
            market_segment_Complementary=0
            market_segment_Corporate=0
            market_segment_Direct=0
            market_segment_Groups=0
            market_segment_Offline=0
            market_segment_Online =1
            market_segment_Undefined=0
            market_segment_Aviation=0

        elif(market_segment_Complementary=='market_segment_Undefined'):
            market_segment_Complementary=0
            market_segment_Corporate=0
            market_segment_Direct=0
            market_segment_Groups=0
            market_segment_Offline=0
            market_segment_Online =0
            market_segment_Undefined=1
            market_segment_Aviation=0

        else:
            market_segment_Complementary=0
            market_segment_Corporate=0
            market_segment_Direct=0
            market_segment_Groups=0
            market_segment_Offline=0
            market_segment_Online =0
            market_segment_Undefined=0
            market_segment_Aviation=1    

        distribution_channel_Direct=request.form['distribution_channel_Direct']
        if(distribution_channel_Direct=='distribution_channel_Direct'):
            distribution_channel_Direct=1
            distribution_channel_GDS=0
            distribution_channel_TA=0
            distribution_channel_Undefined=0
            distribution_channel_Corporate=0

        elif(distribution_channel_Direct=='distribution_channel_GDS'):
            distribution_channel_Direct=0
            distribution_channel_GDS=1
            distribution_channel_TA=0
            distribution_channel_Undefined=0
            distribution_channel_Corporate=0    

        elif(distribution_channel_Direct=='distribution_channel_TA'):
            distribution_channel_Direct=0
            distribution_channel_GDS=0
            distribution_channel_TA=1
            distribution_channel_Undefined=0
            distribution_channel_Corporate=0

        elif(distribution_channel_Direct=='distribution_channel_Undefined'):
            distribution_channel_Direct=0
            distribution_channel_GDS=0
            distribution_channel_TA=0
            distribution_channel_Undefined=1
            distribution_channel_Corporate=0    

        else:
            distribution_channel_Direct=0
            distribution_channel_GDS=0
            distribution_channel_TA=0
            distribution_channel_Undefined=0
            distribution_channel_Corporate=1

        reserved_room_type_B=request.form['reserved_room_type_B']
        if(reserved_room_type_B=='reserved_room_type_B'):
            reserved_room_type_B=1 
            reserved_room_type_A=0
            reserved_room_type_D=0
            reserved_room_type_F=0
            reserved_room_type_G=0
            reserved_room_type_E=0
            reserved_room_type_C=0
            reserved_room_type_H=0
            reserved_room_type_P=0
            reserved_room_type_L=0

        elif(reserved_room_type_B=='reserved_room_type_A'):           
            reserved_room_type_B=0 
            reserved_room_type_A=1
            reserved_room_type_D=0
            reserved_room_type_F=0
            reserved_room_type_G=0
            reserved_room_type_E=0
            reserved_room_type_C=0
            reserved_room_type_H=0
            reserved_room_type_P=0
            reserved_room_type_L=0

        elif(reserved_room_type_B=='reserved_room_type_D'):           
            reserved_room_type_B=0 
            reserved_room_type_A=0
            reserved_room_type_D=1
            reserved_room_type_F=0
            reserved_room_type_G=0
            reserved_room_type_E=0
            reserved_room_type_C=0
            reserved_room_type_H=0
            reserved_room_type_P=0
            reserved_room_type_L=0

        elif(reserved_room_type_B=='reserved_room_type_F'):           
            reserved_room_type_B=0 
            reserved_room_type_A=0
            reserved_room_type_D=0
            reserved_room_type_F=1
            reserved_room_type_G=0
            reserved_room_type_E=0
            reserved_room_type_C=0
            reserved_room_type_H=0
            reserved_room_type_P=0
            reserved_room_type_L=0        

        elif(reserved_room_type_B=='reserved_room_type_G'):           
            reserved_room_type_B=0 
            reserved_room_type_A=0
            reserved_room_type_D=0
            reserved_room_type_F=0
            reserved_room_type_G=1
            reserved_room_type_E=0
            reserved_room_type_C=0
            reserved_room_type_H=0
            reserved_room_type_P=0
            reserved_room_type_L=0

        elif(reserved_room_type_B=='reserved_room_type_E'):           
            reserved_room_type_B=0 
            reserved_room_type_A=0
            reserved_room_type_D=0
            reserved_room_type_F=0
            reserved_room_type_G=0
            reserved_room_type_E=1
            reserved_room_type_C=0
            reserved_room_type_H=0
            reserved_room_type_P=0
            reserved_room_type_L=0 

        elif(reserved_room_type_B=='reserved_room_type_C'):           
            reserved_room_type_B=0 
            reserved_room_type_A=0
            reserved_room_type_D=0
            reserved_room_type_F=0
            reserved_room_type_G=0
            reserved_room_type_E=0
            reserved_room_type_C=1
            reserved_room_type_H=0
            reserved_room_type_P=0
            reserved_room_type_L=0       

        elif(reserved_room_type_B=='reserved_room_type_H'):           
            reserved_room_type_B=0 
            reserved_room_type_A=0
            reserved_room_type_D=0
            reserved_room_type_F=0
            reserved_room_type_G=0
            reserved_room_type_E=0
            reserved_room_type_C=0
            reserved_room_type_H=1
            reserved_room_type_P=0
            reserved_room_type_L=0 

        elif(reserved_room_type_B=='reserved_room_type_P'):           
            reserved_room_type_B=0 
            reserved_room_type_A=0
            reserved_room_type_D=0
            reserved_room_type_F=0
            reserved_room_type_G=0
            reserved_room_type_E=0
            reserved_room_type_C=0
            reserved_room_type_H=0
            reserved_room_type_P=1
            reserved_room_type_L=0 

        else:           
            reserved_room_type_B=0 
            reserved_room_type_A=0
            reserved_room_type_D=0
            reserved_room_type_F=0
            reserved_room_type_G=0
            reserved_room_type_E=0
            reserved_room_type_C=0
            reserved_room_type_H=0
            reserved_room_type_P=0
            reserved_room_type_L=1              

        assigned_room_type_B=request.form['assigned_room_type_B']
        if(assigned_room_type_B=='assigned_room_type_B'):
            assigned_room_type_B=1 
            assigned_room_type_A=0
            assigned_room_type_D=0
            assigned_room_type_F=0
            assigned_room_type_G=0
            assigned_room_type_E=0
            assigned_room_type_C=0
            assigned_room_type_H=0
            assigned_room_type_P=0
            assigned_room_type_L=0
            assigned_room_type_K=0
            assigned_room_type_I=0

        elif(assigned_room_type_B=='assigned_room_type_A'):           
            assigned_room_type_B=0 
            assigned_room_type_A=1
            assigned_room_type_D=0
            assigned_room_type_F=0
            assigned_room_type_G=0
            assigned_room_type_E=0
            assigned_room_type_C=0
            assigned_room_type_H=0
            assigned_room_type_P=0
            assigned_room_type_L=0
            assigned_room_type_K=0
            assigned_room_type_I=0

        elif(assigned_room_type_B=='assigned_room_type_D'):           
            assigned_room_type_B=0 
            assigned_room_type_A=0
            assigned_room_type_D=1
            assigned_room_type_F=0
            assigned_room_type_G=0
            assigned_room_type_E=0
            assigned_room_type_C=0
            assigned_room_type_H=0
            assigned_room_type_P=0
            assigned_room_type_L=0
            assigned_room_type_K=0
            assigned_room_type_I=0

        elif(assigned_room_type_B=='assigned_room_type_F'):           
            assigned_room_type_B=0 
            assigned_room_type_A=0
            assigned_room_type_D=0
            assigned_room_type_F=1
            assigned_room_type_G=0
            assigned_room_type_E=0
            assigned_room_type_C=0
            assigned_room_type_H=0
            assigned_room_type_P=0
            assigned_room_type_L=0
            assigned_room_type_K=0
            assigned_room_type_I=0        

        elif(assigned_room_type_B=='assigned_room_type_G'):           
            assigned_room_type_B=0 
            assigned_room_type_A=0
            assigned_room_type_D=0
            assigned_room_type_F=0
            assigned_room_type_G=1
            assigned_room_type_E=0
            assigned_room_type_C=0
            assigned_room_type_H=0
            assigned_room_type_P=0
            assigned_room_type_L=0
            assigned_room_type_K=0
            assigned_room_type_I=0

        elif(assigned_room_type_B=='assigned_room_type_E'):           
            assigned_room_type_B=0 
            assigned_room_type_A=0
            assigned_room_type_D=0
            assigned_room_type_F=0
            assigned_room_type_G=0
            assigned_room_type_E=1
            assigned_room_type_C=0
            assigned_room_type_H=0
            assigned_room_type_P=0
            assigned_room_type_L=0 
            assigned_room_type_K=0
            assigned_room_type_I=0

        elif(assigned_room_type_B=='assigned_room_type_C'):           
            assigned_room_type_B=0 
            assigned_room_type_A=0
            assigned_room_type_D=0
            assigned_room_type_F=0
            assigned_room_type_G=0
            assigned_room_type_E=0
            assigned_room_type_C=1
            assigned_room_type_H=0
            assigned_room_type_P=0
            assigned_room_type_L=0
            assigned_room_type_K=0
            assigned_room_type_I=0       

        elif(assigned_room_type_B=='assigned_room_type_H'):           
            assigned_room_type_B=0 
            assigned_room_type_A=0
            assigned_room_type_D=0
            assigned_room_type_F=0
            assigned_room_type_G=0
            assigned_room_type_E=0
            assigned_room_type_C=0
            assigned_room_type_H=1
            assigned_room_type_P=0
            assigned_room_type_L=0
            assigned_room_type_K=0
            assigned_room_type_I=0 

        elif(assigned_room_type_B=='assigned_room_type_P'):           
            assigned_room_type_B=0 
            assigned_room_type_A=0
            assigned_room_type_D=0
            assigned_room_type_F=0
            assigned_room_type_G=0
            assigned_room_type_E=0
            assigned_room_type_C=0
            assigned_room_type_H=0
            assigned_room_type_P=1
            assigned_room_type_L=0
            assigned_room_type_K=0
            assigned_room_type_I=0 

        elif(assigned_room_type_B=='assigned_room_type_L'):           
            assigned_room_type_B=0 
            assigned_room_type_A=0
            assigned_room_type_D=0
            assigned_room_type_F=0
            assigned_room_type_G=0
            assigned_room_type_E=0
            assigned_room_type_C=0
            assigned_room_type_H=0
            assigned_room_type_P=0
            assigned_room_type_L=1
            assigned_room_type_K=0
            assigned_room_type_I=0 

        elif(assigned_room_type_B=='assigned_room_type_K'):           
            assigned_room_type_B=0 
            assigned_room_type_A=0
            assigned_room_type_D=0
            assigned_room_type_F=0
            assigned_room_type_G=0
            assigned_room_type_E=0
            assigned_room_type_C=0
            assigned_room_type_H=0
            assigned_room_type_P=0
            assigned_room_type_L=0
            assigned_room_type_K=1
            assigned_room_type_I=0

        else:           
            assigned_room_type_B=0 
            assigned_room_type_A=0
            assigned_room_type_D=0
            assigned_room_type_F=0
            assigned_room_type_G=0
            assigned_room_type_E=0
            assigned_room_type_C=0
            assigned_room_type_H=0
            assigned_room_type_P=0
            assigned_room_type_L=0
            assigned_room_type_K=0
            assigned_room_type_I=1           
                
        deposit_type_Non=request.form['deposit_type_Non']
        if(deposit_type_Non=='deposit_type_Non'):
            deposit_type_Non=1
            deposit_type_Refundable=0
            deposit_type_No_deposit=0

        elif(deposit_type_Non=='deposit_type_Refundable'):
            deposit_type_Non=0
            deposit_type_Refundable=1
            deposit_type_No_deposit=0    

        else:
            deposit_type_Non=0
            deposit_type_Refundable=0
            deposit_type_No_deposit=1          

        customer_type_Group=request.form['customer_type_Group']
        if(customer_type_Group=='customer_type_Group'):
            customer_type_Group=1
            customer_type_Transient=0
            customer_type_Transient_party=0
            customer_type_Contract=0

        elif(customer_type_Group=='customer_type_Transient'):
            customer_type_Group=0
            customer_type_Transient=1
            customer_type_Transient_party=0
            customer_type_Contract=0

        elif(customer_type_Group=='customer_type_Transient_party'):
            customer_type_Group=0
            customer_type_Transient=0
            customer_type_Transient_party=1
            customer_type_Contract=0    

        else:
            customer_type_Group=0
            customer_type_Transient=0
            customer_type_Transient_party=0
            customer_type_Contract=1   

        prediction=model.predict([[lead_time, arrival_date_year, arrival_date_month, arrival_date_day_of_month, stays_in_weekend_nights, stays_in_week_nights, adults, children,babies,is_repeated_guest,previous_cancellations,previous_bookings_not_canceled,booking_changes, days_in_waiting_list,adr,  required_car_parking_spaces,total_of_special_requests,  hotel_Resort,meal_FB, meal_HB, meal_SC, meal_Undefined,market_segment_Complementary,market_segment_Corporate ,market_segment_Direct,market_segment_Groups, market_segment_Offline, market_segment_Online, market_segment_Undefined, distribution_channel_Direct, distribution_channel_GDS, distribution_channel_TA, distribution_channel_Undefined, reserved_room_type_B, reserved_room_type_C, reserved_room_type_D, reserved_room_type_E, reserved_room_type_F, reserved_room_type_G,reserved_room_type_H, reserved_room_type_L, reserved_room_type_P, assigned_room_type_B, assigned_room_type_C, assigned_room_type_D, assigned_room_type_E, assigned_room_type_F, assigned_room_type_G, assigned_room_type_H, assigned_room_type_I, assigned_room_type_K, assigned_room_type_L, assigned_room_type_P, deposit_type_Non, deposit_type_Refundable, customer_type_Group, customer_type_Transient,customer_type_Transient_party ]])    
        output=round(prediction[0],2) 

        if output<0:
            return render_template('index.html', prediction_texts="Sorry you cannot book any Room" )
        else:
            return render_template('index.html', prediction_text="Your booking Result is {}".format(output))
    else:
        return render_template('index.html')   


#if __name__=="__main__":
#    app.run(debug=True)        
            
#to run this on surver
if __name__=="__main__":
    app.run(host='0.0.0.0',port=8080)             
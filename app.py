from flask import Flask,render_template,request
import pickle
import pandas as pd



app = Flask(__name__, template_folder='templates')

@app.route('/', methods=["GET","POST"])
def main():
    if request.method == 'GET':
        return(render_template('main.html'))

    if request.method == "POST":
        abdominal_pain = request.form.getlist("  abdominal_pain ")
        if request.form.getlist("  abdominal_pain ") == []:      abdominal_pain = ["0"]
        abnormal_menstruation = request.form.getlist("  abnormal_menstruation ")
        if request.form.getlist("  abnormal_menstruation ") == []:      abnormal_menstruation = ["0"]
        acidity = request.form.getlist("  acidity ")
        if request.form.getlist("  acidity ") == []:      acidity = ["0"]
        acute_liver_failure = request.form.getlist("  acute_liver_failure ")
        if request.form.getlist("  acute_liver_failure ") == []:      acute_liver_failure = ["0"]
        altered_sensorium = request.form.getlist("  altered_sensorium ")
        if request.form.getlist("  altered_sensorium ") == []:      altered_sensorium = ["0"]
        anxiety = request.form.getlist("  anxiety ")
        if request.form.getlist("  anxiety ") == []:      anxiety = ["0"]
        back_pain = request.form.getlist("  back_pain ")
        if request.form.getlist("  back_pain ") == []:      back_pain = ["0"]
        belly_pain = request.form.getlist("  belly_pain ")
        if request.form.getlist("  belly_pain ") == []:      belly_pain = ["0"]
        blackheads = request.form.getlist("  blackheads ")
        if request.form.getlist("  blackheads ") == []:      blackheads = ["0"]
        bladder_discomfort = request.form.getlist("  bladder_discomfort ")
        if request.form.getlist("  bladder_discomfort ") == []:      bladder_discomfort = ["0"]
        blister = request.form.getlist("  blister ")
        if request.form.getlist("  blister ") == []:      blister = ["0"]
        blood_in_sputum = request.form.getlist("  blood_in_sputum ")
        if request.form.getlist("  blood_in_sputum ") == []:      blood_in_sputum = ["0"]
        bloody_stool = request.form.getlist("  bloody_stool ")
        if request.form.getlist("  bloody_stool ") == []:      bloody_stool = ["0"]
        blurred_and_distorted_vision = request.form.getlist("  blurred_and_distorted_vision ")
        if request.form.getlist("  blurred_and_distorted_vision ") == []:      blurred_and_distorted_vision = ["0"]
        breathlessness = request.form.getlist("  breathlessness ")
        if request.form.getlist("  breathlessness ") == []:      breathlessness = ["0"]
        brittle_nails = request.form.getlist("  brittle_nails ")
        if request.form.getlist("  brittle_nails ") == []:      brittle_nails = ["0"]
        bruising = request.form.getlist("  bruising ")
        if request.form.getlist("  bruising ") == []:      bruising = ["0"]
        burning_micturition = request.form.getlist("  burning_micturition ")
        if request.form.getlist("  burning_micturition ") == []:      burning_micturition = ["0"]
        chest_pain = request.form.getlist("  chest_pain ")
        if request.form.getlist("  chest_pain ") == []:      chest_pain = ["0"]
        chills = request.form.getlist("  chills ")
        if request.form.getlist("  chills ") == []:      chills = ["0"]
        cold_hands_and_feets = request.form.getlist("  cold_hands_and_feets ")
        if request.form.getlist("  cold_hands_and_feets ") == []:      cold_hands_and_feets = ["0"]
        coma = request.form.getlist("  coma ")
        if request.form.getlist("  coma ") == []:      coma = ["0"]
        congestion = request.form.getlist("  congestion ")
        if request.form.getlist("  congestion ") == []:      congestion = ["0"]
        constipation = request.form.getlist("  constipation ")
        if request.form.getlist("  constipation ") == []:      constipation = ["0"]
        continuous_feel_of_urine = request.form.getlist("  continuous_feel_of_urine ")
        if request.form.getlist("  continuous_feel_of_urine ") == []:      continuous_feel_of_urine = ["0"]
        continuous_sneezing = request.form.getlist("  continuous_sneezing ")
        if request.form.getlist("  continuous_sneezing ") == []:      continuous_sneezing = ["0"]
        cough = request.form.getlist("  cough ")
        if request.form.getlist("  cough ") == []:      cough = ["0"]
        cramps = request.form.getlist("  cramps ")
        if request.form.getlist("  cramps ") == []:      cramps = ["0"]
        dark_urine = request.form.getlist("  dark_urine ")
        if request.form.getlist("  dark_urine ") == []:      dark_urine = ["0"]
        dehydration = request.form.getlist("  dehydration ")
        if request.form.getlist("  dehydration ") == []:      dehydration = ["0"]
        depression = request.form.getlist("  depression ")
        if request.form.getlist("  depression ") == []:      depression = ["0"]
        diarrhoea = request.form.getlist("  diarrhoea ")
        if request.form.getlist("  diarrhoea ") == []:      diarrhoea = ["0"]
        dischromic_patches = request.form.getlist("  dischromic _patches ")
        if request.form.getlist("  dischromic _patches ") == []:      dischromic_patches = ["0"]
        distention_of_abdomen = request.form.getlist("  distention_of_abdomen ")
        if request.form.getlist("  distention_of_abdomen ") == []:      distention_of_abdomen = ["0"]
        dizziness = request.form.getlist("  dizziness ")
        if request.form.getlist("  dizziness ") == []:      dizziness = ["0"]
        drying_and_tingling_lips = request.form.getlist("  drying_and_tingling_lips ")
        if request.form.getlist("  drying_and_tingling_lips ") == []:      drying_and_tingling_lips = ["0"]

        Columns=[' abdominal_pain', ' abnormal_menstruation', ' acidity', ' acute_liver_failure', ' altered_sensorium', ' anxiety', 
        ' back_pain', ' belly_pain', ' blackheads', ' bladder_discomfort', ' blister', ' blood_in_sputum', ' bloody_stool', ' blurred_and_distorted_vision', ' breathlessness', 
        ' brittle_nails', ' bruising', ' burning_micturition', ' chest_pain', ' chills', ' cold_hands_and_feets', ' coma', ' congestion', ' constipation', ' continuous_feel_of_urine', 
        ' continuous_sneezing', ' cough', ' cramps', ' dark_urine', ' dehydration', ' depression', ' diarrhoea', ' dischromic _patches', ' distention_of_abdomen', ' dizziness', 
        ' drying_and_tingling_lips', ' enlarged_thyroid', ' excessive_hunger', ' extra_marital_contacts', ' family_history', ' fast_heart_rate', ' fatigue', ' fluid_overload', 
        ' foul_smell_of urine', ' headache', ' high_fever', ' hip_joint_pain', ' history_of_alcohol_consumption', ' increased_appetite', ' indigestion', ' inflammatory_nails', 
        ' internal_itching', ' irregular_sugar_level', ' irritability', ' irritation_in_anus', ' itching', ' joint_pain', ' knee_pain', ' lack_of_concentration', ' lethargy', 
        ' lethargy dizziness', ' loss_of_appetite', ' loss_of_balance', ' loss_of_smell', ' malaise', ' mild_fever', ' mood_swings', ' movement_stiffness', ' mucoid_sputum', 
        ' muscle_pain', ' muscle_pain receiving_blood_transfusion', ' muscle_wasting', ' muscle_weakness', ' nausea', ' neck_pain', ' nodal_skin_eruptions', ' obesity', 
        ' pain_behind_the_eyes', ' pain_during_bowel_movements', ' pain_in_anal_region', ' painful_walking', ' palpitations', ' passage_of_gases', ' patches_in_throat', 
        ' phlegm', ' polyuria', ' prominent_veins_on_calf', ' puffy_face_and_eyes', ' pus_filled_pimples', ' receiving_blood_transfusion', ' receiving_unsterile_injections', 
        ' red_sore_around_nose', ' red_spots_over_body', ' redness_of_eyes', ' restlessness', ' runny_nose', ' rusty_sputum', ' scurring', ' shivering', ' silver_like_dusting', 
        ' sinus_pressure', ' skin_peeling', ' skin_rash', ' slurred_speech', ' small_dents_in_nails', ' spinning_movements', ' spotting_ urination', ' spotting_urination', 
        ' stiff_neck', ' stomach_bleeding', ' stomach_pain', ' sunken_eyes', ' sweating', ' swelled_lymph_nodes', ' swelling_joints', ' swelling_of_stomach', ' swollen_blood_vessels', 
        ' swollen_extremeties', ' swollen_legs', ' throat_irritation', ' toxic_look_(typhos)', ' ulcers_on_tongue', ' unsteadiness', ' visual_disturbances', ' vomiting', ' watering_from_eyes', 
        ' weakness_in_limbs', ' weakness_of_one_body_side', ' weight_gain', ' weight_loss', ' yellow_crust_ooze', ' yellow_urine', ' yellowing_of_eyes', ' yellowish_skin']

        data = [abdominal_pain[0], int(abnormal_menstruation[0]), int(acidity[0]), int(acute_liver_failure[0]), int(altered_sensorium[0]), int(anxiety[0]),
         int(back_pain[0]), int(belly_pain[0]), int(blackheads[0]), int(bladder_discomfort[0]), int(blister[0]), int(blood_in_sputum[0]), int(bloody_stool[0]), int(blurred_and_distorted_vision[0]), 
         int(breathlessness[0]), int(brittle_nails[0]), int(bruising[0]), int(burning_micturition[0]), int(chest_pain[0]), int(chills[0]), int(cold_hands_and_feets[0]), int(coma[0]), int(congestion[0]), 
         int(constipation[0]), int(continuous_feel_of_urine[0]), int(continuous_sneezing[0]), int(cough[0]), int(cramps[0]), int(dark_urine[0]), int(dehydration[0]), int(depression[0]), int(diarrhoea[0]), 
         int(dischromic_patches[0]), int(distention_of_abdomen[0]), int(dizziness[0]), int(drying_and_tingling_lips[0]), 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
     
        input_variables = pd.DataFrame([data],columns = Columns)
        model = pickle.load(open('model/model1.pkl','rb'))
        prediction = model.predict(input_variables)
        

        return render_template('main.html', pred=prediction[0])
        app.run(debug=True)

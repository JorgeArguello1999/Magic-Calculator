/* List of type's activities */
pub fn list_activitys(activity:i32 ) -> f64 {

    if activity == 0 {
        println!("
        1.- Sedentary
        2.- 1-3 days of activity
        3.- 3-5 days of activity
        4.- 6-7 days of activity
        5.- Athletic extreme
        ");
        return 0.0;
    }

    let days_activity = match activity {
        1 => 1.2,
        2 => 1.375,
        3 => 1.55,
        4 => 1.725,
        5 => 1.9,
        _ => {
            println!("Error in your input");
            0.0
        }
    };

    return days_activity;
    
}

/* Function to get caloric expenditure */
pub fn calculate_caloric_expenditure(genere:String, weight_kg:f64, height_cm:f64, years_old:f64, days_activity:i32) -> f64{
    let activity:f64 = list_activitys(days_activity);
    let result:f64 = (10.0 * weight_kg) + (6.25 * height_cm) - (5.0 * years_old) * activity;

    let genere:bool = get_genere(genere);
    if genere{ 
        return result + 5.0;
    }

    return result - 161.0;

}

/* Transform the genere to bool */
pub fn get_genere(genere:String) -> bool {
    let mut genere_output :bool = false;
    if genere.to_lowercase() == "male"{
        genere_output = true;
    }
    return genere_output;
}
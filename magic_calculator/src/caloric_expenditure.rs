/* Function to get caloric expenditure */
pub fn calculate_caloric_expenditure(genere:bool, weight_kg:f64, height_cm:f64, years_old:f64) -> f64{
    let result = (10.0 * weight_kg) + (6.25 * height_cm) - (5.0 * years_old);

    /*
    genere -> True -> Male
    genere -> False -> Female
    */
    if genere{ 
        return result + 5.0;
    }

    return result - 161.0;

}
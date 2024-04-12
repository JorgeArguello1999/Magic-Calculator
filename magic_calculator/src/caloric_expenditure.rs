/* Function to get caloric expenditure */

pub fn calculate_caloric_expenditure(genere:String, weight_kg:f64, height_cm:f64, years_old:f64) -> f64{
    let result = (10.0 * weight_kg) + (6.25 * height_cm) - (5.0 * years_old);

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
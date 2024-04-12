mod weight_another_planets;
mod caloric_expenditure;
mod funcs;

// Function to get your weight 
fn calculate_weight_another_planets() -> f64 {
    // Print gravity of planets 
    weight_another_planets::list_planets_gravity(None); 

    // Prompt user to enter the planet
    println!("Enter the planet that you want to calculate: ");
    let planet: String = funcs::get_str_value();

    // Prompt user to enter their weight
    println!("Enter your weight in Kg: ");
    let weight: f64 = funcs::get_float_value();

    let calculate: f64 = weight_another_planets::calculate_weight(weight, &planet);
    println!("Your weight is: {}", calculate);
    return calculate;
}

// Function to calculate your caloric expenditure
fn calculate_caloric_expenditure() -> f64{
    // Genere input
    println!("Please enter your genere, Male or Female: ");
    let genere_input:String = funcs::get_str_value();

    let mut genere_output :bool = false;
    if genere_input.to_lowercase() == "male"{
        genere_output = true;
    }

    // Weight input
    println!("Enter your weight (Kg): ");
    let weight_input:f64 = funcs::get_float_value();

    // Height input
    println!("Enter your height (cm): ");
    let height_input:f64 = funcs::get_float_value();

    // Years old input
    println!("Enter your age (Years): ");
    let years_input:f64 = funcs::get_float_value();


    let result:f64 = caloric_expenditure::calculate_caloric_expenditure(
        genere_output, weight_input, height_input,years_input 
    );

    println!("Your caloric expenditure is {}", result);

    return result;
}

fn main() {
    println!("Magic Calculator!");

    print!("
    1.- Calculate Caloric Expenditure.
    2.- Calculate Weight on Another Planets.
    3.- Calculate Porcentage.
    4.- Convertions of temperatures.

    Enter the option: 
    ");

    let input = funcs::get_int_value();

    let result = match input {
        1 => calculate_caloric_expenditure(),
        2 => calculate_weight_another_planets(),
        _ => {
            println!("Error with your input");
            0.0 // Return a default value of type f64
        },
    };

    println!("Your choice: {}", result);

}
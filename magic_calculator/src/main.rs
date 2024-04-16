// Functions basic
mod funcs;

// Module functions
mod functions {
    pub mod caloric_expenditure;
    pub mod weight_another_planets;
    pub mod conversion_temperatures;
}

// Make use
use functions::caloric_expenditure;
use functions::weight_another_planets;
use functions::conversion_temperatures;

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
        genere_input, weight_input, height_input,years_input 
    );

    println!("Your caloric expenditure is {}", result);

    return result;
}

// Function to transform the temperatures
fn transform_temperatures() -> f64 {
    println!("
    1.- Celsius to Kelvin (C -> K). 
    2.- Kelvin to Celsius (K -> C).
    3.- Celsius to Fahrenheit (C -> F).
    4.- Fahrenheit to Celsius (F -> C).
    5.- Kelvin to Fahrenheit (K -> F).
    6.- Fahrenheit to Kelvin (F -> K).

    Your input: 
    ");

    let input:i32 = funcs::get_int_value();

    println!("Enter the value to transform: ");
    let value:f64 = funcs::get_float_value();

    let result = match input {
        1 => conversion_temperatures::celsius_kelvin(value),
        2 => conversion_temperatures::kelvin_celsius(value),
        3 => conversion_temperatures::celsius_fahrenheit(value),
        4 => conversion_temperatures::fahrenheit_celsius(value),
        5 => conversion_temperatures::kelvin_fahrenheit(value),
        6 => conversion_temperatures::fahrenheit_kelvin(value),
        _ => {
            println!("Invalid input");
            0.0 // Return a default value
        }
    };

    println!("The temperature convertion is: {result}");

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
        4 => transform_temperatures(),
        _ => {
            println!("Error with your input");
            0.0 // Return a default value of type f64
        },
    };

    println!("Your result: {}", result);

}
use crate::functions::porcentage::porcentage;

// Basic Functions
use super::funcs; 
// Converts functions
use super::functions::{
    caloric_expenditure, 
    weight_another_planets, 
    conversion_temperatures,
};

// Function to get your weight 
pub fn calculate_weight_another_planets() -> f64 {
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
    calculate
}

// Function to calculate your caloric expenditure
pub fn calculate_caloric_expenditure() -> f64{
    // Gender input
    println!("Please enter your gender, Male or Female: ");
    let gender_input:String = funcs::get_str_value();

    // Weight input
    println!("Enter your weight (Kg): ");
    let weight_input:f64 = funcs::get_float_value();

    // Height input
    println!("Enter your height (cm): ");
    let height_input:f64 = funcs::get_float_value();

    // Age input
    println!("Enter your age (Years): ");
    let age_input:f64 = funcs::get_float_value();

    let result:f64 = caloric_expenditure::calculate_caloric_expenditure(
        gender_input, weight_input, height_input, age_input 
    );

    println!("Your caloric expenditure is {}", result);
    result
}

// Function to transform the temperatures
pub fn transform_temperatures() -> f64 {
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

    println!("The temperature convertion is: {}", result);
    result
}


pub fn calculate_porcentage() -> f64 {
    println!("Enter the total value: ");
    let total_value:f64 = funcs::get_float_value();

    println!("Enter the value for know the porcentage: ");
    let value:f64 = funcs::get_float_value();

    let result:f64 = porcentage(value, total_value);
    println!("The value ({value}) from total value ({total_value}) is: {result}");

    return result;
}
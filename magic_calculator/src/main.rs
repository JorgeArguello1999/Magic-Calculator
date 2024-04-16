mod funcs;
mod cli;

// Module functions
mod functions {
    pub mod caloric_expenditure;
    pub mod weight_another_planets;
    pub mod conversion_temperatures;
    pub mod porcentage;
}

use funcs::get_int_value;

use cli::{
    calculate_caloric_expenditure, 
    calculate_weight_another_planets, 
    transform_temperatures,
    calculate_porcentage
};

fn main() {
    println!("Magic Calculator!");

    print!("
    1.- Calculate Caloric Expenditure.
    2.- Calculate Weight on Another Planets.
    3.- Calculate Porcentage.
    4.- Convertions of temperatures.

    Enter the option: 
    ");

    let input = get_int_value();

    let result = match input {
        1 => calculate_caloric_expenditure(),
        2 => calculate_weight_another_planets(),
        3 => calculate_porcentage(),
        4 => transform_temperatures(),
        _ => {
            println!("Error with your input");
            0.0 // Return a default value of type f64
        },
    };
    print!("{}", result);

}
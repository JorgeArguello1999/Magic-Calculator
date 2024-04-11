mod weight_another_planets;
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

fn main() {
    println!("Magic Calculator!");

    // Your weight on another planet
    calculate_weight_another_planets();
}
mod weight_another_planets;

fn main() {
    println!("Magic Calculator!");

    // Print gravity of planets 
    weight_another_planets::list_planets_gravity(None); 

    // Calculate your weight
    let calculate:f64 = weight_another_planets::calculate_weight(32.0, "Marte");
    println!("Your weight is: {calculate}");

}
use std::collections::HashMap;

/*
Show the differents planets/gravity
*/
pub fn list_planets_gravity(planet: Option<&str>) -> Option<f64> {
    // Map with planets gravity
    let planets: HashMap<&str, f64> = [
        ("Marte", 3.71),
        ("Mercurio", 3.70),
        ("Urano", 8.69),
        ("Neptuno", 11.00),
        ("Saturno", 8.96),
        ("Jupiter", 23.12),
        ("Tierra", 9.81),
    ]
    .iter()
    .cloned()
    .collect();

    if let Some(planet) = planet {
        if let Some(gravity) = planets.get(planet) {
            println!("Planet: {} Gravity: {}", planet, gravity);
            return Some(*gravity);

        } else {
            println!("Planet {} don't exists.", planet);
            return None;

        }
    } else {
        println!("Show the all gravity for planets:");
        for (planet, gravity) in &planets {
            println!("{}: {}", planet, gravity);
        }
        return None;
    }
}

/*
Make the calculate
*/
pub fn calculate_weight(weight:f64, planet:&str) -> i32 {
    println!("{}, {}", weight, planet);
    return 1;
}

mod weight_another_planets;

fn main() {
    println!("Hello, world!");
    
    let calculate = weight_another_planets::calculate_weight(1.0, "h");
    print!("{calculate}");

    weight_another_planets::list_planets_gravity(Some("Tierra")); // Ejemplo: Obtener la gravedad de un planeta específico
    weight_another_planets::list_planets_gravity(None); // Ejemplo: Mostrar todos los valores de gravedad
}
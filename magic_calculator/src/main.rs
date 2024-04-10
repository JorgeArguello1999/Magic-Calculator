mod weight_another_planets;

fn main() {
    println!("Hello, world!");
    
    let calculate = weight_another_planets::calculate(1.0, 2);
    print!("{calculate}");
}
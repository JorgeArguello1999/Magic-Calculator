use std::io;

pub fn get_float_value() -> f64 {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Error al leer la entrada");
    let valor: f64 = input.trim().parse().expect("No se pudo convertir a f64");
    return valor;
}

pub fn get_str_value() -> String {
    let mut input:String = String::new();
    io::stdin().read_line(&mut input).expect("Error al leer la entrada");
    return input.trim().to_string()
}


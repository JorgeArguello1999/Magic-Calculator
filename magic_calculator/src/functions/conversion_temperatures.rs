/**
 * Functions to convert the differentents temperatures
 */

pub fn celsius_kelvin(celsius:f64) -> f64 {
    return celsius + 273.15;
}

pub fn kelvin_celsius(kelvin:f64) -> f64 {
    return kelvin - 273.15;
}

pub fn celsius_fahrenheit(celsius:f64) -> f64 {
    return celsius * 1.8 + 32.0;
}

pub fn fahrenheit_celsius(fahrenheit:f64) -> f64 {
    return (fahrenheit - 32.0)/1.8;
}

pub fn kelvin_fahrenheit(kelvin:f64) -> f64 {
    return (kelvin * 1.8) - 459.67;
}

pub fn fahrenheit_kelvin(fahrenheit:f64) -> f64 {
    return (fahrenheit+459.67)/1.8; 
}

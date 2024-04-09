# Magic Calculator 

> This program is a small application that has as its purpose small operations of conversions of: Temperature, Weight and other interesting things

![icon for app](Banner.jpeg)

## Features 
This program have this functions:
- [Temperature](#conversion-table-for-temperatures)
- [Porcentage](#formula-for-percentage-conversion)
- [Calories](#formula-to-calculate-caloric-expenditure)
- [Weight on another planet](#formula-to-calculate-your-weight-on-another-planet)

## Conversion table for temperatures 

1. Celsius to Kelvin (C -> K):
   \[ K = C + 273.15 \]

2. Kelvin to Celsius (K -> C):
   \[ C = K - 273.15 \]

3. Celsius to Fahrenheit (C -> F):
   \[ F = (C x 1.8) + 32 \]

4. Fahrenheit to Celsius (F -> C):
   \[ C = (F - 32) / 1.8 \]

5. Kelvin to Fahrenheit (K -> F):
   \[ F = (K x 1.8) - 459.67 \]

6. Fahrenheit to Kelvin (F -> K):
   \[ K = (F + 459.67) / 1.8 \]


## Formula for percentage conversion
working..

## Formula to calculate caloric expenditure

> This function allows us to calculate a person's caloric expenditure depending on their physical activity and other indices, such as the person's weight and height.

### For man
```math
Result = (10 * weight-on-Kg) + (6.25 * height-on-cm) - (5 * years-old) + 5
```

### For women
```math
Result = (10 * weight-on-Kg) + (6.25 * height-on-cm) - (5 * years-old) - 161 
```

Then, you multiply the result obtained by a physical activity factor according to the amount of exercise you do per week:
- Sedentary * 1.2
- 1-3 days of exercise * 1.375
- 3-5 days of exercise * 1.55
- 6-7 days of exercise * 1.725
- Athletes or extreme activity * 1.9 

## Formula to calculate your weight on another planet
The formula for calculate your wieight on another planet is this:

```math 
Weight-on-planet = (Weight-on-Earth * Planetary-Gravity) / Earth-Gravity
```
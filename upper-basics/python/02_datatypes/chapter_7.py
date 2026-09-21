#tuples are immputable
tuple_masala_spices= tuple()

print(f"Initial tuple: {tuple_masala_spices}")

masala_spices = ("cardamom", "cloves", "cinnamon")

(spice1, spice2, spice3) = masala_spices

print(f"Main masala spices: {spice1}, {spice2}, {spice3}")

ginger_ratio, cadramom_ratio = 2, 1
print(f"Ratio is G :{ginger_ratio} and C: {cadramom_ratio}")
ginger_ratio, cadramom_ratio = cadramom_ratio, ginger_ratio
print(f"Ratio is G :{ginger_ratio} and C: {cadramom_ratio}")

# membership testing

print(f"Is cinnamon in masala spices ? {'cinnamon' in masala_spices}")

print(f"is cloves in masala spiices {int('cloves' in masala_spices)}")

print(bool(12))
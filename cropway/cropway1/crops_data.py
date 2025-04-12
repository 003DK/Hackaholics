from cropway1.models import Crop

crop_data = [
    ("Wheat", "Alluvial Soil", "Moderate", "Rabi", "3-4 tons/acre"),
    ("Rice", "Clay", "High", "Kharif", "2-3 tons/acre"),
    ("Maize", "Loamy", "Moderate", "Kharif", "2.5-3.5 tons/acre"),
    ("Cotton", "Black Soil", "High", "Kharif", "1.5-2 tons/acre"),
    ("Millet", "Red Soil", "Low", "Kharif", "1-1.5 tons/acre"),
    ("Barley", "Sandy Loam", "Moderate", "Rabi", "2-2.5 tons/acre"),
    ("Sugarcane", "Loamy", "High", "Whole Year", "35-40 tons/acre"),
    ("Groundnut", "Red Soil", "Moderate", "Kharif", "1.2-1.5 tons/acre"),
    ("Soybean", "Black Soil", "Moderate", "Kharif", "2.2-2.8 tons/acre"),
    ("Lentil", "Alluvial Soil", "Low", "Rabi", "0.8-1.2 tons/acre"),
    ("Mustard", "Loamy", "Low", "Rabi", "1-1.5 tons/acre"),
    ("Chickpea", "Black Soil", "Low", "Rabi", "1-1.2 tons/acre"),
    ("Sorghum", "Red Soil", "Low", "Kharif", "1.5-2 tons/acre"),
    ("Peas", "Loamy", "Moderate", "Rabi", "1-1.4 tons/acre"),
    ("Turmeric", "Sandy Loam", "High", "Kharif", "5-6 tons/acre"),
    ("Garlic", "Loamy", "Moderate", "Rabi", "4-5 tons/acre"),
    ("Onion", "Alluvial Soil", "Moderate", "Rabi", "10-12 tons/acre"),
    ("Tomato", "Loamy", "High", "Summer", "15-20 tons/acre"),
    ("Cabbage", "Alluvial Soil", "High", "Winter", "20-25 tons/acre"),
    ("Carrot", "Sandy Loam", "Moderate", "Rabi", "12-15 tons/acre")
]

for name, soil, water, season, yield_amt in crop_data:
    Crop.objects.create(name=name, soil_type=soil, water_availability=water, season=season, expected_yield=yield_amt)

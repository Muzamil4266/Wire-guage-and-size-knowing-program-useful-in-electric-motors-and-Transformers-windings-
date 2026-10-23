import math

def display_instructions():
    print("=" * 70)
    print("       PENCIL METHOD WIRE GAUGE & WINDING CALCULATOR")
    print("=" * 70)
    print("""
🔴What each thing in  your input means so you know what to input 


🟢Enter turns on pen for new wire:

This is the number of turns of the new wire you are going to use in your coil. You should use 15 turns for every wire you measure on the pen. Wind the wire very closely together without leaving any gaps.

Example: 15 turns.



🟢Enter total length of turns in mm for new wire 

This is the total length of the turns you made using the new wire. In our case, we use 15 turns. After winding the wire closely together without leaving any gaps, measure the total length of those 15 turns using a scale in millimetres (mm).

Example: 20 mm.

🟢Enter turns on pen for old wire:


This is the number of turns of the old wire that is already wound in the coil you are going to replace. First, take a piece of the old wire and wind it around the pen. Use 15 turns, winding them very closely together without leaving any gaps.

Example: 15 turns.

🟢Enter total length of turns in mm for old wire:

This is the total length of the turns you made using the old wire. In our case, we use 15 turns. After winding the wire closely together without leaving any gaps, measure the total length of those 15 turns using a scale in millimetres (mm).

Example: 20 mm.

🟢 Enter total turns in the old coil:

This is the total number of turns in the old coil. This is not a measurement taken using a scale. Instead, you must determine how many turns the old coil had before replacing its wire.

First, open the coil and count the number of turns. The coil might have 50, 100, 200, 1,000 turns, or even more.

If the coil has a large number of turns, you can estimate the total by counting turns in smaller bundles instead of counting every single turn individually.



🔴 Calculation results understanding 




New wire diameter=diameter of new wire that we are gonna use or you just calculated 



New wire swg=swg of new wire wires are measured in swg we use a standard scale of swg values putted into python code that is fetched firstly from web then we hard coded into python without needing any connection to google 





New wire area=area of new wire



Old wire diameter=diameter of old wire

Old wire area=area of old wire


Required new turns=this is the most important thing this tells us that the new wire that we just calculated now we make how many turns of that wire into the coil so eveuthing is perfect even if you are using different swg wires this is the beauty of this whole math that it allows us to wind different wire sizes too suppose you have motor with factory winding of 20swg wire now you have 30swg wire so by this formula python code you should know exactly that how many turns you wind of your available wire but note that length and breadth etc of coil exactly needrd to be matched just like old coil this just tells you turns .
""")
    print("=" * 70 + "\n")

# Official Imperial Standard Wire Gauge (SWG) Table (Diameter in mm)[cite: 4, 5]
SWG_TABLE = [
    ("7/0", 12.7000), ("6/0", 11.7860), ("5/0", 10.9730), ("4/0", 10.1600),
    ("3/0", 9.4490), ("2/0", 8.8390), ("1/0", 8.2360),
    ("1", 7.6200), ("2", 7.0100), ("3", 6.4010), ("4", 5.8930), ("5", 5.3850),
    ("6", 4.8770), ("7", 4.4700), ("8", 4.0640), ("9", 3.6580), ("10", 3.2510),
    ("11", 2.9460), ("12", 2.6420), ("13", 2.3370), ("14", 2.0320),
    ("15", 1.8290), ("16", 1.6260), ("17", 1.4220), ("18", 1.2190),
    ("19", 1.0160), ("20", 0.9140), ("21", 0.8130), ("22", 0.7110),
    ("23", 0.6100), ("24", 0.5590), ("25", 0.5080), ("26", 0.4570), 
    ("27", 0.4170), ("28", 0.3760), ("29", 0.3450), ("30", 0.3150), 
    ("31", 0.2950), ("32", 0.2740), ("33", 0.2540), ("34", 0.2340), 
    ("35", 0.2130), ("36", 0.1930), ("37", 0.1730), ("38", 0.1520), 
    ("39", 0.1320), ("40", 0.1220), ("41", 0.1120), ("42", 0.1020), 
    ("43", 0.0910), ("44", 0.0810), ("45", 0.0710), ("46", 0.0610), 
    ("47", 0.0510), ("48", 0.0410), ("49", 0.0300), ("50", 0.0250)
]

def find_closest_swg(diameter_mm):
    """Finds the closest SWG standard size based on diameter."""
    closest_swg = SWG_TABLE[0][0]
    min_diff = float('inf')
    for swg, dia in SWG_TABLE:
        diff = abs(dia - diameter_mm)
        if diff < min_diff:
            min_diff = diff
            closest_swg = swg
    return closest_swg

def calculate_wire_properties(turns, length_mm):
    diameter = length_mm / turns
    radius = diameter / 2
    area = math.pi * (radius ** 2)
    return diameter, area

def main():
    display_instructions()
    
    print("--- 1. NEW WIRE MEASUREMENT (Pencil Method) ---")
    new_turns_pen = float(input("Enter turns on pen for NEW wire: "))
    new_length = float(input("Enter total length of turns in mm for NEW wire: "))
    
    print("\n--- 2. OLD WIRE MEASUREMENT (Pencil Method) ---")
    old_turns_pen = float(input("Enter turns on pen for OLD wire: "))
    old_length = float(input("Enter total length of turns in mm for OLD wire: "))
    
    print("\n--- 3. WINDING DETAILS ---")
    old_coil_turns = float(input("Enter total turns in the OLD coil: "))
    
    # Calculations
    new_dia, new_area = calculate_wire_properties(new_turns_pen, new_length)
    old_dia, old_area = calculate_wire_properties(old_turns_pen, old_length)
    
    new_swg = find_closest_swg(new_dia)
    
    # Winding formula: Turns_new = Turns_old * (Area_old / Area_new)
    calculated_new_turns = old_coil_turns * (old_area / new_area)
    
    # Display Results
    print("\n" + "=" * 40)
    print("             CALCULATION RESULTS")
    print("=" * 40)
    print(f"New Wire Diameter : {new_dia:.4f} mm")
    print(f"New Wire SWG      : SWG {new_swg}")
    print(f"New Wire Area     : {new_area:.4f} mm²")
    print("-" * 40)
    print(f"Old Wire Diameter : {old_dia:.4f} mm")
    print(f"Old Wire Area     : {old_area:.4f} mm²")
    print("-" * 40)
    print(f"Required New Turns: {round(calculated_new_turns)} turns")
    print("=" * 40)

if __name__ == "__main__":
    main()

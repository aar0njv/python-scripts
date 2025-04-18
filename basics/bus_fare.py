def calculate_fare(num):
    base_fare_per_km = 10
    dist = float(input("Enter the distance (in km): "))
    total_fare = 0

    for i in range(num):
        age = int(input(f"Enter the age of passenger no {i + 1}: "))

        if age < 5:
            fare = 0
        elif age >= 60:
            fare = (dist * base_fare_per_km) * 0.5
        else:
            fare = dist * base_fare_per_km

        total_fare += fare

    print(f"\nThe total fare for {num} passengers is ₹{total_fare:.2f}")



num = int(input("Enter the number of tickets needed : "))
calculate_fare(num)

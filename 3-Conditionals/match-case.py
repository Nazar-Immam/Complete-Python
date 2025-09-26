#match-case similar to switch case

seat_type = input("Enter the seat type ").lower()



match seat_type :
    case "sleeper":
        print("Rs 300")
    case "ac":
        print("Rs 900")
    case "general":
        print("Rs 100")
    case "luxury":
        print("Rs 1200")
    case _:
        print("Invalid Seat Type")

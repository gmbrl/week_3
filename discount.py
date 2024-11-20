# Define the function to calculate the final price after applying a discount
def calculate_discount(price, discount_percent):
    """Calculate the price after applying the discount."""
    if discount_percent >= 20:
        # Apply the discount if it's 20% or higher
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price, discount_amount
    else:
        # No discount applied if it's less than 20%
        return price, 0

def main():
    """Main function to handle user input and display results."""
    try:
        # Get the original price and discount percentage from the user
        price = float(input("Enter the original price of the item ($): "))
        discount_percent = float(input("Enter the discount percentage: "))
        
        # Validate the input values
        if price < 0 or discount_percent < 0:
            print("Error: Price and discount percentage must be positive values.")
            return

        # Call the calculate_discount function
        final_price, discount_amount = calculate_discount(price, discount_percent)
        
        # Display the result
        if discount_amount > 0:
            print(f"\nThe original price was: ${price:.2f}")
            print(f"Discount applied: ${discount_amount:.2f} ({discount_percent}% off)")
            print(f"Final price after discount: ${final_price:.2f}")
        else:
            print(f"\nNo discount applied. The original price remains: ${final_price:.2f}")
    
    except ValueError:
        print("Error: Please enter valid numbers for price and discount percentage.")

# Call the main function to run the program
if __name__ == "__main__":
    main()

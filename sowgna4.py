def calculate_gst_with_input():
    amount = float(input("Enter the original amount: "))
    gst_rate = float(input("Enter the GST rate (%): "))
    
    gst_amount = amount * (gst_rate / 100)
    total_amount = amount + gst_amount
    
    print(f"GST Amount: {gst_amount:.2f}")
    print(f"Total Amount: ₹{total_amount:.2f}")

# Call the function
calculate_gst_with_input()

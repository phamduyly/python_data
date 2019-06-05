def final_grade(final_result):
    """
    Determine the final grade of a given final result
    :param final_result: a float b/w 0 and 100
    :return: final grade based on the given grade table
    """
    if final_result >= 80:
        final_grade = "HD"
    elif final_result >= 70:
        final_grade = "DI"
    elif final_result >= 60:
        final_grade = "CR"
    elif final_result >= 50:
        final_grade = "PA"
    else:
        final_grade = "NN"
    return final_grade

# Main program
final_result = float(input("Enter your final result: "))

# Make sure that final result is between 0 and 100
while final_result < 0 or final_result > 100:
    print("Final result must be between 0 and 100")
    final_result = float(input("Re-enter your final result: "))
	
# Call the final grade function to get the final grade
print("Your final grade is", final_grade(final_result))
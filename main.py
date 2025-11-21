class NutritionTracker:
    def __init__(self):
        self.Nutrition = []

    def add_nutrition(foodname, time, protein, calories):
        nutrition = {
            'foodname': food_name,
            'time': time,
            'protein': protein,
            'calories': calories
        }
        self.nutrition.append(nutrition)
        print(f"Added nutrition: {foodname} on {time} with {protein} grams of protein, including {calories} calories.")

    def view_nutrition(self):
        if not self.nutrition:
            print("No nutrition to display.")
            return

        for i, eat in enumerate(self.nutrition, 1):
            print(f"{i}. {workout['name']} on {workout['date']} for {workout['duration']} minutes, burning {workout['calories']} calories.")

    def delete_workout(self, index):
        try:
            removed_workout = self.workouts.pop(index - 1)
            print(f"Deleted workout: {removed_workout['name']} on {removed_workout['date']}.")
        except IndexError:
            print("Invalid workout number.")

def main():
    manager = WorkoutManager()

    while True:
        print("\nWorkout Manager")
        print("1. Add workout")
        print("2. View workouts")
        print("3. Delete workout")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter workout name: ")
            date = input("Enter workout date (YYYY-MM-DD): ")
            duration = input("Enter workout duration (in minutes): ")
            calories = input("Enter calories burned: ")
            manager.add_workout(name, date, duration, calories)
        elif choice == '2':
            manager.view_workouts()
        elif choice == '3':
            manager.view_workouts()
            index = int(input("Enter the workout number to delete: "))
            manager.delete_workout(index)
        elif choice == '4':
            print("Exiting the Workout Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

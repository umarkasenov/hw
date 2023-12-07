class Home:
    def new(self, value):
        try:
            integer_value = int(value)
            print(f"Введенное целое число: {integer_value}")
        except ValueError:
            print("Ошибка: Введенное значение не является целым числом.")

home_instance = Home()
home_instance.new(324)
home_instance.new('аываываук')

def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()
test_function()

# inner_function() # Если вызываем "inner_function" вне "test_function", то получаем ошибку.
import os

def clear_screen():
  """Очищает экран терминала.

  Эта функция проверяет операционную систему и выполняет команду для очистки
  экрана. Для Windows используется команда 'cls', для Unix-подобных систем — 'clear'.

  Returns:
      None
  """
  os.system('cls' if os.name == 'nt' else 'clear')

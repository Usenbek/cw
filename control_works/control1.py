


import flet as cw
def func(page: cw.Page):
      page.title = 'Мое первое приложение'
      page.theme_mode = cw.ThemeMode.LIGHT
      greeting_text = cw.Text(value='Hello world')

      greeting_history = []
      favorite_names = []
      fwnames_text = cw.Text(value='Избранные имена: ')
      history_text = cw.Text(value='История приветствий:')

      
      def on_button_click(_):
        print(name_input.value)
        name = name_input.value.strip()
      
        if name:
            greeting_text.value = f'Hello {name}'
            greeting_text.color = None
            name_input.value = None

            greeting_history.append(name)
            print("history>>>>",greeting_history)
            history_text.value = "История приветствий: \n" + "\n".join(greeting_history)
            if len(greeting_history) > 4:
              greeting_history.pop(0)
        else:
            greeting_text.value = 'Введите корректное имя'
            greeting_text.color = cw.Colors.RED
        page.update()

      def add_favorite_name(_):
          fname = name_input.value.strip()
          if fname:
            favorite_names.append(fname)
            print(favorite_names)
            fwnames_text.value='Избранные имена: \n' + '\n'.join(favorite_names)
            greeting_history.append(fname)
            history_text.value='История приветствий: \n' + '\n'.join(greeting_history)
          page.update()
      Izbrannie_button = cw.ElevatedButton(text='send',icon=cw.Icons.SEND,on_click=add_favorite_name)
      
      name_input = cw.TextField(label='Введите имя', on_submit=on_button_click, expand=True)
      page.add(greeting_text,cw.Row([name_input,Izbrannie_button]),cw.Row([history_text,fwnames_text]))

cw.app(target=func)
 
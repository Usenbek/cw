import flet as cw
from db import control_db

def main(page: cw.Page):
  page.title = 'Приложение для покупок'
  page.theme_mode = cw.ThemeMode.LIGHT
  greeting_text = cw.Text(value="Введите свои покупки!")
  # pur_text = cw.Text(value='Ваши покупки: ')
  purchases = cw.Column(spacing=10)

  filter = "Все"

  def load_purchases():
    purchases.controls.clear()
    for pur_id, pur, buyed in control_db.get_pur(filter):
        purchases.controls.append(create_purs_row(pur_id=pur_id, pur=pur, buyed=buyed))
    page.update()

  def create_purs_row(pur_id, pur, buyed):
    pur_text = cw.TextField(value=pur,read_only=True, expand=True)

    delete_purchase_button = cw.IconButton(icon=cw.Icons.DELETE, on_click=lambda e: delete_purchase(pur_id=pur_id))

    checkbox = cw.Checkbox(value=bool(buyed), on_change=lambda e: toggle(pur_id=pur_id, buyed=e.control.value))

    return cw.Row([checkbox,pur_text,delete_purchase_button], alignment=cw.MainAxisAlignment.SPACE_BETWEEN)
  


  def toggle(pur_id, buyed):
    print(f'{pur_id} - {buyed}')
    print(f'{pur_id} - {int(buyed)}')
    control_db.update_pur(pur_id, buyed=int(buyed))
    load_purchases()

  def delete_purchase(pur_id):
    control_db.delete_pur(pur_id)
    load_purchases()  

  def add_purchase(_):
    if pur_input.value:
      purv = pur_input.value
      pur_id = control_db.add_pur(purv)
      purchases.controls.append(create_purs_row(pur_id=pur_id, pur=purv, buyed=None))
      pur_input.value = ''
    page.update()
    

  # delete_purchase_button = cw.IconButton(icon=cw.Icons.DELETE, on_click=delete_purchase)

  pur_input = cw.TextField(label='Введите покупку',on_submit=add_purchase,expand=True)  
  submit_button = cw.ElevatedButton(text='Добавить покупку', on_click=add_purchase)

  def set_filter(filter_type):
    nonlocal filter
    filter = filter_type
    load_purchases()
  
  M_objects = cw.Row([pur_input,submit_button], alignment=cw.MainAxisAlignment.SPACE_BETWEEN)

  filter_buttons = cw.Row([
    cw.ElevatedButton(text='Все', on_click=lambda _: set_filter('Все')),
    cw.ElevatedButton(text='Купленные', on_click=lambda _: set_filter('Купленные')),
    cw.ElevatedButton(text='Не купленные', on_click=lambda _: set_filter('Не купленные')),
  ], alignment=cw.MainAxisAlignment.SPACE_EVENLY)


  page.add(greeting_text,M_objects,filter_buttons,purchases)
  load_purchases()


if __name__ == '__main__':
  control_db.init_db()
  cw.app(target=main) 
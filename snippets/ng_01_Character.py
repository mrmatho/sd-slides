from nicegui import ui

ui.label("Hello")

# 1. Main Container (Centred with a gap)
with ui.column():
    # 2. Styled Card
    with ui.card():
        ui.label('Character Creator')
        # 3. Inputs with Props
        name = ui.input(label='Hero Name').props('outlined clearable')
        lvl = ui.slider(min=0, max=100, value=50, step=5).props('label-always markers')
    
        # 4. Action Button
        with ui.row().classes('justify-end'):
            ui.button('Save Hero', on_click=lambda: ui.notify(f'Saved {name.value}'))
            ui.button('Reset', on_click=lambda: (name.set_value(''), lvl.set_value(50)))


ui.run(native=True)
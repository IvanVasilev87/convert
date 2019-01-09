# Все функции конвертации строятся по одному принципу, так что недостающие надо просто дописать аналогичным образом

def temp_convert(c=None, f=None, k=None):
    if c is not None:
        c = float(c)
        if c < -273.15:
            raise ValueError
        f = (9 / 5) * c + 32
        k = c + 273.15
    elif f is not None:
        f = float(f)
        if f < -459.669:
            raise ValueError
        c = (5 / 9) * (f - 32)
        k = c + 273.15
    elif k is not None:
        k = float(k)
        if k < 0:
            raise ValueError
        c = k - 273.15
        f = (9 / 5) * c + 32
    s = ["{:12.3f}".format(param).strip() for param in (c, f, k)]  #конвертации в строку и дает на выход три сточки
    print('s',s)
    return s
    return (str(param) for param in (c, f, k))


def mass_convert(kg, g, t):
    if kg is not None:
        kg = float(kg)
        if kg < 0:
            raise ValueError
        g = kg * 1000
        t = kg / 1000
    elif g is not None:
        g = float(g)
        if g < 0:
            raise ValueError
        kg = g / 1000
        t = kg / 1000
    elif t is not None:
        t = float(t)
        if t < 0:
            raise ValueError
        kg = t * 1000
        g = kg * 1000
    return (str(param) for param in (kg, g, t))


def len_convert(m, sm, mm):
    if m is not None:
        m = float(m)
        if m < 0:
            raise ValueError
        sm = m * 100
        mm = sm * 10
    elif sm is not None:
        sm = float(sm)
        if sm < 0:
            raise ValueError
        m = sm / 100
        mm = sm * 10
    elif mm is not None:
        mm = float(mm)
        if mm < 0:
            raise ValueError
        sm = mm / 10
        m = sm / 100
    return (str(param) for param in (m, sm, mm))


def press_convert(unit_one, unit_two, unit_three):
    return '', '', ''


def flow_rate_convert(unit_one, unit_two, unit_three):
    return '', '', ''


def turb_prod_convert(unit_one, unit_two, unit_three):
    return '', '', ''


def wot_turb_convert(unit_one, unit_two, unit_three):
    return '', '', ''


def wot_comp_convert(unit_one, unit_two, unit_three):
    return '', '', ''


def b_heat_convert(unit_one, unit_two, unit_three):
    return '', '', ''


def condenser_convert(unit_one, unit_two, unit_three):
    return '', '', ''


def back_work_convert(unit_one, unit_two, unit_three):
    return '', '', ''


# Вместо заглушек  'unit 1', 'unit 2', 'unit 3' требуется написать имена конвертируемых величин в том порядке,
# в котором их принимает функция конвертации

# Набор опций представляет собой кортеж из словарей, где в каждом словаре есть следующие соответствия:
# 'name': название величины, 'units': единицы измерения, 'func': конвертирующая функция

options = (
            {'name': "Temperature",            'units': ('Celsius', 'Fahrenheit', 'Kelvine'), 'func': temp_convert},
            {'name': "Pressure",               'units': ('unit 1', 'unit 2', 'unit 3'),       'func': press_convert},
            {'name': "Mass",                   'units': ('Kg', 'Gr', 'Tonn'),                 'func': mass_convert},
            {'name': "Length",                 'units': ('Meter', 'Sm', 'Mm'),                'func': len_convert},
            {'name': "Flow Rate by Volume",    'units': ('unit 1', 'unit 2', 'unit 3'),       'func': flow_rate_convert},
            {'name': "Turbine Productivity",   'units': ('unit 1', 'unit 2', 'unit 3'),       'func': turb_prod_convert},
            {'name': "Work of the Turbine",    'units': ('unit 1', 'unit 2', 'unit 3'),       'func': wot_turb_convert},
            {'name': "Work of the Compressor", 'units': ('unit 1', 'unit 2', 'unit 3'),       'func': wot_comp_convert},
            {'name': "Boiler Heat",            'units': ('unit 1', 'unit 2', 'unit 3'),       'func': b_heat_convert},
            {'name': "Condenser",              'units': ('unit 1', 'unit 2', 'unit 3'),       'func': condenser_convert},
            {'name': "Back Work Ratio",        'units': ('unit 1', 'unit 2', 'unit 3'),       'func': back_work_convert}
          )


def convert(mode, unit_one=None, unit_two=None, unit_three=None):
    try:
        unit_one, unit_two, unit_three = options[mode]['func'](unit_one, unit_two, unit_three)
    except ValueError:
        unit_one = '' if unit_one is None else unit_one
        unit_two = '' if unit_two is None else unit_two
        unit_three = '' if unit_three is None else unit_three
    finally:
        return unit_one, unit_two, unit_three

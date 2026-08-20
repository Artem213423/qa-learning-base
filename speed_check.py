def check_speed(speed):
    if speed < 0:
        return "error"
    elif 0 <= speed <= 60:
        return "ok"
    else:
        return "warning"
speeds = [-5, 0, 59, 60, 61, 120]
for s in speeds:
    status = check_speed(s)
    if status == "error":
        print(f"{s} км/ч — Ошибка: скорость не может быть отрицательной")
    elif status == "ok":
        print(f"{s} км/ч — ОК: в пределах нормы")
    else:
        print(f"{s} км/ч — Внимание: превышение скорости!")